#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as sql

    try:
        db = sql.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    except Exception:
        print("Can not connect to the database")
        exit(0)

    sql_querry = argv[4]

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = '{:s}' \
                    ORDER BY id ASC;".format(sql_querry))

    result_query = cursor.fetchall()

    for row in result_query:
        print(row)

    cursor.close()
    db.close()
