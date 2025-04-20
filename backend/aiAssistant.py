import google.generativeai as genai 
from backend.db.database import Database
from datetime import datetime
from backend.product import Product
from backend.transaction import Transaction
from backend.soldProduct import SoldProduct

genai.configure(api_key="AIzaSyBdrJMVA-cG86Dj3dJIskhB0DsCbo7CwFk")
model = genai.GenerativeModel("gemini-1.5-flash")
myTransaction = Transaction()
myProduct = Product()
mySoldProduct = SoldProduct()

class Ai(Database):

    def generateAnswer(self, prompt):
        command = "act as ai assisatnt for my grocery store pos system.answer this promt based on the data in my database. if the promt is not realated to my system respond 'Sorry i can only respond to prompt specifically related to this system. when mentioning data dont mention data id'"
        systemData = self.getsystemData()
        finalPrompt = command + "prompt: " + prompt + systemData 
        response = model.generate_content(finalPrompt)  
        return response.text 
    
    def getConvoMessages(self):
        sql = "select * from messages"
        val = ()
        return self.getAll(sql, val)
    
    def addMessage(self, message):
        sql = "INSERT INTO messages (sender, message, datetime) VALUES (%s, %s, %s)"
        values = ( message['sender'], message['message'], message['datetime'])
        self.insert(sql, values)

    def getsystemData(self):
        productData = myProduct.getProducts()
        transactionData = myTransaction.getTransactions()
        soldProductData = mySoldProduct.getSoldProducts()
        combinedData = str(productData) + str(transactionData) + str(soldProductData)
        return "system data: " + combinedData

