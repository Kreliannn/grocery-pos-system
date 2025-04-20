from datetime import datetime
from backend.db.database import Database

class Notification(Database):

    def addNotifications(self, notification):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = "INSERT INTO notifications (header, message, icon, datetime) VALUES (%s, %s, %s, %s)"
        values = (notification['header'], notification['message'], notification['icon'], current_datetime)
        self.insert(sql, values)
    
    def getNotifications(self):
        sql = "select * from notifications"
        return list(reversed(self.getAll(sql)))