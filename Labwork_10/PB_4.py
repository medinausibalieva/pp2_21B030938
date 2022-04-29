import psycopg2

def order_by(something):
    sql = """ 
    SELECT * FROM My_PhoneBook ORDER BY %s;
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
        cur.execute(sql, (something,))
        all_rows = cur.fetchall()
        for row in all_rows:
            print(row)
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

something = str(input())
order_by(something)