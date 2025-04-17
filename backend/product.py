from db.database import database

class Product(database):

    def addProduct(self, product):
        sql = "INSERT INTO products (name, barcode, category ,image, stocks ) VALUES (%s, %s, %s, %s, %s)"
        values = (product['name'], product['barcode'], product['category'], product['image'], product['stocks'])
        self.insert(sql, values)

    def getProducts(self):
        sql = "SELECT * FROM products"
        return self.getAll(sql)
    
    def getProduct(self, id):
        sql = "SELECT * FROM products where product_id = %s"
        return self.getOne(sql, id)

        
       
        