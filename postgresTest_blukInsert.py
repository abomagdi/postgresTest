import psycopg2
def bulkInsert(records):
    try:
        connection = psycopg2.connect(user = "ahmed2",
                                  password = "metalgear87",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "auctionData")
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO mobile (id, model, price) 
                           VALUES (%s,%s,%s) """
        # executemany() to insert multiple rows rows
        result = cursor.executemany(sql_insert_query, records)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into mobile table")
    except (Exception, psycopg2.Error) as error:
        print("Failed inserting record into mobile table {}".format(error))
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
records_to_insert = [ (8,'LG', 800) , (9,'One Plus 6', 950)]
bulkInsert(records_to_insert)