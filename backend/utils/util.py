
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtCore

class utils:

    @staticmethod
    def scanBarCodeAndUpdateFrame(cap, camera, callBack):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)  

        if ret:
            barcodes = decode(frame)
            for barcode in barcodes:
                barcode_data = barcode.data.decode('utf-8')
                print(f"Detected barcode: {barcode_data}")
                callBack( str(barcode_data) )

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channels = frame.shape
            bytes_per_line = 3 * width
            q_img = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
            camera.setPixmap(QPixmap.fromImage(q_img))

    @staticmethod
    def alertError(message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec()
    
    @staticmethod
    def alertSuccess(message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Success")
        msg.setInformativeText(message)
        msg.setWindowTitle("Success")
        msg.exec()
    
    @staticmethod
    def delayCameraLoad(callback, timer, MainWindow):
        delay = QtCore.QTimer(MainWindow)
        delay.setInterval(timer)  
        delay.timeout.connect(lambda: callback(MainWindow))
        delay.setSingleShot(True) 
        delay.start()  

 



