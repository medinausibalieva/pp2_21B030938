'''
create or replace procedure add_user(username varchar, surname varchar, phonenumber varchar)
as
$$
begin
  insert into My_Phonebook2(username, surname, phonenumber) values(username, surname, phonenumber);  
end;
$$
    language plpgsql;
'''
import psycopg2
from config import config

list = (('Daryn', 'Akanov','8700-555-12-34'), ('Akniet', 'Ryskul', '8747-747-74-47'), ('Madi','Bakiev', '8701-111-10-00'))

def add_users(ussers):
    params = config()
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    try:
        cursor.executemany('call add_user(%s, %s, %s)', ussers)
        print('succesfully added!')
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        conn.close()
        
add_users(list)