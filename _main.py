import sys
from PyQt5 import QtWidgets
import mysql.connector
from main import Ui_MainWindow
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox

class window(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_save.clicked.connect(self.save)

    def save(self):
        connection = mysql.connector.connect(
            host = "localhost",                             
            user = "root",                                  
            password = "159753",
            database = "app_bank"
            )
        my_cursor = connection.cursor() 
        name = self.ui.name_text_input.text()
        number_of_installments = self.ui.number_of_installments_text_input.text()
        price = self.ui.price_text_input.text()
        if self.ui.cb_bank.currentText() == "Enpara.com":
            sql ="Insert Into enpara_com (name, number_of_installments, price) Values (%s, %s, %s)" #values (%s, %s, %s)
            values = (name, number_of_installments, price)
        elif self.ui.cb_bank.currentText() == "Garanti BBVA":
            sql ="Insert Into garanti_bbva (name, number_of_installments, price) Values (%s, %s, %s)" #values (%s, %s, %s)
            values = (name, number_of_installments, price)
        elif self.ui.cb_bank.currentText() == "Özel":
            sql ="Insert Into special (name, price) Values (%s, %s)" #values (%s, %s, %s)
            values = (name, price)
        my_cursor.execute(sql, values)
        try:
            connection.commit()
        except mysql.connector.Error as err:
            print(f"hata :{err}")
        finally:
            connection.close()

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

app()