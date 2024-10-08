import sqlite3


def try_create_db():

    try:

            ### create or connect to db

            conn = sqlite3.connect("devices.db")

            ### create curser
            c = conn.cursor()

            ## create table

            c.execute("""CREATE TABLE devices (
                    name text,
                    ip text,
                    username text,
                    password text,
                    secret text
                    )""")

            conn.commit()

    except:
            pass