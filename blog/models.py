from flask_login import UserMixin
from blog import db, login
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Text, Integer, String, DateTime
from datetime import datetime


class User(UserMixin, db.Model):
    id = Column(Integer, primary_key=True, autoincrement='auto')
    email = Column(String(50), unique=True, nullable=False)
    username = Column(String(50), nullable=True)
    password = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    posts = relationship("Post", backref='author')
    comment = relationship("Comment", backref='author')


class Post(db.Model):
    id = Column(Integer, primary_key=True, autoincrement='auto')
    title = Column(String(255), nullable=False)
    body = Column(db.Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    comment = relationship("Comment", backref='post')
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)


class Comment(db.Model):
    id = Column(Integer, primary_key=True, autoincrement='auto')
    body = Column(db.Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
