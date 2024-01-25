import sqlite3


def read_row_from_db(path):
    # Specify the database file path
    db_path = path
    connection = None

    try:
        if db_path:
        # Connect to the SQLite database
            connection = sqlite3.connect(db_path)
            if connection:


                # Create a cursor object
                cursor = connection.cursor()

                # Example: Select all rows from a table
                cursor.execute('SELECT * FROM counter')
                rows = cursor.fetchall()
                print(rows)
                # Process the retrieved rows as needed
        else:
            print('Unable to find the path')
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")

    finally:
        # Close the database connection
        if connection:
            connection.close()