import os
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select


def get_connection():
    server = os.environ.get("SERVER")
    user = os.environ.get("username");
    pwd = os.environ.get("password");

    url = "mssql+pyodbc://{0}:{1}@{2}:{3}/{4}?driver=ODBC+Driver+17+for+SQL+Server".format(user, pwd, server, 1433,
                                                                                           "QuizDB")
    print(url)
    return create_engine(url);


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    try:
        engine = get_connection()
        connection = engine.connect()

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Reflect the database schema
        Base = automap_base()
        Base.prepare(engine, reflect=True)

        # Access the table you want to query
        Questions = Base.classes.Questions

        # Construct a select statement
        stmt = select(Questions).limit(10)

        # Execute the statement
        result = session.execute(stmt)

        # Fetch the results
        rows = result.fetchall()

        # Process the rows
        for row in rows:
            print(row[0].QuestionText)

        # Close the connection
        session.close()
    except Exception as ex:
        print("viata nu e frumoasa")
        print(ex)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
