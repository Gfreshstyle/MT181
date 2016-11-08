from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello flask'

@app.route('/greet')
def greet(name='name'):
	return 'hello ' +name 

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')