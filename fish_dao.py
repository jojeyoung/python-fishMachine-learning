import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import sqlalchemy as db
from data.fish_api2 import getFishData


engine = db.create_engine(
    "mariadb+mariadbconnector://python:python1234@127.0.0.1:3306/pythondb")


def insert():
    fishs = getFishData()
    fishs.to_sql("test", engine, index=False, if_exists="replace")


def select():
    df = pd.read_sql(sql="select * from fish", con=engine)
    print(df)
    pass


insert()
# select()
