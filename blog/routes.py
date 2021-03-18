from blog import app, session, login
from blog.models import User, Post
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user, fresh_login_required
from blog import _


@login.unauthorized_handler
def unauthorized():
    return redirect('/')


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    return render_template('post.html', post=post)

@app.route('/users/<int:user_id>')
def user_posts(user_id):
    posts = Post.query.filter_by(user_id=user_id)
    print(posts)
    return render_template('posts.html', posts=posts)


@app.route('/login')
def login_get():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()

    if not user:
        flash('invalid user')
        return redirect(url_for('login_get'))

    login_user(user)
    flash(_('You were successfully logged in'))
    return redirect(url_for('home'))


@app.route('/home')
@login_required
def home():
    return render_template('home.html', user=current_user)


@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()

    return render_template('index.html')


@app.route('/language/<language>')
def switch_language(language):
    session['language'] = language

    return redirect(request.referrer)
