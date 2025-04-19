from backend.db.database import Database

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