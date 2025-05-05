from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/top')
def top():
    return 'se der o paulo ladasdasdasd me a gaita'