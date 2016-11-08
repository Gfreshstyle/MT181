from flask import Flask

app = Flask(__name__)
@app.route('/auth')

def auth(username, password):
