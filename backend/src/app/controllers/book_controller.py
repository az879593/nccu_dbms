from flask import jsonify, request
import logging
from app.services.book_service import create_book

class BookController:
    
    def add_book(self):
        """新增書籍"""
        logging.info("----Book_controller.add_book----")

        data = request.get_json()

        # 驗證必要欄位
        required_fields = ["書名", "ISBN", "作者", "版本", "出版年份", "書本類別", "價格", "書況"]
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f"'{field}' is required"}), 400

        try:
            new_book = create_book(data)
            return jsonify({'message': 'Book added successfully', 'book': new_book.to_dict()}), 201
        except Exception as e:
            logging.error(f"Error adding book: {e}")
            return jsonify({'error': 'Failed to add book', 'details': str(e)}), 500

    
    def update_book(self):
        logging.info("----Book_controller.update_book----")

        # TODO: 實現修改書籍邏輯
        return jsonify({"message": "Book updated successfully"})
    
    def get_books(self):
        logging.info("----Book_controller.get_books----")

        # TODO: 實現獲得書籍資料邏輯
        return jsonify({"message": "Books retrieved successfully", "books": []})
    
    def list_books(self):
        logging.info("----Book_controller.list_books----")

        # TODO: 實現獲得書籍列表邏輯
        return jsonify({"message": "Books listed successfully", "books": []})
    
    def search_books(self):
        logging.info("----Book_controller.search_books----")

        # TODO: 實現書籍搜尋邏輯
        return jsonify({"message": "Books searched successfully", "books": []})
    
book_controller = BookController()