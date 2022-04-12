import pandas as pd

def my_method(a):
  df = pd.DataFrame(a)
  df2 = df.sort_values(df.columns[0])
  return df2.to_json(orient='values')
