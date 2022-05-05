"""
create or replace function get_by_limit(limitt integer, offsett integer)
returns TABLE(user_id integer, username varchar, surname varchar, phonenumber varchar) as
$$
begin
    return query
    select my_phonebook2.user_id, my_phonebook2.username, my_phonebook2.surname, my_phonebook2.phonenumber from my_phonebook2 limit limitt offset offsett ;
end;
$$
language plpgsql;
"""

import psycopg2
from config import config

def get_by_offset(limitt, offsett):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.callproc('get_by_limit', (limitt, offsett))
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

get_by_offset(3, 2)