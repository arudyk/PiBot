from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN

"""
author: Andriy Rudyk
        Tim Sizemore

date: 21.10.2013

Views that pass the required information to our templates to generate dynamic
pages.
"""

@app.route('/')
@app.route('/index')
def index():
    """
    Handles the homepage.
    """
    user = g.user

    return render_template("index.html",
	                       title='Home',
                           user=user)

@app.before_request
def before_request():
    """
    Makes sure ew have a user before every request.
    """
    g.user = current_user

@lm.user_loader
def load_user(id):
    """
    Returns a user object based on the id given.
    """
    return User.query.get(int(id))

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    """
    Login page, we have the ability to GET the login page, or POST to it in
    order to login into the system.
    """
    if g.user is not None and g.user.is_authenticated():
        # if already logged in, redirect to index page
        return redirect(url_for('index'))
    form = LoginForm() # generate login form

    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])

    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])

@app.route('/logout')
def logout():
    """
    Signs a user out from the system and redirect to the index page.
    """
    logout_user()
    return redirect(url_for('index'))

@oid.after_login
def after_login(resp):
    """
    Adds a user to the database, if authentication with openid is successful.
    """
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))

    user = User.query.filter_by(email = resp.email).first()

    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False

    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)

    return redirect(request.args.get('next') or url_for('index'))

@app.route('/user/<nickname>')
@login_required
def user(nickname):
    """
    User profile page.
    """
    user = User.query.filter_by(nickname = nickname).first()
    
    if user == None:
        flash('User ' + nickname + ' not found.')
        return redirect(url_for('index'))
    
    return render_template('user.html',
                           user = user)
