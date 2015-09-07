from flask import Flask

app = Flask(__name__)

app.config.from_object('angular_flask.settings')

app.url_map.strict_slashes = False

import angular_flask.core
import angular_flask.models
import angular_flask.controllers
