"""Counter Module"""
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from app import app, db
from models import Counter
from schemas import counter_schema

@app.route('/counter', methods=['POST'])
def create_counter():
    """function for creating counter"""
    try:
        initial_value = request.json['initial_value']
        new_counter = Counter(value=initial_value)
        db.session.add(new_counter)
        db.session.commit()
        return jsonify({'value':new_counter.value, 'initial_value': new_counter.initial_value}),201
        # return counter_schema.dump(new_counter).data, 201
    except KeyError:
        return jsonify({'error': 'Invalid request. Missing initial value parameter.'}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error':'Duplicate counter creation. Counter ID must be unique.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500 
@app.route('/counter/<int:counter_id>', methods=['PATCH'])
def increment_counter(counter_id):
    """Function to increment the value of a given counter."""
    try:
        counter = Counter.query.get(counter_id)
        if counter:
            counter.value += 1
            db.session.commit()
            return jsonify({'message': 'Counter incremented successfully.'}), 201
        return jsonify({'error': 'No such counter exists.'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/counter/<int:counter_id', methods=['GET'])
def read_counter(counter_id):
    """Function to get counter by id"""
    try:
        counter = Counter.query.get(counter_id)
        if counter:
            return counter_schema.jsonify(counter)
        return jsonify({'error':'Counter not found'}), 404
    except Exception as e:
        return jsonify({'error':str(e)}), 500