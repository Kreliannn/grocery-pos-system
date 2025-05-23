from backend.db.database import Database

class Product(Database):

    def addProduct(self, product):
        sql = "INSERT INTO products (name, barcode, price ,image, stocks ) VALUES (%s, %s, %s, %s, %s)"
        values = (product['name'], product['barcode'], product['price'], product['image'], product['stocks'])
        self.insert(sql, values)
        

    def updateProduct(self, product):
        sql = "update products set name = %s, price = %s, stocks = %s where product_id = %s"
        values = (product['name'], product['price'], product['stocks'], product['product_id'])
        self.update(sql, values)
    
    def deleteProduct(self, id):
        sql = "delete from products where product_id = %s"
        return self.update(sql, [id])
    
    def getProducts(self):
        sql = "SELECT * FROM products"
        return self.getAll(sql)
    
    def getProduct(self, id):
        sql = "SELECT * FROM products where product_id = %s"
        return self.getOne(sql, id)
    
    def getProductByBarCode(self, barcode):
        sql = "SELECT name, price, stocks, product_id FROM products where barcode = %s"
        return self.getOne(sql, barcode)
    
    def deductStocks(self, id, qty):
        product = self.getProduct(id)
        newQty = product['stocks'] - qty
        sql = "update products set  stocks = %s where product_id = %s"
        values = (newQty, id)
        self.update(sql, values)
        return newQty == 0


    
    


        
       
        