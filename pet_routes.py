from flask import Blueprint, request, jsonify
from controllers.pet_controller import PetController

pet_routes = Blueprint('pet_routes', __name__)
pet_controller = PetController()

@pet_routes.route('/', methods=['GET'])
def get_all_pets():
    return jsonify(pet_controller.get_all_pets()), 200

@pet_routes.route('/<int:id>', methods=['GET'])
def get_pet_by_id(id):
    return jsonify(pet_controller.get_pet_by_id(id)), 200

@pet_routes.route('/', methods=['POST'])
def create_pet():
    data = request.json
    return jsonify(pet_controller.create_pet(data)), 201

@pet_routes.route('/<int:id>', methods=['PUT'])
def update_pet(id):
    data = request.json
    return jsonify(pet_controller.update_pet(id, data)), 200

@pet_routes.route('/<int:id>', methods=['DELETE'])
def delete_pet(id):
    return jsonify(pet_controller.delete_pet(id)), 204

def set_pet_routes(app):
    app.register_blueprint(pet_routes, url_prefix='/api/pets')
