import pymysql

def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',           
        password='@Anup.03',           
        database='nepal_travel_db',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection