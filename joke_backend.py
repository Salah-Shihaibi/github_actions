import requests
from backend_framework_library import ServiceGenerator

service = ServiceGenerator()
app = service.app


def get_joke():
	r = requests.get('http://localhost:8080/')
	return r.json()["joke"]


@service.add_route("/joke")
def my_method():
	joke = get_joke()
	return joke


if __name__ == "__main__":
	service.run_in_debug()
