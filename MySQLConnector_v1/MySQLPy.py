from getpass import getpass
from mysql.connector import connect, Error

config ={
    'host' : '127.0.0.1',
    'user': input('Enter Username: '),
    'password': getpass('Enter password: '),
}
DB_NAME = "online_movie_rating10"

TABLES = {}

TABLES['movies']= ("""
    CREATE TABLE movies(
    `id` INT NOT NULL AUTO_INCREMENT,
    `title` NVARCHAR(50) NULL,
    `release_year` DATE NULL,
    `genre` NVARCHAR(50) NULL,
    `collection_in_mil` DECIMAL(4,2) NULL,
    PRIMARY KEY (`id`)
    )
    """)

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
    )
    """)

  ## Define a DBConn_Exec function Automatic open/close DB connection and execute (MySQL QUERY) passed as a parameter and return the fetch all as the results if any.


def DBConn_Exec (query):
        with connect(
        **config
        ) as connection:
            connection.database= DB_NAME
            with connection.cursor() as cursor:
                cursor.execute(query)
                curResults = cursor.fetchall()
                connection.commit()
                return curResults
##Database Queries to excute using the DBConn_Exec function.

useDBQuery= "USE {}".format(DB_NAME)
createDBQuery= "CREATE DATABASE {}".format(DB_NAME)
try:

        useDBQuery= "USE {}".format(DB_NAME)
        with connect(
        **config
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(useDBQuery)
except Error as e:
        print("Database Error: {}.\nCreating {} database Now!".format(e.msg, DB_NAME))
        createDBQuery= "CREATE DATABASE {}".format(DB_NAME)
        with connect(
        **config
        ) as connection:
            print("Successfully connected to MySQL sever!")
            with connection.cursor() as cursor:
                cursor.execute(createDBQuery)
                print("Database created")
            #   cursorConn = conn.cursor()
            #   cursorConn
else:
    print("Successfully connected to MySQL sever and database!")

finally:


    try:
          #create a loop for the insert tables, put the connection into a function; returning cursor/ or csrExc
        showDBQuery = "SHOW DATABASES"
        cursorResults = DBConn_Exec(showDBQuery)
        # for cursorShowDB in cursorResults:
        #      for db in cursorShowDB:
        #         print(db)
        for cursorShowDB in cursorResults:
             #for db in cursorShowDB:
                print(cursorShowDB)

        #cursor.execute(createTableQuery)
        for table in TABLES:
            print("Creating {} table".format(table))
            createTableQuery= "{}".format(TABLES[f'{table}'])
            cursorTable = DBConn_Exec(createTableQuery)


        #with connection.cursor() as cursor:
            #connection.database= DB_NAME
        #cursor.execute(createTableQuery)
    except Error as e:
        print("Error 2: {}. check input details".format(e ))
    else:
        print("Successfully created table ")
print("Sever connection closed!")


#import mySQLConnectPy

