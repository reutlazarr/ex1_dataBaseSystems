import mysql.connector
if __name__ == '__main__':
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="covid_db",
    port='3307',
    )
    cursor = mydb.cursor()
    # Find the difference between the number of total cases in February (across all
    # years) and in March(February-March).

    cursor.execute("""
        SELECT x.date, x.new_cases, x.location, y.location
        FROM (SELECT * FROM covid_deaths LIMIT 1000) As x,
             (SELECT * FROM covid_deaths LIMIT 1000) AS y
        WHERE x.new_cases = y.new_cases
        AND x.location < y.location
        AND x.date = y.date
        AND x.new_cases> 1000;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))


    