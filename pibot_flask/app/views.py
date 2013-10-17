from flask import render_template, flash, redirect
from app import app
from forms import LoginForm


@app.route('/login', methods = ['GET', 'POST'])
def login():
    user = { 'nickname' : 'Andriy' } # fake user
    form = LoginForm()
    return render_template('login.html',
        title = "Sign In",
        form = form,
        user = user)

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname' : 'Andriy' } # fake user
    return render_template("index.html",
        title='Home',
        user = user)
