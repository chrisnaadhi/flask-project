from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Chrisna'}
    posts = [
        {
            'author': {'username': 'Adhi'},
            'body': 'Nice move you got there!'
        },
        {
            'author': {'username': 'Pranoto'},
            'body': 'Touhou 3D - Imperishable Night is the most nice things in 2020!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)