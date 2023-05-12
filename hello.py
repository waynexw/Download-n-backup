# Set some temperory variables in CMD 
set db = 1
set db #to verify the value of db
print db

# When you need to set a system env varable, you would have to set in sys advanced setting panel


# new hello swagger api
from flask import Flask
app = Flask(__name__)

@app.route("/waynew")
def hello():
    return "Hello World!"

    
@app.route("/api/NewPlayer")
def NewPlayer():
    return "Hello NewPlayer!"

     
@app.route("/api/checkUserName")
def checkUserName():
    return "Hello checkUserName!"

     
if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
#

"""A Python Flask REST API BoilerPlate (CRUD) Style"""

import argparse
import os
from urllib.request import HTTPHandler
from flask import Flask, jsonify, make_response, render_template
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from routes import request_api
from datetime import datetime

APP = Flask(__name__)
@APP.route('/')

def index():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return "<html><body>\
        <h3>The Current Time: \
        <script>var myDate = new Date(); document.write(myDate.toLocaleString())</script></h3>\
        <div <p>Please go to the index page: <a href=http://localhost:5000/swagger/>Swagger</a>\
        </p></div></body></html>"
    #return render_template('index.html') 
    #return "<body><div <h3>This is a header</h3> <p>This is a paragraph.</p> </div></body>"
    
   

### swagger specific
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
APP.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
