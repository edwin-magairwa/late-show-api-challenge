from flask import Blueprint, request, jsonify
from models.guest import Guest

guest_controller = Blueprint('guest_controller', __name__)

@guest_controller.route('/guests', methods=['POST'])
def create_guest():
    data = request.get_json()
    new_guest = Guest(name=data['name'], email=data['email'])
    new_guest.save()
    return jsonify(new_guest.to_dict()), 201

@guest_controller.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests]), 200

@guest_controller.route('/guests/<int:guest_id>', methods=['GET'])
def get_guest(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    return jsonify(guest.to_dict()), 200

@guest_controller.route('/guests/<int:guest_id>', methods=['PUT'])
def update_guest(guest_id):
    data = request.get_json()
    guest = Guest.query.get_or_404(guest_id)
    guest.name = data['name']
    guest.email = data['email']
    guest.save()
    return jsonify(guest.to_dict()), 200

@guest_controller.route('/guests/<int:guest_id>', methods=['DELETE'])
def delete_guest(guest_id):
    guest = Guest.query.get_or_404(guest_id)
    guest.delete()
    return jsonify({'message': 'Guest deleted successfully'}), 204