import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5 import uic


class CoffeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.initUI()
        self.update_table()

    def initUI(self):
        uic.loadUi("main.ui", self)

    def update_table(self):
        res = self.cur.execute("""SELECT * FROM coffee""").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название", "Степень обжарки", "Молотый",
                                                    "Вкус", "Цена", "Объем упаковки"])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                item = QTableWidgetItem(str(elem))
                item.setFlags(Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, item)
        self.tableWidget.resizeColumnsToContents()


def excepthook(cls, value, traceback):
    sys.__excepthook__(cls, value, traceback)


if __name__ == "__main__":
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = CoffeeWindow()
    ex.show()
    sys.exit(app.exec())
