from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.models import db
from server.controllers import auth_controller, episode_controller, guest_controller, appearance_controller

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)
    
    # Register blueprints
    app.register_blueprint(auth_controller.bp)
    app.register_blueprint(episode_controller.bp)
    app.register_blueprint(guest_controller.bp)
    app.register_blueprint(appearance_controller.bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)