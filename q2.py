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
        # select date, new_cases and to different locations
        SELECT first.date, first.new_cases, first.location, second.location
        #  consider only the first 1000 rows from the table
        FROM (SELECT  * FROM covid_deaths LIMIT 1000) As first,
             (SELECT  * FROM covid_deaths LIMIT 1000) AS second
            # 2 different locations with the same amount of new cases in the same date
            WHERE first.new_cases = second.new_cases AND first.date = second.date
            AND first.location < second.location AND first.new_cases > 1000 
            # amount of new_cases is greater than 1000
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))


    
