import os
import sys
import ast
from dotenv import load_dotenv


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.utils.libs import connect_to_db, create_table, drop_table, insert_data, query_func



if __name__ == "__main__":

    '''
    TASK1: Connect to the databse using the connection string from the .env file.
    TASK2: Create a table in the database using python code.
    TASK3: Drop the table using python code.
    TASK4: Insert data into the table using python code.
    '''

    load_dotenv()
    data_base = ast.literal_eval(os.getenv("data_list"))

    #TASK1;
    conn = connect_to_db()
    print("Connection successful !!")

    #TASK2;
    # query = os.getenv("query")
    # create_table(conn, "test_table", query)
    # print("Table created successfully !!")

    #TASK3;
    # drop_table(conn, "test_table")
    # print("Table dropped successfully !!")

    #TASK4;
    insert_data(conn, "test_table", data_base)
    print(f"Data inserted successfully for data base !!")
    data = query_func(conn, "SELECT * FROM test_table")
    print("Data queried successfully !!")
    print(data)
    
    pass
