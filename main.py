import pandas as pd
from r2_factory_platform import ServiceGenerator

service = ServiceGenerator()
app = service.app


def my_method():
    a = [1,2,3,4]
    df = pd.DataFrame(a)
    df2 = df.sort_values(df.columns[0])
    return df2.to_json(orient="values"),  200


@service.add_route("/")
def my_method_expose():
    return my_method()


if __name__ == "__main__":
    service.run_in_debug()
