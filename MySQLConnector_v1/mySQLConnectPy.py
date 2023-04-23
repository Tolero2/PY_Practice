from getpass import getpass
from mysql.connector import connect, Error

config ={
    'host' : '127.0.0.1',
    'user': input('Enter Username: '),
    'password': getpass(),
}
try:
    with connect(
        **config
    ) as connection:
       cursor = connection.cursor()
except Error as e:
    print("Cannot connect to DBserver: {}. check input details.".format(e.msg))
else:
    print("Successfully connected to MySQL Sever!")

print("connection closed!")