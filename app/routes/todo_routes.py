from flask import Blueprint, request, jsonify
from ..models import TodoItem
from ..schemas import todo_schema, todos_schema
from .. import db

bp = Blueprint('todos', __name__, url_prefix='/todo')


@bp.route('/', methods=['POST'])
def add_todo():
    try:
        name = request.json['name']
        is_executed = request.json['is_executed']

        new_todo_item = TodoItem(name, is_executed)
        db.session.add(new_todo_item)
        db.session.commit()

        return todo_schema.jsonify(new_todo_item)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/', methods=['GET'])
def get_todos():
    try:
        all_todos = TodoItem.query.all()
        result = todos_schema.dump(all_todos)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/<id>', methods=['PUT', 'PATCH'])
def execute_todo(id):
    try:
        todo = TodoItem.query.get(id)
        todo.is_executed = not todo.is_executed
        db.session.commit()
        return todo_schema.jsonify(todo)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/<id>', methods=['DELETE'])
def delete_todo(id):
    try:
        todo_to_delete = TodoItem.query.get(id)
        db.session.delete(todo_to_delete)
        db.session.commit()
        return todo_schema.jsonify(todo_to_delete)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
