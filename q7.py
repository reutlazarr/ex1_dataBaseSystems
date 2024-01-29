# Write a query such that For each location in covid_deaths, will find:
# a. The monthly average of new cases(called “avg”)
# b. The max monthly amount of new cases(called “max_monthly”)
# c. The min monthly amount of new cases(called “min_monthly”)
# The result should present the location, and all 3 amount

# SELECT location, 
# we need to take each month and do an averge
# take all the days in month and make average. and make averge to this


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
    SELECT location, AVG(monthly_avg) AS avg_monthly_average
    FROM (
        SELECT location, MONTH(date) AS month, AVG(new_cases) AS monthly_avg
        FROM covid_deaths
        GROUP BY location, MONTH(date)
    ) AS monthly_averages
    GROUP BY location;
     """) 
    print(', '.join(str(row) for row in cursor.fetchall()))

