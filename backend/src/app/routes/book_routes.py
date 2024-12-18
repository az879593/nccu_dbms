from flask import Blueprint
from app.controllers.book_controller import book_controller

book_bp = Blueprint('book', __name__)

book_bp.add_url_rule('add_book', view_func=book_controller.add_book, methods=['POST'])
book_bp.add_url_rule('update_book', view_func=book_controller.update_book, methods=['PUT'])
book_bp.add_url_rule('list_books', view_func=book_controller.list_books, methods=['GET'])
book_bp.add_url_rule('search_books', view_func=book_controller.search_books, methods=['GET'])