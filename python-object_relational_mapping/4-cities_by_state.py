#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as sql

    if (len(argv) != 4):
        print('just use: username, password, database name')
        exit(1)

    try:
        db = sql.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    except Exception:
        print('Can not connect to the database')
        exit(0)

    cursor = db.cursor()

    cursor.execute("""SELECT ct.id, ct.name, st.name FROM cities as ct
                      INNER JOIN states as st
                      ON ct.state_id = st.id
                      ORDER BY ct.id ASC;""")

    result_query = cursor.fetchall()

    for row in result_query:
        print(row)

    cursor.close()
    db.close()
