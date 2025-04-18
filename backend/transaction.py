from backend.db.database import Database

class Transaction(Database):

    def addProduct(self, transaction):
        sql = "INSERT INTO transactions (transaction_id, total, payment, customer_change, date) VALUES (%s, %s, %s, %s, %s)"
        values = (transaction['transaction_id'], transaction['total'], transaction['payment'], transaction['customer_change'], transaction['date'])
        self.insert(sql, values)
