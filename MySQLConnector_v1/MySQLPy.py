##Define the packages to use
#Package 1: password handler module.
from getpass import getpass
#Package 2: MysQL db connector module that implement py DB-API 249.
from mysql.connector import connect, Error


##Define the variables for the database implementation.

#config variable holding dict value of the connection strings for connecting to the MySQL DB server// takes Username input and password input through the 'getpass' method.
config ={
    'host' : '127.0.0.1',
    'user': input('Enter Username: '),
    'password': getpass('Enter password: '),
}

#Database name to use or create on if not existing.
DB_NAME = "online_movie_rating13"

#List of schema tables and 'Create' DDL statement for each schema table stored as a key=>value pair of a dictionary variable (TABLES).
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

##Database Queries to excute using the DBConn_Exec function.
useDBQuery= "USE {}".format(DB_NAME)
createDBQuery= "CREATE DATABASE {}".format(DB_NAME)
showDBQuery = "SHOW DATABASES"
createTableQuery = ""

#----------------------------------------------------------------------------------------------------------------------------------
##Define a DBConn_Exec function Automatic open/commit/close DB connection and use the connection cursor to execute (MySQL QUERY) passed as a parameter // returns the cursor fetch all method as the results if any.
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


##Perform the USE DB and CREATE DB SQL statementS to set/create database (DB_NAME).
try:
    #use DB DML query
        with connect(
        **config
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(useDBQuery)
except Error as e:
        print("Database Error: {}.\nCreating {} database Now!".format(e.msg, DB_NAME))
    #Create DB DDL query.
        with connect(
        **config
        ) as connection:
            print("Successfully connected to MySQL sever!")
            with connection.cursor() as cursor:
                cursor.execute(createDBQuery)
                print("Database created")
else:
    print("Successfully connected to MySQL sever and {} database!".format(DB_NAME))
finally:

##Perform the create table DDL statement after database (DB_NAME) has been set/created.
    try:
        #Show the available database and create a loop for each table.

        #Show DB query.
            cursorResults = DBConn_Exec(showDBQuery)
            for cursorShowDB in cursorResults:
                print(cursorShowDB)

        #Create tables DDL query.
            for table in TABLES:
                print("Creating {} table".format(table))
                tableAtt= TABLES[f'{table}']
                createTableQuery= "{}".format(tableAtt)
                cursorTable = DBConn_Exec(createTableQuery)
    except Error as e:
        print("Error on Table: {}.\nCheck table DDL details".format(e.msg))
    else:
        print("Successfully created tables ")

    # finally:
    #      try:
    #           error_reply
print("Sever connection closed!")

