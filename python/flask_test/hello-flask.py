from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<username>')
def show_user_profile(username=None):
    return render_template('user_profile.html', username=username)
