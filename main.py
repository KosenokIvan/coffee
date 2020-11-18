import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5 import uic
from main_window import Ui_MainWindow
from addEditCoffeeForm import Ui_MainWindow as CoffeeForm


class CoffeeWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect("data/coffee.sqlite")
        self.cur = self.con.cursor()
        self.initUI()
        self.update_table()

    def initUI(self):
        self.setupUi(self)
        self.add_coffee_action.triggered.connect(self.open_add_coffee_form)
        self.edit_coffee_action.triggered.connect(self.open_edit_coffee_form)

    def update_table(self):
        res = self.cur.execute("""SELECT coffee.id, 
                    coffee.title, 
                    roast_degrees.title, 
                    coffee.is_ground, 
                    coffee.flavor, 
                    coffee.price, 
                    coffee.size 
                    FROM coffee
                    LEFT OUTER JOIN
                    roast_degrees
                    ON coffee.roast_degree = roast_degrees.id""").fetchall()
        self.tableWidget.clearContents()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название", "Степень обжарки", "Молотый",
                                                    "Вкус", "Цена", "Объем упаковки"])
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                item = QTableWidgetItem(str(elem))
                item.setFlags(Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, item)
        self.tableWidget.resizeColumnsToContents()

    def open_add_coffee_form(self):
        AddEditCoffeeForm(self).show()

    def open_edit_coffee_form(self):
        current_row = self.tableWidget.currentRow()
        coffee_id = int(self.tableWidget.item(current_row, 0).text())
        AddEditCoffeeForm(self, coffee_id).show()

    def closeEvent(self, event):
        self.con.close()


class AddEditCoffeeForm(QMainWindow, CoffeeForm):
    def __init__(self, parent, coffee_id=None):
        super().__init__(parent)
        self.coffee_id = coffee_id
        self.con = sqlite3.connect("data/coffee.sqlite")
        self.cur = self.con.cursor()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.setWindowTitle("Добавить кофе" if self.coffee_id is None else "Изменить кофе")
        self.set_roast_degrees_list()
        self.set_coffee_info()
        self.save_btn.clicked.connect(self.save_coffee_to_db)

    def set_coffee_info(self):
        if self.coffee_id is None:
            return
        _, title, _, is_ground, flavor, price, size, _, roast_degree = self.cur.execute("""SELECT *
                    FROM coffee
                    LEFT OUTER JOIN
                    roast_degrees
                    ON coffee.roast_degree = roast_degrees.id
                    WHERE coffee.id = ?""", (self.coffee_id,)).fetchone()
        self.title_input.setText(title)
        self.roast_degree_cb.setCurrentText(roast_degree)
        self.is_ground_cb.setCheckState(2 if is_ground else 0)
        self.flavor_input.setText(flavor)
        self.price_input.setValue(price)
        self.size_input.setValue(size)

    def set_roast_degrees_list(self):
        roast_degrees = self.cur.execute("""SELECT title FROM roast_degrees""").fetchall()
        for roast_degree in roast_degrees:
            self.roast_degree_cb.addItem(roast_degree[0])

    def save_coffee_to_db(self):
        title = self.title_input.text().strip()
        if not title:
            self.status_bar.showMessage("Название не может быть пустым")
            return
        if not self.check_originality_title(title):
            self.status_bar.showMessage("Кофе с таким названием уже есть")
            return
        roast_degree = self.roast_degree_cb.currentText()
        roast_degree = self.cur.execute("""SELECT id FROM roast_degrees
                    WHERE title = ?""", (roast_degree,)).fetchone()[0]
        is_ground = 1 if self.is_ground_cb.checkState() else 0
        flavor = self.flavor_input.text()
        price = self.price_input.value()
        size = self.size_input.value()
        if self.coffee_id is None:
            self.cur.execute("""INSERT INTO coffee(
                        title, 
                        roast_degree, 
                        is_ground, 
                        flavor, 
                        price, 
                        size)
                        VALUES(?, ?, ?, ?, ?, ?)""",
                             (title, roast_degree, is_ground, flavor, price, size))
        else:
            self.cur.execute("""UPDATE coffee
                        SET title = ?,
                        roast_degree = ?,
                        is_ground = ?,
                        flavor = ?,
                        price = ?,
                        size = ?
                        WHERE id = ?""", (title, roast_degree, is_ground,
                                          flavor, price, size, self.coffee_id))
        self.con.commit()
        self.parent().update_table()
        self.close()

    def check_originality_title(self, title):
        request = """SELECT * FROM coffee WHERE title = ?"""
        if self.coffee_id is not None:
            request += f""" AND id != {self.coffee_id}"""
        return not self.cur.execute(request, (title,)).fetchall()


    def closeEvent(self, event):
        self.con.close()


def excepthook(cls, value, traceback):
    sys.__excepthook__(cls, value, traceback)


if __name__ == "__main__":
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = CoffeeWindow()
    ex.show()
    sys.exit(app.exec())
