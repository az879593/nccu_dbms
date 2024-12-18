from app.database import get_db
import logging

class ReplyService:
    def add_reply(post_id, from_id, to_id, content):
        db = get_db()
        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO replies (from_id, to_id, post_id, content) VALUES (?, ?, ?, ?)", 
                (from_id, to_id, post_id, content)
            )
            db.commit()

            reply_id = cursor.lastrowid
            logging.info(f"Reply added successfully: {reply_id}")

            cursor.execute(
                "SELECT reply_id, from_id, to_id, post_id, content, reply_time "
                "FROM replies WHERE reply_id = ?", 
                (reply_id,)
            )
            reply = cursor.fetchone()

            reply_data = {
                "reply_id": reply[0],
                "from_id": reply[1],
                "to_id": reply[2],
                "post_id": reply[3],
                "content": reply[4],
                "reply_time": reply[5].isoformat()
            }
            return reply_data
        except Exception as e:
            db.rollback()
            raise e
        