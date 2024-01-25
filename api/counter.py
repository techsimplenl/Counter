"""Counter Module"""
from flask import request, jsonify, Blueprint
from sqlalchemy.exc import IntegrityError
from api.models import Counter,db
from api.schemas import counter_schema

# Create a Flask Blueprint for counter-related endpoints
counter_bp = Blueprint('counter', __name__, url_prefix='/counter')
@counter_bp.route('', methods=['POST'])
def create_counter():
    """Create a new counter"""

    # Check if the request is JSON
    if not request.is_json:
        raise ValueError("Unsupported Media Type. Please send a JSON request.")
    if not request.get_json():
        raise ValueError("Empty JSON request. Please provide valid data.")
    # Deserialize the JSON into an object and store it in the database
    initial_value = request.json['initial_value']
    # Create a new counter with the given initial value
    new_counter = Counter(counter=initial_value, initial_value=initial_value)
    try:
        # Add the new counter to the session and commit the changes   
        db.session.add(new_counter)
        db.session.commit()
        # Return the created counter ID with a 201 status code
        return jsonify({'id':new_counter.id}),201
    except KeyError:
        return jsonify({'error': 'Invalid request. Missing initial value parameter.'}), 400
    except IntegrityError:
        # Rollback the session in case of an IntegrityError
        db.session.rollback()
        # Return a 400 status code with an error message
        return jsonify({'error':f'Duplicate counter creation. Counter ID must be unique.'}), 400
    except Exception as e:
        # If any other exception occurs, rollback the session and return a 500 status
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