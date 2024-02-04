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
    cursor.execute("""
        # select the sum of new cases
        SELECT SUM(new_cases) AS total_new_cases
        FROM covid_deaths
        # location that have in some time the highest population
        WHERE location IN (SELECT location
                            FROM covid_deaths
                            WHERE population = (SELECT MAX(population)
                                                FROM covid_deaths))
        GROUP BY location  # groups the results by location
        HAVING AVG(new_cases) > 3
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
    
# Write a query to find the amount of new cases, in location that have in some
# time the highest population, and the average of new cases in this location are
# greater than 3.
