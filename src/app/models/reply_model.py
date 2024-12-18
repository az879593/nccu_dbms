from app import db

class Reply(db.Model):
    __tablename__ = 'replies'

    reply_id = db.Column(db.Integer, primary_key=True)
    #reply_userid = db.Column(db.Text, db.ForeignKey('user.id'), nullable=False)
    from_id = db.Column(db.Integer,  nullable=False)
    #post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    to_id = db.Column(db.Integer, nullable=False)
    #poster_userid = db.Column(db.Text, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    reply_time = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            "reply_id": self.reply_id,
            "from_id":self.from_id,
            "to_id": self.to_id,
            "post_id": self.post_id,
            "content": self.content,
            "reply_time": self.reply_time.isoformat() if self.reply_time else None
        }


