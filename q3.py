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
        SELECT AVG(new_tests) # calculate the average amount of new tests
        FROM covid_vaccination
        WHERE new_tests <> '' AND positive_rate <> '' # not empty
            # if positive rate  is higher than average
            AND positive_rate > (SELECT AVG(positive_rate) # calculate the average of positive rate
                                 FROM covid_vaccination
                                 # not empty
                                 WHERE new_tests <> '' AND positive_rate <> '')
     """)
    print(', '.join(str(row) for row in cursor.fetchall()))


    
