import sqlite3

conn = sqlite3.connect('employee.db')

cur = conn.cursor()


def execute_query(sql):
    cur.execute(sql)
    return cur.fetchall()


create_table = """
CREATE TABLE EMPLOYEES(
    FIRST TEXT,
    LAST TEXT,
    PAY INTEGER
)
"""
# execute_query(create_table)

# add_user = "INSERT INTO EMPLOYEES VALUES ('Prabesh', 'Lamichhane', 6000)"

select_user = 'select * from EMPLOYEES'
a = execute_query(select_user)
print(a)
conn.commit()
conn.close()
