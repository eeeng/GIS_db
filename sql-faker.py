import psycopg2
from faker import Faker
from config import config

def connect():
    fake=Faker("tr_TR")

    conn=None

    try:
        params=config()

        #connect p-sql server

        print("Connecting to the PostgreSQL database...")
        conn=psycopg2.connect(**params)

        #create cursor
        cur=conn.cursor()
        print("PostgreSQL database version:")
        cur.execute("SELECT version()")

        db_version=cur.fetchone()[0]
        print(db_version)
        
        cur.execute("SELECT COUNT(*) FROM bina")
        bina_count=cur.fetchone()

        for i in range(1, bina_count+1):
            cur.execute(f"UPDATE bina SET (asansor, daire_sayisi, kat_adedi, bina_adi) ) = ({fake.booelan(change_of_getting_true=60)}, {fake.random_element(elements=(1, 2, 3))}, {fake.random_element(elements=(3, 4, 5, 6))}, '{fake.name()}') where id={i}")
            print(f"id: {i} executed")



        cur.execute("SELECT COUNT(*) FROM mahalle")
        mahalle_count=cur.fetchone()[0]

        for i in range(1, mahalle_count+1):
            cur.execute(f"UPDATE mahalle SET (mahalle_adi) ) = '{fake.name()}' where id={i}")
            print(f"id: {i} executed")

        conn.commit()
        cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed")


if __name__=='__main__':
    connect()