from pymysql import *


def insert_code(user_number, user_name, password, entering_date):
    """
       Function it enter user to sql table
       :param user_username: Username to enter
       :param user_name: username to enter
       :param password to enter
       :return:entering the user name to the table
       """
    connection = None

    try:

        if connection is None:
            connection = connect(host='127.0.0.1', user='root', password=None, db='exercise_diceware',
                                 cursorclass=cursors.DictCursor)
        query = "INSERT INTO accounts(user_number,user_name, password,entering_date) VALUES (%d,'%s','%s','%s')" % (
            user_number, user_name, password, entering_date)
        connection.cursor().execute(query)
        connection.commit()
    except MySQLError:
        print("Database error")
    else:
        connection.close()


