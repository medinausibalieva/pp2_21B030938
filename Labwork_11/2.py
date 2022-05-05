"""
create or replace procedure insert_user(name varchar, surname varchar, number varchar)
as $$
begin
	insert into My_Phonebook2(username, surname, phonenumber) values (name, surname, number);	
end;
$$
language plpgsql;
"""

"""
create or replace procedure update_number(name varchar, surname varchar, number varchar)
as $$
begin
	update My_Phonebook2 set phonenumber = number where username = name ;
end;
$$
language plpgsql;
"""
import psycopg2
from config import config

name = input()
surname = input()
phone = input()

def insert(name, surname, number):
    global phonenumber
    params = config() 
    conn = psycopg2.connect(**params)
    sql = """
    SELECT exists(select * from My_Phonebook2 where username=%s);
    """
    cur = conn.cursor()
    cur.execute(sql, (name, ))
    result = cur.fetchone()
    
    if result[0]:
        sql = """select phonenumber from My_Phonebook2 where username=%s ;"""
        cur.execute(sql, (name,  ))
        conn.commit()
        numbers = cur.fetchone()
        if number != numbers[0]:
            print('updated!')
            cur.execute('call update_number(%s, %s, %s)', (name, surname, number))
            conn.commit()
            cur.close()
    else:
        cur.execute('call insert_user(%s, %s, %s)', (name, surname, number))
        conn.commit()
        cur.close()
insert(name, surname, phone)

