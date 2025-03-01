import pandas as pd


def insert_to_db(data, file_path):
    data_in_pandas = pd.DataFrame(data=data)
    data_in_pandas.to_csv(file_path, index=False)
    pass


def read_from_db(file, rows, colomns):
    pass
