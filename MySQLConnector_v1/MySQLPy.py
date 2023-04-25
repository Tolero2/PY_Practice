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

#List of schema tables and CREATE DDL statement for each schema table stored as a key=>value pair of a dictionary variable (TABLES).
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
# ##Perform the USE DB and CREATE DB SQL statements operation to set/create database (DB_NAME). // Finally statement  include the CREATE tables DDL statement operation after database (DB_NAME) has been set/created.
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


# #______________________________________________________________________________________________________________________________
# ##Perform ALTER DDL statement operation.

# #ALTER table variables from user input.
# alterTableQuery="ALTER TABLE"
# tableName = input('Enter table name to Alter: ')
# add_modify = input('Enter the alter operation to perform (ADD or MODIFY):  ')
# newColumn = input('Enter COLUMN name and logic: ')

# try:

#         #USE DB query.
#         UseDB()
#     #extendable ALTER table DDL queries.
#         if( add_modify.upper() == 'MODIFY'):
#         #MODIFY COLUMN query.
#             modifyColumnQuery= (f"{alterTableQuery} {tableName} MODIFY COLUMN {newColumn} ")
#             DBConn_Exec(modifyColumnQuery)
#             print("Successfully modified selected column on {} table".format(tableName))
#         elif(add_modify.upper() == 'ADD'):
#         #ADD COLUMN query.
#             addColumnQuery= (f"{alterTableQuery} {tableName} ADD COLUMN {newColumn} ")
#             DBConn_Exec(addColumnQuery)
#             print("Successfully added new column to {} table".format(tableName))
#         else:
#             print('Please specify between the ADD or MODIFY operation')

# except Error as err:
#       print("Alter Table Error: {}".format(err.msg))
# finally:
#     print("MySQL Sever connection closed!")

# #______________________________________________________________________________________________________________________________
# ##Perform DROP/TRUNCATE statement operation.

# #DROP table variables from user input.
# dropQuery="DROP TABLE"
# truncateQuery = "TRUNCATE TABLE" #Unused.
# tableName = input('Enter table name to DELETE: ')

##try to catch any errors.
# try:

#         #USE DB query.
#             UseDB()
#     #extendable DELETE table DDL queries.
#         #DROP COLUMN query.
#             dropTableQuery= (f"{dropQuery} {tableName}")
#             DBConn_Exec(dropTableQuery)
#             print("Successfully deleted {} table".format(tableName))
# except Error as err:
#       print("Delete Table Error: {}".format(err.msg))
# finally:
#     print("MySQL Sever connection closed!")

#______________________________________________________________________________________________________________________________
##Perform INSERT DML statement operation.
##Perform two cursor execution class (execute/executemany).

#INSERT DML using cursor.execute() method. // Use execute method when all values will be passed with the single query string.
insertMoviesQuery = """
INSERT INTO movies
(title, release_year, genre, collection_in_mil)
VALUES
    ("Forrest Gump", 1994, "Drama", 330.2),
    ("3 Idiots", 2009, "Drama", 2.4),
    ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
    ("Good Will Hunting", 1997, "Drama", 138.1),
    ("Skyfall", 2012, "Action", 304.6),
    ("Gladiator", 2000, "Action", 188.7),
    ("Black", 2005, "Drama", 3.0),
    ("Titanic", 1997, "Romance", 659.2),
    ("The Shawshank Redemption", 1994, "Drama",28.4),
    ("Udaan", 2010, "Drama", 1.5),
    ("Home Alone", 1990, "Comedy", 286.9),
    ("Casablanca", 1942, "Romance", 1.0),
    ("Avengers: Endgame", 2019, "Action", 858.8),
    ("Night of the Living Dead", 1968, "Horror", 2.5),
    ("The Godfather", 1972, "Crime", 135.6),
    ("Haider", 2014, "Action", 4.2),
    ("Inception", 2010, "Adventure", 293.7),
    ("Evil", 2003, "Horror", 1.3),
    ("Toy Story 4", 2019, "Animation", 434.9),
    ("Air Force One", 1997, "Drama", 138.1),
    ("The Dark Knight", 2008, "Action",535.4),
    ("Bhaag Milkha Bhaag", 2013, "Sport", 4.1),
    ("The Lion King", 1994, "Animation", 423.6),
    ("Pulp Fiction", 1994, "Crime", 108.8),
    ("Kai Po Che", 2013, "Sport", 6.0),
    ("Beasts of No Nation", 2015, "War", 1.4),
    ("Andadhun", 2018, "Thriller", 2.9),
    ("The Silence of the Lambs", 1991, "Crime", 68.2),
    ("Deadpool", 2016, "Action", 363.6),
    ("Drishyam", 2015, "Mystery", 3.0)
"""

#try to catch any errors.
try:

    DBConn_Exec(insertMoviesQuery)
except Error as err:
     print("Insert error: {}".format(err.msg))
else:
     print("Successfully inserted data in Movies table")

finally:
   print("MySQL Sever connection closed!")

#INSERT DML using cursor.executemany() method. // Use executemany method when all values are stored separately as a list variable and will be passed as a tuple with query string. // notice you have to define the values pointer in your insert query.
insertReviewersQuery = """
INSERT INTO reviewers
(first_name, last_name)
VALUES ( %s, %s )
"""

reviewersRecords = [
    ("Chaitanya", "Baweja"),
    ("Mary", "Cooper"),
    ("John", "Wayne"),
    ("Thomas", "Stoneman"),
    ("Penny", "Hofstadter"),
    ("Mitchell", "Marsh"),
    ("Wyatt", "Skaggs"),
    ("Andre", "Veiga"),
    ("Sheldon", "Cooper"),
    ("Kimbra", "Masters"),
    ("Kat", "Dennings"),
    ("Bruce", "Wayne"),
    ("Domingo", "Cortes"),
    ("Rajesh", "Koothrappali"),
    ("Ben", "Glocker"),
    ("Mahinder", "Dhoni"),
    ("Akbar", "Khan"),
    ("Howard", "Wolowitz"),
    ("Pinkie", "Petit"),
    ("Gurkaran", "Singh"),
    ("Amy", "Farah Fowler"),
    ("Marlon", "Crafford"),
]

#try to catch any errors.
try:
#open new connection here to allow the use of the cursor.executemany() method. the DBConn_Exec function only use the cursor.execute() method.
    with connect(**config) as connection:
            connection.database=DB_NAME
            with connection.cursor() as cursor:
                cursor.executemany(insertReviewersQuery,reviewersRecords)
                connection.commit()
except Error as err:
     print("Insert error: {}".format(err.msg))
else:
     print("Successfully inserted data in Reviewers table")

finally:
   print("MySQL Sever connection closed!")


print("MySQL Sever connection closed!")