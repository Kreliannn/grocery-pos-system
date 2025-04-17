import mysql.connector

class database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            port=3307,
            user="root",
            database="example",
            password=""
        )

    def insert(self, sql, values):
        cursor = self.conn.cursor(prepared=True)  
        cursor.execute(sql, values)
        self.conn.commit()
        cursor.close()
   
    def getAll(self, sql, values = ()):
        cursor = self.conn.cursor(prepared=True, dictionary=True)  
        cursor.execute(sql, values)
        result = cursor.fetchall()
        return result
    
    def getOne(self, sql, id):
        cursor = self.conn.cursor(prepared=True, dictionary=True)  
        cursor.execute(sql, id)
        result = cursor.fetchall()
        return result


