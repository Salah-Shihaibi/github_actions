from flask import Flask, Response, request
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

    def add_route(self, rule, **options):
        def outer(fnc):
            def inner():
                return Response(
                    response=json.dumps(
                        fnc(request.get_json(force=True, silent=True)),
                        indent=4,
                    ),
                    status=200,
                    mimetype="application/json",
                )
            inner.__name__ = fnc.__name__
            endpoint = options.pop("endpoint", None)
            self.app.add_url_rule(rule, endpoint, inner, **options)
        return outer

    def run_in_debug(self, debug=True):
        self.app.run(debug=debug, host="0.0.0.0", port=8080)
