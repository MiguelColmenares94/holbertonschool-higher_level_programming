#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa the safe way"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as sql

    if (len(argv) != 4):
        print('Trying to make a SQL Injection? just use: username,
              password, database name')
        exit(1)

    try:
        db = sql.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    except Exception:
        print("Can not connect to the database")
        exit(0)

    cursor = db.cursor()

    cursor.execute("""SELECT ct.id, ct.name, ct.name FROM cities AS ct
                      INNER JOIN states AS st
                      ON ct.state = st.id
                      ORDER BY ct.id ASC;""")

    result_query = cursor.fetchall()

    for row in result_query:
        print(row)

    cursor.close()
    db.close()
