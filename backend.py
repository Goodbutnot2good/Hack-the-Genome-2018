from flask import Flask, request, jsonify, session, render_template
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    session['data'] = []
    session.modified = True
    return "Hello world!"
    #ask sequencing this data
    

@app.route('/results', methods=['GET', 'POST'])
def showresults():

	return "This is the results page"


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)
