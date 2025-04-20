from backend.db.database import Database

class SoldProduct(Database):

    def addSoldProduct(self, item):
        sql = "INSERT INTO soldproduct (qty, product_id, transaction_id) VALUES (%s, %s, %s)"
        values = (item['qty'], item['product_id'], item['transaction_id'])
        self.insert(sql, values)

    def getSoldProducts(self, transaction_id):
        sql = "select * from soldproduct join products on soldProduct.product_id = products.product_id where transaction_id = %s"
        values = [transaction_id]
        return self.getAll(sql, values)
    
    def getSoldProductCount(self):
        sql = "select sum(qty) from soldproduct"
        values = []
        return self.getAll(sql, values)[0]