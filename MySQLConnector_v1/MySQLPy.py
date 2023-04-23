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

    TABLES = {}

    TABLES['movies']= ("""
    CREATE TABLE `movies`(
    `id` INT NOT NULL AUTO_INCREMENT,
    `title` NVARCHAR(50) NULL,
    `release_year` DATE NULL,
    `genre` NVARCHAR(50) NULL,
    `collection_in_mil` float NULL,
    PRIMARY KEY (`id`))""")

    TABLES['reviewers'] = ("""
    CREATE TABLE reviewers (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(100),
    `last_name` VARCHAR(100)
)
""")
    TABLES['ratings'] = ("""
    CREATE TABLE ratings (
    movie_id INT,
    reviewer_id INT,
    rating DECIMAL(2,1),
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
    PRIMARY KEY(movie_id, reviewer_id)
    """)
    try:
       with connect(
        **config
    ) as connection:
          createTableQuery= "{}".format("".join(TABLES['movies']))
          with connection.cursor() as cursor:
            connection.database= DB_NAME
            cursor.execute(createTableQuery)
    except Error as e:
        print("Error: {}. check input details".format(e.msg ))
    else:
        print("Successfully connected to MySQL Sever!")  
print("Connection closed!")


#import mySQLConnectPy

