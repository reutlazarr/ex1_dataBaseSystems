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
     SELECT
        (SELECT SUM(new_cases)
        FROM covid_deaths
        WHERE date LIKE '%/02/%') -
        (SELECT SUM(new_cases)
        FROM covid_deaths
        WHERE date LIKE '%/03/%') AS difference;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))


    