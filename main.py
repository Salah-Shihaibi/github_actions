import pandas as pd
from r2_factory_platform import ServiceGenerator

service = ServiceGenerator()
app = service.app


def my_method():
    return "Why was 6 afraid of 7? Because 7, 8, 9!"


@service.add_route("/")
def my_method_exposed():
    return my_method()


@service.add_route("/swagger-example", methods =['POST'])
def new_method2():
    """
        Create a new user
        ---
        tags:
          - users
        definitions:
          - schema:
              id: Group
              properties:
                name:
                 type: string
                 description: the group's name
        parameters:
          - in: body
            name: body
            schema:
              id: User
              required:
                - email
                - name
              properties:
                email:
                  type: string
                  description: email for user
                name:
                  type: string
                  description: name for user
                address:
                  description: address for user
                  schema:
                    id: Address
                    properties:
                      street:
                        type: string
                      state:
                        type: string
                      country:
                        type: string
                      postalcode:
                        type: string
                groups:
                  type: array
                  description: list of groups
                  items:
                    $ref: "#/definitions/Group"
        responses:
          201:
            description: User created
    """
    return json.dumps({"data": "example data"})


if __name__ == "__main__":
    service.run_in_debug()
