from flask import jsonify
import logging

class BookController:
    def add_book(self):
        logging.info("----Book_controller.add_book----")

        # TODO: 實現新增書籍邏輯
        return jsonify({"message": "Book added successfully"})
    
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