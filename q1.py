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
        (SELECT Sum(new_cases) # total cases is the sum of new cases
        FROM covid_deaths
        WHERE MONTH(date) = 2) -   # subtraction of total cases in February to total cases in  March
        (SELECT Sum(new_cases) # total cases is the sum of new cases
        FROM covid_deaths
        WHERE MONTH(date) = 3)
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))


    
