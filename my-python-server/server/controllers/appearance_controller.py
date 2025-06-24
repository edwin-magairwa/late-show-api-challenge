from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..models.appearance import Appearance, db

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    appearance = Appearance(
        rating=data['rating'],
        guest_id=data['guest_id'],
        episode_id=data['episode_id']
    )
    db.session.add(appearance)
    db.session.commit()
    return jsonify({'id': appearance.id, 'rating': appearance.rating}), 201

class AppearanceController:
    def __init__(self):
        pass

    def create_appearance(self, guest_id, episode_id):
        pass

    def get_appearance(self, appearance_id):
        pass

    def update_appearance(self, appearance_id, guest_id, episode_id):
        pass

    def delete_appearance(self, appearance_id):
        pass

    def list_appearances(self):
        pass