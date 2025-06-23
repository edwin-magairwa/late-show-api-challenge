from flask import Flask
from server.controllers.guest_controller import GuestController
from server.controllers.episode_controller import EpisodeController
from server.controllers.appearance_controller import AppearanceController
from server.controllers.auth_controller import AuthController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SECRET_KEY'] = SECRET_KEY
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

db.init_app(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(guest_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(appearance_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)