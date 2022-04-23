import pandas as pd
from r2_factory_platform import ServiceGenerator

service = ServiceGenerator()
app = service.app


def my_method():
    return "Why was 6 afraid of 7? Because 7, 8, 9!"


@service.add_route("/")
def my_method_exposed():
    return my_method()


if __name__ == "__main__":
    service.run_in_debug()
