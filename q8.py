
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
        SELECT continent # select continent
        FROM covid_deaths 
        GROUP BY continent # group by continent
        # having average of new cases while it is greater than average of new cases of locations
        HAVING AVG(new_cases) > (SELECT AVG(cd1.new_cases)
                                    FROM covid_deaths cd1
                                    # the average population is lower than the global average population
                                    WHERE cd1.population < (SELECT AVG(population) # select the global average population
                                                            FROM covid_deaths))
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
# Write a query that returns the continents which average new cases is greater that
# the average of new cases of locations where the average population is lower
# than the global average population
    
