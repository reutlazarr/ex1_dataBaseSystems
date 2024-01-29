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
        SELECT AVG(new_tests)
        FROM covid_vaccination
        WHERE positive_rate > (
                   SELECT AVG(positive_rate)
                   FROM covid_vaccination
                   WHERE positive_rate <> ""
                   )
        AND new_tests <> ""
     """)
    print(', '.join(str(row) for row in cursor.fetchall()))


    