import psycopg2
from config import load_db_config

def create_employee_table():
    """
    Connects to the PostgreSQL database and creates the 'employees' table.
    """
    conn = None
    try:
        # Loads the database configuration
        params = load_db_config()

        # Connects to the Postgresql database
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # SQL statement to create table for employees
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS employees (
            employee_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone_number VARCHAR(20),
            hire_date DATE NOT NULL DEFAULT CURRENT_DATE,
            gender VARCHAR(50) NOT NULL,
            job_id VARCHAR(20),
            salary DECIMAL(10, 2),
            department_id INTEGER
        );
        """

        # Execute the CREATE statement
        cur.execute(create_table_sql)

        # Commits to the database
        conn.commit()
        print("Table 'employees' created successfully!")

        # Close
        cur.close()

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL or creating table: {error}")
    finally:
        if conn:
            conn.close()
            print("PostgreSQL connection closed.")

if __name__ == '__main__':
    create_employee_table()