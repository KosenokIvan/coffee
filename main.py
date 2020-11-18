import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import uic


class CoffeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.update_table()

    def initUI(self):
        uic.loadUi("main.ui", self)

    def update_table(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("coffee.sqlite")
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable("coffee")
        model.select()
        self.tableView.setModel(model)


def excepthook(cls, value, traceback):
    sys.__excepthook__(cls, value, traceback)


if __name__ == "__main__":
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = CoffeeWindow()
    ex.show()
    sys.exit(app.exec())
