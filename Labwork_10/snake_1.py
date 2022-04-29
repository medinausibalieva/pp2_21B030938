import psycopg2

def create_tables():
    command1 = (
        """
        CREATE TABLE game (
            user_id serial PRIMARY KEY,
            username VARCHAR (50) UNIQUE NOT NULL,
            level INT
        );
        """
    )
    conn = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='21B030938'
        )
        cur = conn.cursor()
        cur.execute(command1)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
        if conn is not None:
            conn.close()
        
create_tables()
    

