from getpass import getpass
from mysql.connector import connect, Error

config ={
    'host' : '127.0.0.1',
    'user': input('Enter Username: '),
    'password': getpass(),
}
DB_NAME = "online_movie_rating6"
try:
    with connect(
        **config
    ) as connection:
       createDBQuery= "CREATE DATABASE {}".format(DB_NAME)
       showDBQuery = "SHOW DATABASES"
       with connection.cursor() as cursor:
        #cursor.execute(createDBQuery)
        connection.database= DB_NAME
except Error as e:
        print("Error: {}. check input details".format(e.msg ))
else:
    print("Successfully connected to MySQL Sever!")  
finally:
    with connect(
        **config
    ) as connection:
       showDBQuery = "SHOW DATABASES"
       with connection.cursor() as cursor:
        cursor.execute(showDBQuery)
        for db in cursor:
             print(db)
print("Connection closed!")


#import mySQLConnectPy

