import psycopg2

def delete_data(username):
    sql = """
    DELETE FROM My_PhoneBook
    WHERE username = %s
    """
    conn = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='21B030938'
        )
        cur = conn.cursor()
        cur.execute(sql, (username,))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
username = input()
delete_data(username)