from flask import Blueprint
from app.controllers.home_controller import home_controller

home_bp = Blueprint('home', __name__)

home_bp.add_url_rule('/', view_func=home_controller.index, methods=['GET'])