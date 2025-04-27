import os
import sys
import ast
from dotenv import load_dotenv


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from src.utils.libs import connect_to_db, create_table, drop_table, insert_data, query_func, update_data, delete_data



if __name__ == "__main__":

    '''
    TASK1: Connect to the databse using the connection string from the .env file.
    TASK2: Create a table in the database using python code.
    TASK3: Drop the table using python code.
    TASK4: Insert data into the table using python code.
    TASK5: Query the table using python code.
    TASK6: Update the table using python code.
    TASK7: Delete the table using python code.
    '''

    load_dotenv()
    data_base = ast.literal_eval(os.getenv("data_list"))

    #TASK1: Connect to the databse using the connection string from the .env file.
    conn = connect_to_db()
    print("Connection successful !!")

    #TASK2: Create a table in the database using python code.
    query = os.getenv("query")
    create_table(conn, "test_table", query)
    print("Table created successfully !!")

    #TASK3: Drop the table using python code.
    drop_table(conn, "test_table")
    print("Table dropped successfully !!")

    #TASK4: Insert data into the table using python code.
    insert_data(conn, "test_table", data_base)
    print(f"Data inserted successfully for data base !!")

    #TASK5: Query the table using python code.
    data = query_func(conn, "SELECT * FROM test_table")
    print("Data queried successfully !!")
    print(data)
    
    # #TASK6: Update the table using python code.
    update_data(conn, "test_table", "age", "1", 60)
    data = query_func(conn, "SELECT * FROM test_table")
    print("Data queried successfully !!")
    print(data)

    # #TASK7: Delete the table using python code.
    delete_data(conn,"test_table", "id", 1)
    data = query_func(conn, "SELECT * FROM test_table")
    print("Data queried successfully !!")
    print(data)

    pass
