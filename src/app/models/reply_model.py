from app import db

class Reply(db.Model):
    __talename__ = 'replies'

    reply_id = db.Column(db.Integer, primary_key=True)
    #reply_userid = db.Column(db.Text, db.foreignKey('user.id'), nullable=False)
    reply_userid = db.Column(db.Text,  nullable=False)
    #post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    post_id = db.Column(db.Integer, nullable=False)
    #poster_userid = db.Column(db.Text, db.ForeignKey('users.id'), nullable=False)
    post_userid = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, reply_userid, post_id, post_userid, content):
        self.reply_userid = reply_userid
        self.post_id = post_id
        self.post_userid = post_userid
        self.content = content

    def to_dict(self):
        return {
            "reply_id": self.id,
            "reply_userid":self.reply_userid,
            "post_id": self.post_id,
            "post_userid": self.poster_userid,
            "content": self.content,
            "created_at": self.created_at.isoformat()
        }


