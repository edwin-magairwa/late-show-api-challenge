from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..models.episode import Episode, db

episode_bp = Blueprint('episodes', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def list_episodes():
    episodes = Episode.query.all()
    return jsonify([{'id': e.id, 'date': str(e.date), 'number': e.number} for e in episodes]), 200

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'msg': 'Episode and its appearances deleted'}), 200

class EpisodeController:
    def __init__(self):
        pass

    def create_episode(self, episode_data):
        """Create a new episode."""
        pass

    def get_episode(self, episode_id):
        """Retrieve an episode by its ID."""
        pass

    def update_episode(self, episode_id, episode_data):
        """Update an existing episode."""
        pass

    def delete_episode(self, episode_id):
        """Delete an episode by its ID."""
        pass

    def list_episodes(self):
        """List all episodes."""
        pass