# translator for mySQL & python. scoring data is in the database
import mysql.connector 
# imports my mySQL credentials from my private/safe config file
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

#defining function to be reused whenever i need to pull my mySQL credentials
def get_db():
    #actually makes the connection to the mySQL database. dialing phone number analogy
    return mysql.connector.connect(
        host = DB_HOST,
        user = DB_USER,
        password = DB_PASSWORD,
        database = DB_NAME
    )
# 