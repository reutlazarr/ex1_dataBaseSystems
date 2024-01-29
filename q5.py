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
        SELECT cd.location, AVG(cd.new_cases) AS avg_new_cases
        FROM covid_deaths cd
        INNER JOIN (
            SELECT date, MAX(population) AS max_population
            FROM covid_deaths
            GROUP BY date
        ) max_pop ON cd.date = max_pop.date AND cd.population = max_pop.max_population
        GROUP BY cd.location
        HAVING AVG(cd.new_cases) > 3;
     """)
    print(', '.join(str(row) for row in cursor.fetchall()))

# highest population and AVG(new cases) >3
    
# Write a query to find the amount of new cases, in location that have in some
# time the highest population, and the average of new cases in this location are
# greater than 3.
