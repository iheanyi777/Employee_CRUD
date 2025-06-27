import psycopg2
from config import load_db_config

def insert_multiple_employees(employee_input):
    """
    Inserts multiple employee records into the 'employees' table.
    employees_data should be a list of tuples, where each tuple
    represents a row of data in the correct column order.
    """
    conn = None
    try:
        params = load_db_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        print("Truncating 'employees' table...")
        cur.execute("TRUNCATE TABLE employees RESTART IDENTITY CASCADE;")

        insert_sql = """
        INSERT INTO employees (
            first_name, last_name, email, phone_number,
            hire_date, gender, job_id, salary, department_id
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """

        # employee_input is a list of tuples
        cur.executemany(insert_sql, employee_input)

        conn.commit()
        print(f"{cur.rowcount} rows inserted successfully!")
        cur.close()

    except (Exception, psycopg2.Error) as error:
        print(f"Error inserting multiple employees: {error}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    employees_to_insert = [
        ("Charlie", "Brown", "charlie.b@example.com", "123-456-7899", "2023-03-01", "MALE", "SALES_REP", 55000.00, 103),
        ("Diana", "Prince", "diana.p@example.com", "400-401-4012", "2024-11-10", "FEMALE", "MARKETING", 62000.00, 104),
        ("Eve", "Adams", "eve.a@example.com", None, "2025-06-18", "FEMALE", "SW_DEV", 95000.00, 101)
    ]

    insert_multiple_employees(employees_to_insert)