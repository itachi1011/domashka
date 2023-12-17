import sqlite3 as sql


def sql_connector():
    con = sql.connect("blog_site.db")
    cur = con.cursor()

    return con, cur


def create_tables():
    con, cur = sql_connector()

    cur.execute("""CREATE TABLE IF NOT EXISTS article(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(100),
                descriptionm TEXT,
                date TIMESTAMP,
                img VARCHAR(255)
                )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS contact(
                address VARCHAR(100),
                phone_number VARCHAR(50),
                location TEXT,
                email VARCHAR(100)
                )""")

def get_timelines():
    con, cur = sql_connector()

    data = cur.execute("SELECT * FROM article").fetchall()
    return data

def get_contacts():
    con, cur = sql_connector()

    data = cur.execute("SELECT * FROM article").fetchone()
    return data