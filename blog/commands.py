import random
from faker import Faker
from blog import app
from blog import models as model
from blog import db

fake = Faker()


@app.cli.command("seed")
def seed():
    db.drop_all()
    db.create_all()

    for i in range(10):
        create_user()
    db.session.commit()

    for i in range(20):
        create_post(random.randint(1, 10))
    db.session.commit()

    for i in range(30):
        create_comment(random.randint(1, 10), random.randint(1, 20))
    db.session.commit()


def create_user():
    user = model.User(email=fake.email(), username=fake.name())
    db.session.add(user)
    db.session.commit()
    return user


def create_post(user_id):
    post = model.Post(title=fake.text(max_nb_chars=100), body='<br>'.join(fake.texts(10)), user_id=user_id)
    db.session.add(post)
    return post


def create_comment(user_id, post_id):
    comment = model.Comment(body='<br>'.join(fake.texts(3)), user_id=user_id, post_id=post_id)
    db.session.add(comment)
    return comment
