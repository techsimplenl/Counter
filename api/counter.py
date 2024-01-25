"""Counter Module"""
from flask import request, jsonify, Blueprint
from sqlalchemy.exc import IntegrityError
from api.models import Counter,db
from api.schemas import counter_schema

counter_bp = Blueprint('counter', __name__, url_prefix='/counter')
@counter_bp.route('/', methods=['POST'])
def create_counter():
    """function for creating counter"""
    try:
        if not request.is_json:
            raise ValueError("Unsupported Media Type. Please send a JSON request.")
        if not request.get_json():
            raise ValueError("Empty JSON request. Please provide valid data.")
        print("Request Data:", request.data)  # Print the request data for debugging
        initial_value = request.json['initial_value']
        new_counter = Counter(counter=initial_value, initial_value=initial_value)
        db.session.add(new_counter)
        db.session.commit()
        return jsonify({'id':new_counter.id}),201
    except KeyError:
        return jsonify({'error': 'Invalid request. Missing initial value parameter.'}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error':f'Duplicate counter creation. Counter ID must be unique.'}), 400
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500 
@counter_bp.route('/<int:counter_id>', methods=['PATCH'])
def increment_counter(counter_id):
    """Function to increment the value of a given counter."""
    try:
        counter = Counter.query.get(counter_id)
        if counter:
            counter.counter += 1
            db.session.commit()
            return jsonify({'message': f'Counter incremented successfully with id {counter.id}.'}), 201
        return jsonify({'error': 'No such counter exists.'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400
@counter_bp.route('/<int:counter_id>', methods=['GET'])
def read_counter(counter_id):
    """Function to get counter by id"""
    try:
        counter = Counter.query.get(counter_id)
        if counter:
            return counter_schema.jsonify(counter)
        return jsonify({'error':'Counter not found'}), 404
    except Exception as e:
        return jsonify({'error':str(e)}), 500