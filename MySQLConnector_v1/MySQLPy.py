##Define the packages to use
#Package 1: password handler module.
from getpass import getpass

#Package 2: MysQL db connector module that implement py DB-API 249.
from mysql.connector import connect, Error

#______________________________________________________________________________________________________________________
##Define the variables for the database implementation.

#config variable holding dict value of the connection strings for connecting to the MySQL DB server// takes Username input and password input through the 'getpass' method.
config ={
    'host' : '127.0.0.1',
    'user': input('Enter Username: '),
    'password': getpass('Enter password: '),
}

#Database name to use or create on if not existing.
DB_NAME = "online_movie_rating15"

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
describeQuery = "DESCRIBE "


##----------------------------------------------------------------------------------------------------------------------------------
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
#USE DB statement.
def UseDB ():
     with connect(
        **config
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(useDBQuery)
#   #______________________________________________________________________________________________________________________________
# ##Perform the USE DB and CREATE DB SQL statements to set/create database (DB_NAME). // Finally statement  include the CREATE tables DDL statement after database (DB_NAME) has been set/created.
# try:
#     #USE DB query.
#         UseDB()
#         with connect(
#         **config
#         ) as connection:
#             with connection.cursor() as cursor:
#                 cursor.execute(useDBQuery)
# except Error as e:
#         print("Database Error: {}.\nCreating {} database Now!".format(e.msg, DB_NAME))
#     #Create DB DDL query.
#         with connect(
#         **config
#         ) as connection:
#             print("Successfully connected to MySQL sever!")
#             with connection.cursor() as cursor:
#                 cursor.execute(createDBQuery)
#                 print("Database created")
# else:
#     print("Successfully connected to MySQL sever and {} database!".format(DB_NAME))
# finally:
#     try:
#     #Show the available database and create a loop for each table.

#         #Show DB query.
#             cursorResults = DBConn_Exec(showDBQuery)
#             for cursorShowDB in cursorResults:
#                 print(cursorShowDB)

#         #Create tables DDL query.
#             for table in TABLES:
#                 print("Creating {} table".format(table))
#                 # tableAtt= TABLES[f'{table}']
#                 createTableQuery= TABLES[f'{table}']
#                 describeTableQuery = (f"{describeQuery} {table}")
#                 DBConn_Exec(createTableQuery)
#                 describeResult= DBConn_Exec(describeTableQuery)
#                 print(f"Describe {table}:\n{describeResult}")

#     except Error as e:
#         print("Error on Table: {}.\nCheck table DDL details".format(e.msg))
#     else:
#         print("Successfully created tables ")

#     finally:
#         print("MySQL Sever connection closed!")


#______________________________________________________________________________________________________________________________
##Perform ALTER DDL statement

#ALTER table variables from user input.
alterTableQuery="ALTER TABLE"
tableName = input('Enter table name to Alter: ')
add_modify = input('Enter the alter operation to perform (ADD or MODIFY):  ')
newColumn = input('Enter COLUMN name and logic: ')

try:

        #USE DB query.
        UseDB()
    #ALTER table DDL query
        if( add_modify.upper() == 'MODIFY'):
            print("MODIFY works")
        #MODIFY COLUMN query.
            modifyColumnQuery= (f"{alterTableQuery} {tableName} MODIFY COLUMN {newColumn} ")
        elif(add_modify.upper() == 'ADD'):
            print("ADD works")
        #ADD COLUMN query.
            addColumnQuery= (f"{alterTableQuery} {tableName} ADD COLUMN {newColumn} ")
        else:
            print('Please specify between the ADD or MODIFY operation')

except Error as err:
      print("Alter Table Error: {}".format(err.msg))
finally:
    print("MySQL Sever connection closed!")


print("MySQL Sever connection closed!")