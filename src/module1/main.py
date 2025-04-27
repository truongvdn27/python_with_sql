import os
import sys
from dotenv import load_dotenv


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.utils.libs import connect_to_db, create_table, drop_table



if __name__ == "__main__":

    '''
    TASK1: Connect to the databse using the connection string from the .env file.
    TASK2: Create a table in the database using python code.
    TASK3: Drop the table using python code.
    '''

    #TASK1;
    conn = connect_to_db()
    print("Connection successful !!")

    #TASK2;
    load_dotenv()
    query = os.getenv("query")
    create_table(conn, "test_table", query)
    print("Table created successfully !!")

    #TASK3;
    drop_table(conn, "test_table")
    print("Table dropped successfully !!")

    pass
