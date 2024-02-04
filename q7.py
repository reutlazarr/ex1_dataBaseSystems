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
    # select location,  monthly average, max monthly amount and min monthly amount of new cases
        SELECT location, AVG(sum_new_cases) AS avg, MAX(sum_new_cases) AS max_monthly, MIN(sum_new_cases) AS min_monthly
        FROM (SELECT location, SUM(new_cases) AS sum_new_cases # select the sum of new cases per location and month
                FROM covid_deaths
                GROUP BY location, MONTH(date)) AS monthly_stats_per_location # group by location and monthly
        GROUP BY location # group by location
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))

