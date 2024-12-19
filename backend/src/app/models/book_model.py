from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    書名 = db.Column(db.String(255), nullable=False)
    ISBN = db.Column(db.String(13), nullable=False, unique=True)
    作者 = db.Column(db.String(255), nullable=False)
    版本 = db.Column(db.String(100), nullable=False)
    出版年份 = db.Column(db.Integer, nullable=False)
    書本類別 = db.Column(db.String(100), nullable=False)
    價格 = db.Column(db.Float, nullable=False)
    書況 = db.Column(db.String(50), nullable=False)
    posted_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "書名": self.書名,
            "ISBN": self.ISBN,
            "作者": self.作者,
            "版本": self.版本,
            "出版年份": self.出版年份,
            "書本類別": self.書本類別,
            "價格": self.價格,
            "書況": self.書況,
            "posted_time": self.posted_time.strftime('%Y-%m-%d %H:%M:%S')
        }
