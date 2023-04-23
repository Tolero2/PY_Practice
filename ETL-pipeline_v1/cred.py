from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode


##create a dict variable to hold YOUR DB connection string
config = {
  'user': 'root',
  'password': 'root1234',
  'host': '127.0.0.1',
  #'raise_on_warnings': True #FOR DEVELOPER'S USE ONLY
}


##MYSQL connector CONSTRUCTOR (connect()) to initiate the sever connection and database connection as well
## Two ways to use the dictionary parameters in config
#1 using the wildcard pointer for dictionary variable -**-config-
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
#2 using the dictionary variable directly as arguments in k=>value pair
#cnx = mysql.connector.connect(host = config["host"] ,user = config["user"] ,passwd = config["password"] )
#cursor = cnx.cursor()


##Define DB name to use or create if it does not exist
DB_NAME = 'Sample36'

## Dict variable to store the list of DB tables and its attributes
TABLES = {}

    #Table name and the DDL query as value - to create its table attribute stored as KEY=>VALUE pair
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int NOT NULL,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

TABLES['departments'] = (
    "CREATE TABLE `departments` (`dept_no` char(4) NOT NULL,`dept_name` varchar(40) NOT NULL,PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)) ENGINE=InnoDB")

TABLES['salaries'] = (
    "CREATE TABLE `salaries` ("
    "  `emp_no` int NOT NULL,"
    "  `salary` int NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
    "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['dept_emp'] = (
    "CREATE TABLE `dept_emp` ("
    "  `emp_no` int NOT NULL,"
    "  `dept_no` char(4) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
    "  KEY `dept_no` (`dept_no`),"
    "  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
    "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['dept_manager'] = (
    "  CREATE TABLE `dept_manager` ("
    "  `emp_no` int NOT NULL,"
    "  `dept_no` char(4) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`dept_no`),"
    "  KEY `emp_no` (`emp_no`),"
    "  KEY `dept_no` (`dept_no`),"
    "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
    "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['titles'] = (
    "CREATE TABLE `titles` ("
    "  `emp_no` int NOT NULL,"
    "  `title` varchar(50) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date DEFAULT NULL,"
    "  PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
    "  CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

##create a dict variable to hold YOUR DB connection string
config = {
  'user': 'root',
  'password': 'root1234',
  'host': '127.0.0.1',
  #'raise_on_warnings': True #FOR DEVELOPER'S USE ONLY
}


##MYSQL connector CONSTRUCTOR (connect()) to initiate the sever connection and database connection as well
## Two ways to use the dictionary parameters in config
#1 using the wildcard pointer for dictionary variable -**-config-
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
#2 using the dictionary variable directly as arguments in k=>value pair
#cnx = mysql.connector.connect(host = config["host"] ,user = config["user"] ,passwd = config["password"] )
#cursor = cnx.cursor()

##Function to create DB if the value of DB_NAME does not exist.
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

##Function to init the use Db with DB_NAME on the MYSQL server connection.
def use_DBNAME ():
    #try-catch and initiate the SQL sever to USE the DB_NAME or create a new DB using the create_database function if not DB_NAME does not exist
    try:
        cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exist.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Creating {} database...".format(DB_NAME))
            create_database(cursor)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)

##Function to create Tables in the DB_NAME using the dict variable of TABLES.
def create_tables(TABLES):
    #use the specified DBNAME or create a DB using the DBNAME if it doesn't exist.
    use_DBNAME ()
    ##Iterator of the Dict variable previously created as (TABLES :dict type)
    #loop through dict list from table name to read each object
    for table_name in TABLES:
        table_attributes = TABLES[table_name]

    #use try-catch funct to log the execute process as successful or failed.
        try:
            print("Creating {} table...".format(table_name.upper()))
            #execute the query from each object in the dict using the Mysql.connector.connect.cursor()
            cursor.execute (table_attributes)
        except mysql.connector.Error as e:
            if (e.errno == errorcode.ER_TABLE_EXISTS_ERROR):
                print("{} table already exists.".format(table_name.upper()))
            else:
                #FOR DEVELOPER'S USE ONLY
                print("Cannot create {t_name} table: {t_err}".format(t_err = e.msg, t_name=table_name.upper()))
                exit(1)
        else:
            print("{} table has been created successfully.".format(table_name.upper()))

#inItiate create_table function to start script process.
create_tables(TABLES)

#Close the DB connection after use to save runtime consumption
cursor.close()
cnx.close()