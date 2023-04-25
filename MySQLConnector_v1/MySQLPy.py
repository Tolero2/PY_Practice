##Define the packages to use
#Package 1: password handler module.
from getpass import getpass
from os import error

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
##Perform INSERT DML statement operations.
##Perform two types of cursor execution operation (execute()/executemany()).

#INSERT DML using cursor.execute() method. // Use execute method when all values will be passed with the single query string.

# #Movies INSERT operation.
# insertMoviesQuery = """
# INSERT INTO movies
# (title, release_year, genre, collection_in_mil)
# VALUES
#     ("Forrest Gump", 1994, "Drama", 330.2),
#     ("3 Idiots", 2009, "Drama", 2.4),
#     ("Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5),
#     ("Good Will Hunting", 1997, "Drama", 138.1),
#     ("Skyfall", 2012, "Action", 304.6),
#     ("Gladiator", 2000, "Action", 188.7),
#     ("Black", 2005, "Drama", 3.0),
#     ("Titanic", 1997, "Romance", 659.2),
#     ("The Shawshank Redemption", 1994, "Drama",28.4),
#     ("Udaan", 2010, "Drama", 1.5),
#     ("Home Alone", 1990, "Comedy", 286.9),
#     ("Casablanca", 1942, "Romance", 1.0),
#     ("Avengers: Endgame", 2019, "Action", 858.8),
#     ("Night of the Living Dead", 1968, "Horror", 2.5),
#     ("The Godfather", 1972, "Crime", 135.6),
#     ("Haider", 2014, "Action", 4.2),
#     ("Inception", 2010, "Adventure", 293.7),
#     ("Evil", 2003, "Horror", 1.3),
#     ("Toy Story 4", 2019, "Animation", 434.9),
#     ("Air Force One", 1997, "Drama", 138.1),
#     ("The Dark Knight", 2008, "Action",535.4),
#     ("Bhaag Milkha Bhaag", 2013, "Sport", 4.1),
#     ("The Lion King", 1994, "Animation", 423.6),
#     ("Pulp Fiction", 1994, "Crime", 108.8),
#     ("Kai Po Che", 2013, "Sport", 6.0),
#     ("Beasts of No Nation", 2015, "War", 1.4),
#     ("Andadhun", 2018, "Thriller", 2.9),
#     ("The Silence of the Lambs", 1991, "Crime", 68.2),
#     ("Deadpool", 2016, "Action", 363.6),
#     ("Drishyam", 2015, "Mystery", 3.0)
# """

# #try to catch any errors for inserting into Movies table.
# try:

#     DBConn_Exec(insertMoviesQuery)
# except Error as err:
#      print("Insert error: {}".format(err.msg))
# else:
#      print("Successfully inserted data in Movies table")
# finally:
#    print("MySQL Sever connection closed!")

# #INSERT DML using cursor.executemany() method. // Use executemany() method when all values are stored separately as a list variable and will be passed as a tuple with query string. // notice you have to define the values placeholders in the insert queries.

# #define a function to use the cursor.executemany() method objectively. // the DBConn_Exec function only use the cursor.execute() method.
# def DBConn_ExecMany(query, recList) :
     with connect(**config) as connection:
            connection.database=DB_NAME
            with connection.cursor() as cursor:
                cursor.executemany(query, recList)
                connection.commit()


# #Reviewers INSERT operation.
# insertReviewersQuery = """
# INSERT INTO reviewers
# (first_name, last_name)
# VALUES ( %s, %s )
# """

# reviewersRecords = [
#     ("Chaitanya", "Baweja"),
#     ("Mary", "Cooper"),
#     ("John", "Wayne"),
#     ("Thomas", "Stoneman"),
#     ("Penny", "Hofstadter"),
#     ("Mitchell", "Marsh"),
#     ("Wyatt", "Skaggs"),
#     ("Andre", "Veiga"),
#     ("Sheldon", "Cooper"),
#     ("Kimbra", "Masters"),
#     ("Kat", "Dennings"),
#     ("Bruce", "Wayne"),
#     ("Domingo", "Cortes"),
#     ("Rajesh", "Koothrappali"),
#     ("Ben", "Glocker"),
#     ("Mahinder", "Dhoni"),
#     ("Akbar", "Khan"),
#     ("Howard", "Wolowitz"),
#     ("Pinkie", "Petit"),
#     ("Gurkaran", "Singh"),
#     ("Amy", "Farah Fowler"),
#     ("Marlon", "Crafford"),
# ]

# #try to catch any errors for inserting into Reviewers table.
# try:
#     DBConn_ExecMany(insertReviewersQuery,reviewersRecords)
# except Error as err:
#      print("Insert error: {}".format(err.msg))
# else:
#      print("Successfully inserted data in Reviewers table")
# finally:
#    print("MySQL Sever connection closed!")



# #Ratings INSERT operation.
# insertRatingsQuery = """
# INSERT INTO ratings
# (rating, movie_id, reviewer_id)
# VALUES ( %s, %s, %s)
# """
# ratingsRecords = [
#     (6.4, 17, 5), (5.6, 19, 1), (6.3, 22, 14), (5.1, 21, 17),
#     (5.0, 5, 5), (6.5, 21, 5), (8.5, 30, 13), (9.7, 6, 4),
#     (8.5, 24, 12), (9.9, 14, 9), (8.7, 26, 14), (9.9, 6, 10),
#     (5.1, 30, 6), (5.4, 18, 16), (6.2, 6, 20), (7.3, 21, 19),
#     (8.1, 17, 18), (5.0, 7, 2), (9.8, 23, 3), (8.0, 22, 9),
#     (8.5, 11, 13), (5.0, 5, 11), (5.7, 8, 2), (7.6, 25, 19),
#     (5.2, 18, 15), (9.7, 13, 3), (5.8, 18, 8), (5.8, 30, 15),
#     (8.4, 21, 18), (6.2, 23, 16), (7.0, 10, 18), (9.5, 30, 20),
#     (8.9, 3, 19), (6.4, 12, 2), (7.8, 12, 22), (9.9, 15, 13),
#     (7.5, 20, 17), (9.0, 25, 6), (8.5, 23, 2), (5.3, 30, 17),
#     (6.4, 5, 10), (8.1, 5, 21), (5.7, 22, 1), (6.3, 28, 4),
#     (9.8, 13, 1)
# ]


# #try to catch any errors for inserting into Ratings table.
# try:
#     DBConn_ExecMany(insertRatingsQuery,ratingsRecords)
# except Error as err:
#      print("Insert error: {}".format(err.msg))
# else:
#      print("Successfully inserted data in Reviewers table")

# finally:
#    print("MySQL Sever connection closed!")


#______________________________________________________________________________________________________________________________
##Perform SELECT DML statement operations.

# #SELECT ALL available columns in any given table with a limit of returned rows.
# print("You are viewing all columns under the specified table name and specific number of returned rows")
# tableName=input('Enter table name: ')
# rowLimit=input('Enter the number of rows to be return: ')
# selectAllQuery="SELECT * FROM {tableName} LIMIT {rowLimit}".format(tableName=tableName, rowLimit=rowLimit)

# try:
#     queryResult=DBConn_Exec(selectAllQuery)
#     # print(f"{queryResult}\n")
#     # for records in queryResult:
#     #      print(f"{records}\n")
# except Error as err:
#         print("Select error: {}".format(err.msg))

# else:
#     print("MySQL sever connection opened!")

#     #print the stored query results into a pandas 2x2 DataFrame with defined columns according to the specified table
#     import pandas as pd
#     from os import error
#     if (tableName.upper() == "MOVIES"):
#             df =pd.DataFrame(queryResult, columns=(  "title", "release_year", "genre", "collection_in_mil"))
#             print(df)
#     elif (tableName.upper() == "RATINGS"):
#             df =pd.DataFrame(queryResult, columns=("rating", "movie_id", "reviewer_id"))
#             print(df)
#     elif (tableName.upper() == "REVIEWERS"):
#             df =pd.DataFrame(queryResult, columns=( "id", "first_name", "last_name"))
#             print(df)


#SELECT specified columns from any specified table with a specified limit of returned rows.
print("You are viewing all specified columns under the specified table name and the specified number of rows returned.")
tableNameUser=input('Enter table name: ')
colNamesUser = input('Enter the column(s) to display( separate each value with (,)): ')
rowLimit=input('Enter the number of rows to be return: ')

#handling the comma(,) prone User input for column names(colNamesUser)
if (colNamesUser.endswith(",")):
        colNameSplit = colNamesUser.removesuffix(",")
else:
    colNameSplit =colNamesUser

selectColumnsQuery="""SELECT {columnsName} FROM `{tableName}` LIMIT {rowLimit}""".format(tableName=str(tableNameUser), columnsName=str(colNameSplit), rowLimit=int(rowLimit))
print (selectColumnsQuery)

#try catch operation on the execution of query.
try:
    queryResult=DBConn_Exec(selectColumnsQuery)
except Error as err:
        print("Select error: {}".format(err.msg))
        print (selectColumnsQuery)
else:
#if SQL query was executed successfully then print.
    print("MySQL sever connection opened!")

#print the stored query results into a pandas 2x2 DataFrame with specified columns header according to the user specified columns.
    import pandas as pd
    #handling the comma(,) prone User input for column names (colNamesUser).
    if (colNamesUser.endswith(",")):
        colNameSplit = colNamesUser.removesuffix(",")
        dfColList = [colNameSplit]
    else:
        dfColList =colNamesUser.split(",")

    df =pd.DataFrame(queryResult, columns=dfColList)
    print(df)
finally:
    print("MySQL Sever connection closed!")

##______________________________________________________________________________________________________________________________
##Perform UPDATE DML statement operations.

#safe parameter handling to prevent SQL injection from User input 

movie_id = input("Enter movie id: ")
reviewer_id = input("Enter reviewer id: ")
new_rating = input("Enter new rating: ")
update_query = """
UPDATE
    ratings
SET
    rating = %s
WHERE
    movie_id = %s AND reviewer_id = %s;

SELECT *
FROM ratings
WHERE
    movie_id = %s AND reviewer_id = %s
"""
val_tuple = (
    new_rating,
    movie_id,
    reviewer_id,
    movie_id,
    reviewer_id,
)

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="online_movie_rating",
    ) as connection:
        with connection.cursor() as cursor:
            for result in cursor.execute(update_query, val_tuple, multi=True):
                if result.with_rows:
                    print(result.fetchall())
            connection.commit()
except Error as e:
    print(e)

print("MySQL Sever connection closed!")