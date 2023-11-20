from pymysql import *

connection = None

try:  # Try to connect and work with the specific database
    """
    Connecting to the database
    host -> Host to connect to
    user -> User to connect to the database with
    password -> Password of a user to connect the database with
    db -> Database we are working with
    cursorclass -> cursor to get records with
    """
    if connection is None:
        connection = connect(host='127.0.0.1', user='root', password=None, db='diceware_exercise',
                             cursorclass=cursors.DictCursor)
    query = "INSERT INTO accounts(user_number,user_name, password,entering_date) VALUES (%d,'%s','%s','%s')" % (
        356, 'Meni', '12345t', '11/12/1999')
    connection.cursor().execute(query)
    connection.commit()  # Saving the result
except MySQLError:  # If there was a problem while connecting/working with the database
    print("Database error")
else:  # If everything was okay, closing the opened connection
    connection.close()
