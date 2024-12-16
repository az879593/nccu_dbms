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
    
    def delete_post(self,post_id):
        logging.info("----Post_controller.delete_post----")
          
        # 確認貼文是否存在
        if post_id not in self.posts:
            logging.error(f"Attempted to delete non-existent post with ID {post_id}")
            return jsonify({"error": "Post not found"}), 404

        # 刪除貼文
        deleted_post = self.posts.pop(post_id)
        logging.info(f"Post deleted successfully: {deleted_post}")

        return jsonify({"message": "Post deleted successfully", "post": deleted_post}), 200
        # TODO: 實現刪除貼文邏輯
        # return jsonify({"message": "Post deleted successfully"})
    
post_controller = PostController()
