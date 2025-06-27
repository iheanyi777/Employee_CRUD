import psycopg2
from config import load_db_config

def fetch_employees_data():
    """
    Connects to the PostgreSQL database and fetches all records
    from the 'employees' table.
    """
    conn = None
    try:
        # Loads database configuration
        params = load_db_config()

        # Connects to the PostgreSQL database
        print('Connecting to the PostgreSQL database to fetch data...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # For SQL to select all columns from the employees table
        select_sql = "SELECT * FROM employees ORDER BY employee_id;"

        # Executes the SELECT statement
        cur.execute(select_sql)

        # Fetches all rows from the result set
        rows = cur.fetchall()

        # Prints the column names
        # cur.description provides metadata about the columns
        if cur.description:
            column_names = [desc[0] for desc in cur.description]
            print("\nColumn Names:", column_names)

        # This prints the fetched data
        if rows:
            print("\nEmployee Data:")
            for row in rows:
                print(row)
        else:
            print("No employees found in the table.")

        # Closes the cursor and connection
        cur.close()

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL or fetching data: {error}")
    finally:
        if conn:
            conn.close()
            print("PostgreSQL connection closed.")

if __name__ == '__main__':
    fetch_employees_data()