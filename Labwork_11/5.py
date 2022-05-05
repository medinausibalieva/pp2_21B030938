"""
create or replace procedure deletedata(name varchar)
as
$$
begin
    delete
    from My_Phonebook2
    where username = name ;
end;
$$
    LANGUAGE plpgsql;
"""
import psycopg2
from config import config


def delete_data(username):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('call deletedata(%s)', (username, ))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

delete_data('Ameli')
