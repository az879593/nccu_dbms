from flask import jsonify, request
import logging
from app.database import get_db

class ReplyController:
    def add_reply(self):
        logging.info("----Reply_controller.add_reply----")

        data = request.get_json()
        post_id = data.get('post_id') # 貼文的 ID
        post_userid = data.get('post_userid') # 貼文 user 的 userId
        content = data.get('content') # 回應的文字
        reply_userid = data.get('reply_userid') # Reply 的 userId

        if not reply_userid or not post_id or not post_userid or not content:
            return jsonify({"error": "Missing required fields: reply_userid, post_id, post_userid, content"}), 400
        
        db = get_db()
        try:
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO replies (reply_userid, post_id, post_userid, content) VALUES (?,?,?,?)", 
                (reply_userid, post_id, post_userid, content)
            )
            db.commit()

            reply_id = cursor.lastrowid

            reply = cursor.execute(
                "SELECT reply_id, post_id, post_userid, reply_userid, content, created_at FROM replies WHERE reply_id = ?",
                (reply_id,)
            ).fetchone()
 
            reply_data = {
                "reply_id": reply["reply_id"],
                "reply_userid": reply["reply_userid"],
                "post_id": reply["post_id"],
                "post_userid": reply["post_userid"],
                "content": reply["content"],
                "created_at": reply["created_at"]
            }

        except Exception as e:
            logging.error(f"Error adding reply: {e}")
            return jsonify({"error": str(e)}), 500

        return jsonify({
            "message": "Reply added successfully",
            "reply": reply_data
            }), 201
    
    def private_message(self):
        logging.info("----Reply_controller.private_message----")

        # TODO: 實現一對一留言邏輯
        return jsonify({"message": "Private message sent successfully"})
    
    def reply_notification(self):
        logging.info("----Reply_controller.reply_notification----")

        # TODO: 實現回應通知邏輯
        return jsonify({"message": "Reply notification sent successfully"})
    
    def history(self):
        logging.info("----Reply_controller.history----")

        # TODO: 實現留言歷史紀錄
        return jsonify({"message": "Reply history retrieved successfully", "replies": []})

reply_controller = ReplyController()