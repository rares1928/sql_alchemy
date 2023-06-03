from sqlalchemy import create_engine, select, MetaData
import os
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    server = os.environ.get("SERVER")
    user = os.environ.get("username");
    pwd = os.environ.get("password");

    url = "mssql+pyodbc://{0}:{1}@{2}:{3}/{4}?driver=ODBC+Driver+17+for+SQL+Server".format(user, pwd, server, 1433,
                                                                                           "QuizDB")
    print(url)
    return create_engine(url);


# Create an engine and establish a connection
engine = get_connection()
connection = engine.connect()

# Create a metadata object
metadata = MetaData(bind=engine)

# Reflect the database schema
metadata.reflect()

# Access the table you want to query
questions_table = metadata.tables['Questions']

# Construct a select statement
stmt = select(questions_table).limit(10)

# Execute the statement
result = connection.execute(stmt)

# Fetch the results
rows = result.fetchall()

# Process the rows
for row in rows:
    print(row.QuestionID)

# Close the connection
connection.close()
