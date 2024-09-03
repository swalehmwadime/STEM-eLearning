from flask import Blueprint, render_template
from .model import db, User, Course

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')
