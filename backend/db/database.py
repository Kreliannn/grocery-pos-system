import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            port=3307,
            user="root",
            database="grocery_pos_system",
            password=""
        )

    def insert(self, sql, values):
        try:       
            cursor = self.conn.cursor(prepared=True)  
            cursor.execute(sql, values)
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")   
        finally:
            cursor.close()

    def update(self, sql, values):
        try:       
            cursor = self.conn.cursor(prepared=True)  
            cursor.execute(sql, values)
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")   
        finally:
            cursor.close()
   
    def getAll(self, sql, values = ()):
        try:   
            cursor = self.conn.cursor(prepared=True, dictionary=True)      
            cursor.execute(sql, values)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")   
   
    
    def getOne(self, sql, id):
        try:       
            cursor = self.conn.cursor(prepared=True, dictionary=True)  
            cursor.execute(sql, [id])
            result = cursor.fetchone()
            return result
        except mysql.connector.Error as err:
            print(f"Error: {err}")   
        finally:
            cursor.close()
        


