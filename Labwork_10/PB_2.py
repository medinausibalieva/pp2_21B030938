import psycopg2
from config import config
import csv

def insert_user_list(user_list):
    sql = """
    insert into My_PhoneBook(username, phonenumber) values (%s, %s);
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(sql, user_list)
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

with open('my.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    insert_user_list(csv_reader)

#  insert into My_PhoneBook (username, phonenumber) values('Sanzhar', '8701-363-36-36') ;
# insert into My_PhoneBook (username, phonenumber) values('Tima', '8701-444-44-44') ;    