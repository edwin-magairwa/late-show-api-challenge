from flask import Flask
from server.controllers.guest_controller import GuestController
from server.controllers.episode_controller import EpisodeController
from server.controllers.appearance_controller import AppearanceController
from server.controllers.auth_controller import AuthController

app = Flask(__name__)

# Initialize controllers
guest_controller = GuestController()
episode_controller = EpisodeController()
appearance_controller = AppearanceController()
auth_controller = AuthController()

# Set up routes
@app.route('/guests', methods=['GET', 'POST'])
def manage_guests():
    return guest_controller.handle_request()

@app.route('/episodes', methods=['GET', 'POST'])
def manage_episodes():
    return episode_controller.handle_request()

@app.route('/appearances', methods=['GET', 'POST'])
def manage_appearances():
    return appearance_controller.handle_request()

@app.route('/auth', methods=['POST'])
def manage_auth():
    return auth_controller.handle_request()

if __name__ == '__main__':
    app.run(debug=True)