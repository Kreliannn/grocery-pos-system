from backend.db.database import Database
from datetime import date

class Transaction(Database):

    def addTransaction(self, transaction):
        sql = "INSERT INTO transactions (transaction_id, total, payment, customer_change, date) VALUES (%s, %s, %s, %s, %s)"
        values = (transaction['transaction_id'], transaction['total'], transaction['payment'], transaction['customer_change'], transaction['date'])
        self.insert(sql, values)

    def getTransaction(self, transaction_id):
        sql = "select * from transactions where transaction_id = %s"
        return self.getOne(sql, transaction_id)
    
    def getTransactions(self):
        sql = "select * from transactions"
        return self.getAll(sql)
    
    def getTotalSales(self):
        sql = "select sum(total) from transactions"
        values = []
        return self.getAll(sql, values)[0]
    
    def getTodaySales(self):
        sql = "select sum(total) from transactions where date = %s"
        values = [date.today()]
        return self.getAll(sql, values)[0]