from flask import Flask

app = Flask(__name__)

# import all the routes from the routes file into the current package

from . import routes