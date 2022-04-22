from flask import Flask
import json
from flask_swagger import swagger
from flask_cors import CORS

# TODO:
# Post requests (conditional logic)
# do they name endpoints or take functions names?


class ServiceGenerator:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)

        @self.app.route("/spec")
        def spec():
            return json.dumps(swagger(self.app))

    def add_route(self, *args, **kwargs):
        return self.app.route(*args, **kwargs)

    def run_in_debug(self, debug=True):
        self.app.run(debug=debug, host="0.0.0.0", port=8080)
