from flask import Flask
from .model import db 
 # Import db here

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object('app.config.Config')
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints or routes
    from .routes import main
    app.register_blueprint(main)
    
    return app


