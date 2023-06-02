import os
from dotenv import load_dotenv
load_dotenv()

import sqlalchemy
from sqlalchemy import  create_engine

from sqlalchemy import select

def get_connection():
    server = os.environ.get("SERVER")
    user = os.environ.get("username");
    pwd = os.environ.get("password");

    url = "mssql+pyodbc://{0}:{1}@{2}:{3}/{4}?driver=ODBC+Driver+17+for+SQL+Server".format(user, pwd, server, 1433, "ouizdb")
    print(url)
    return create_engine(url);


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    try:
        engine = get_connection()
        connection = engine.connect()
        print("viata e frumoasa")
        meta_data = sqlalchemy.MetaData()
        tabel = sqlalchemy.Table('Questions', meta_data, autoload_with=engine)
        stmt = sqlalchemy.select([tabel]).limit(10)
        result = connection.execute(stmt)
        print(result.fetchall())


    except Exception as ex:
        print("viata nu e frumoasa")
        print(ex)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
