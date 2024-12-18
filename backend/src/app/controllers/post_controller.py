from flask import jsonify
import logging

class PostController:
    def add_post(self):
        logging.info("----Post_controller.add_post----")

        # TODO: 實現新增貼文邏輯
        return jsonify({"message": "Post added successfully"})
    
    def update_post(self):
        logging.info("----Post_controller.update_post----")

        # TODO: 實現修改貼文邏輯
        return jsonify({"message": "Post updated successfully"})
    
    def delete_post(self):
        logging.info("----Post_controller.delete_post----")

        # TODO: 實現刪除貼文邏輯
        return jsonify({"message": "Post deleted successfully"})
    
post_controller = PostController()
