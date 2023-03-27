from flask import render_template
from core import app



@app.route('/', methods=['GET'])
def index():
    greeting = "Howdy There Partner"
    return render_template('index.html', greet=greeting)

