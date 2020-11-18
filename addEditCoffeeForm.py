# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 277)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.title_input = QtWidgets.QLineEdit(self.centralwidget)
        self.title_input.setMaxLength(32)
        self.title_input.setObjectName("title_input")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.title_input)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.is_ground_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.is_ground_cb.setObjectName("is_ground_cb")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.is_ground_cb)
        self.flavor_input = QtWidgets.QLineEdit(self.centralwidget)
        self.flavor_input.setMaxLength(256)
        self.flavor_input.setObjectName("flavor_input")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.flavor_input)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setObjectName("save_btn")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.save_btn)
        self.price_input = QtWidgets.QSpinBox(self.centralwidget)
        self.price_input.setMaximum(100000)
        self.price_input.setObjectName("price_input")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.price_input)
        self.size_input = QtWidgets.QSpinBox(self.centralwidget)
        self.size_input.setMaximum(100000)
        self.size_input.setObjectName("size_input")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.size_input)
        self.roast_degree_cb = QtWidgets.QComboBox(self.centralwidget)
        self.roast_degree_cb.setObjectName("roast_degree_cb")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.roast_degree_cb)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.setObjectName("status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_4.setText(_translate("MainWindow", "Цена"))
        self.label_2.setText(_translate("MainWindow", "Название"))
        self.label_5.setText(_translate("MainWindow", "Степень обжарки"))
        self.is_ground_cb.setText(_translate("MainWindow", "Молотый"))
        self.label.setText(_translate("MainWindow", "Объём упаковки"))
        self.save_btn.setText(_translate("MainWindow", "Сохранить"))