from backend.db.database import Database

class Product(Database):

    def addProduct(self, product):
        sql = "INSERT INTO products (name, barcode, price ,image, stocks ) VALUES (%s, %s, %s, %s, %s)"
        values = (product['name'], product['barcode'], product['price'], product['image'], product['stocks'])
        self.insert(sql, values)

    def getProducts(self):
        sql = "SELECT * FROM products"
        return self.getAll(sql)
    
    def getProduct(self, id):
        sql = "SELECT * FROM products where product_id = %s"
        return self.getOne(sql, id)
    
    def getProductByBarCode(self, barcode):
        sql = "SELECT name, category, price FROM products where barcode = %s"
        return self.getOne(sql, barcode)


        
       
        