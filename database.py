import mysql.connector
from mysql.connector import Error

def getCustomerDetails(id):
    try:
        mySQLConnection = mysql.connector.connect(host='localhost',
                                                  database='sample',
                                                  user='root',
                                                  password='root')

        cursor = mySQLConnection.cursor(buffered=True)
        sql_select_query = """select * from loans  where  Loan_ID = %s"""
        cursor.execute(sql_select_query, (id,))
        record = cursor.fetchall()
        #print(record)
        lst = []
        for row in record:
            for i in range(len(row)):
                # print(row[i])
                lst.append(row[i])

        return lst

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if (mySQLConnection.is_connected()):
            cursor.close()
            mySQLConnection.close()


getCustomerDetails(1)
