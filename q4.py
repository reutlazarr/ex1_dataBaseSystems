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
        SELECT date, Sum(new_vaccinations) as daily_vaccinations
        FROM covid_vaccination
        WHERE continent = 'Asia'
        GROUP BY date
        HAVING Sum(new_vaccinations) > 20000000
     """)
    print(', '.join(str(row) for row in cursor.fetchall()))


#Write a query to find the days, where overall, there were more new vaccinations
#than 20000000 in the continent Asia. The answer should contain both the date
#and the total amount of new vaccinations as “daily_vaccinations”