from flask import jsonify
import logging

class ReplyController:
    def add_reply(self):
        logging.info("----Reply_controller.add_reply----")

        # TODO: 實現新增回應邏輯
        return jsonify({"message": "Reply added successfully"})
    
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