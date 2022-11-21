import json
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return json.dumps({'name': 'your name here',
                       'email': 'your_name@alvant.nl'})
app.run()