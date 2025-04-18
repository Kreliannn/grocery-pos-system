from backend.db.database import Database

class SoldProduct(Database):

    def addSoldProduct(self, item):
        sql = "INSERT INTO soldproduct (qty, product_id, transaction_id) VALUES (%s, %s, %s)"
        values = (item['qty'], item['product_id'], item['transaction_id'])
        self.insert(sql, values)
