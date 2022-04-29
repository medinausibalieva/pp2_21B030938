import psycopg2
from config import config

def update_user(user_id, phonenumber):
    sql = """
    update My_PhoneBook
    set phonenumber = %s
    where user_id = %s;
    """
    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (phonenumber, user_id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

update_user(3, '8700-700-70-07')
update_user(6, '8747-444-44-44')