import psycopg2
try:
   connection = psycopg2.connect(user = "ahmed2",
                                  password = "metalgear87",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "auctionData")
   cursor = connection.cursor()
   postgres_insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
   record_to_insert = (7, 'LG', 800)
   cursor.execute(postgres_insert_query, record_to_insert)
   connection.commit()
   count = cursor.rowcount
   print (count, "Record inserted successfully into mobile table")
except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")