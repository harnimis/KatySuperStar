# -*- coding: utf-8 -*-

import sys
import sqlite3
import os
import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from add import AddDialog
from edit import EditDialog
from dell import DeleteDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)

        icon_path = "W:/PractForKatrin/prog/icon/icon.png"
        if os.path.exists(icon_path):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_table = QtWidgets.QLabel(self.groupBox)
        self.label_table.setObjectName("label_table")
        self.gridLayout_2.addWidget(self.label_table, 0, 0, 1, 1)

        self.checkBox_products = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_products.setChecked(True)
        self.checkBox_products.setObjectName("checkBox_products")
        self.gridLayout_2.addWidget(self.checkBox_products, 0, 1, 1, 1)

        self.checkBox_clients = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_clients.setObjectName("checkBox_clients")
        self.gridLayout_2.addWidget(self.checkBox_clients, 0, 2, 1, 1)

        self.checkBox_orders = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_orders.setObjectName("checkBox_orders")
        self.gridLayout_2.addWidget(self.checkBox_orders, 0, 3, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 3)

        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 2, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 2, 2, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_2.addWidget(self.radioButton_3, 2, 3, 1, 1)

        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout_2.addWidget(self.tableWidget, 3, 0, 1, 4)

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 4, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 4, 1, 1, 1)
        self.pushButton_delete = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout_2.addWidget(self.pushButton_delete, 4, 2, 1, 1)
        self.pushButton_exit = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.gridLayout_2.addWidget(self.pushButton_exit, 4, 3, 1, 1)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFixedSize(100, 100)
        self.label.setText("")
        logo_path = "W:/PractForKatrin/prog/icon/negr.png"
        if os.path.exists(logo_path):
            pixmap = QtGui.QPixmap(logo_path)
            pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.right_layout = QtWidgets.QVBoxLayout()
        self.right_layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        self.right_layout.addWidget(self.label)

        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setLayout(self.right_layout)
        self.right_widget.setFixedWidth(120)

        self.gridLayout.addWidget(self.right_widget, 0, 1, 1, 1, QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 0)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Магазин холодильников"))
        self.groupBox.setTitle(_translate("MainWindow", "Управление данными"))
        self.label_table.setText(_translate("MainWindow", "Таблица:"))
        self.checkBox_products.setText(_translate("MainWindow", "Холодильники"))
        self.checkBox_clients.setText(_translate("MainWindow", "Клиенты"))
        self.checkBox_orders.setText(_translate("MainWindow", "Заказы"))
        self.label_4.setText(_translate("MainWindow", "Поиск:"))
        self.label_5.setText(_translate("MainWindow", "Сортировка:"))
        self.radioButton.setText(_translate("MainWindow", "По возрастанию"))
        self.radioButton_2.setText(_translate("MainWindow", "Без сортировки"))
        self.radioButton_3.setText(_translate("MainWindow", "По убыванию"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_3.setText(_translate("MainWindow", "Редактировать"))
        self.pushButton_delete.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_exit.setText(_translate("MainWindow", "Выход"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, username=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db_path = "C:/Users/1/Desktop/PractForKatrin/prog/db.db"
        self.current_table = "Kholodilniki"
        self.username = username if username else "Администратор"

        self.ui.statusbar.showMessage(f"Пользователь: {self.username}")

        self.ui.checkBox_products.toggled.connect(self.on_table_changed)
        self.ui.checkBox_clients.toggled.connect(self.on_table_changed)
        self.ui.checkBox_orders.toggled.connect(self.on_table_changed)
        self.ui.lineEdit.textChanged.connect(self.search_data)
        self.ui.radioButton.toggled.connect(self.sort_data)
        self.ui.radioButton_2.toggled.connect(self.sort_data)
        self.ui.radioButton_3.toggled.connect(self.sort_data)
        self.ui.pushButton.clicked.connect(self.add_record)
        self.ui.pushButton_3.clicked.connect(self.edit_record)
        self.ui.pushButton_delete.clicked.connect(self.delete_record)
        self.ui.pushButton_exit.clicked.connect(self.close)

        self.load_data()

        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, 'ui'):
            total_width = self.ui.tableWidget.width()
            column_count = self.ui.tableWidget.columnCount()
            if column_count > 0:
                for i in range(column_count - 1):
                    self.ui.tableWidget.setColumnWidth(i, int(total_width / column_count))

    def on_table_changed(self):
        sender = self.sender()
        if sender == self.ui.checkBox_products and sender.isChecked():
            self.current_table = "Kholodilniki"
            self.ui.checkBox_clients.setChecked(False)
            self.ui.checkBox_orders.setChecked(False)
            self.load_data()
        elif sender == self.ui.checkBox_clients and sender.isChecked():
            self.current_table = "Klienty"
            self.ui.checkBox_products.setChecked(False)
            self.ui.checkBox_orders.setChecked(False)
            self.load_data()
        elif sender == self.ui.checkBox_orders and sender.isChecked():
            self.current_table = "Zakazy"
            self.ui.checkBox_products.setChecked(False)
            self.ui.checkBox_clients.setChecked(False)
            self.load_data()

    def get_sort_field(self):
        if self.current_table == "Kholodilniki":
            return "price"
        elif self.current_table == "Klienty":
            return "last_name"
        else:
            return "order_date"

    def load_data(self, search_text=""):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            if self.current_table == "Kholodilniki":
                query = "SELECT model_code, model, manufacturer, freezer_compartments, color, price FROM Kholodilniki"
                params = []
                if search_text:
                    query += " WHERE model LIKE ? OR manufacturer LIKE ?"
                    params.append(f"%{search_text}%")
                    params.append(f"%{search_text}%")

                sort_type = self.get_sort_type()
                sort_field = self.get_sort_field()
                if sort_type == "asc":
                    query += f" ORDER BY {sort_field} ASC"
                elif sort_type == "desc":
                    query += f" ORDER BY {sort_field} DESC"

                cursor.execute(query, params)
                data = cursor.fetchall()
                headers = ["Код", "Модель", "Производитель", "Камер", "Цвет", "Цена"]

                self.ui.tableWidget.setRowCount(len(data))
                self.ui.tableWidget.setColumnCount(len(headers))
                self.ui.tableWidget.setHorizontalHeaderLabels(headers)

                for row, record in enumerate(data):
                    for col, value in enumerate(record):
                        if col == 5:
                            item = QTableWidgetItem(f"{value:,.0f} руб.")
                        else:
                            item = QTableWidgetItem(str(value))
                        self.ui.tableWidget.setItem(row, col, item)

            elif self.current_table == "Klienty":
                query = "SELECT client_id, last_name, first_name, patronymic, city FROM Klienty"
                params = []
                if search_text:
                    query += " WHERE last_name LIKE ? OR first_name LIKE ? OR city LIKE ?"
                    params.append(f"%{search_text}%")
                    params.append(f"%{search_text}%")
                    params.append(f"%{search_text}%")

                sort_type = self.get_sort_type()
                sort_field = self.get_sort_field()
                if sort_type == "asc":
                    query += f" ORDER BY {sort_field} ASC"
                elif sort_type == "desc":
                    query += f" ORDER BY {sort_field} DESC"

                cursor.execute(query, params)
                data = cursor.fetchall()
                headers = ["ID", "Фамилия", "Имя", "Отчество", "Город"]

                self.ui.tableWidget.setRowCount(len(data))
                self.ui.tableWidget.setColumnCount(len(headers))
                self.ui.tableWidget.setHorizontalHeaderLabels(headers)

                for row, record in enumerate(data):
                    for col, value in enumerate(record):
                        item = QTableWidgetItem(str(value) if value else "")
                        self.ui.tableWidget.setItem(row, col, item)

            else:
                query = """
                        SELECT z.order_id, \
                               k.last_name || ' ' || k.first_name                as client,
                               h.model, \
                               z.order_date, \
                               z.quantity, \
                               z.discount,
                               (h.price * z.quantity * (100 - z.discount) / 100) as total
                        FROM Zakazy z
                                 JOIN Klienty k ON z.client_id = k.client_id
                                 JOIN Kholodilniki h ON z.model_code = h.model_code \
                        """
                params = []
                if search_text:
                    query += " WHERE k.last_name LIKE ? OR k.first_name LIKE ? OR h.model LIKE ?"
                    params.append(f"%{search_text}%")
                    params.append(f"%{search_text}%")
                    params.append(f"%{search_text}%")

                sort_type = self.get_sort_type()
                sort_field = self.get_sort_field()
                if sort_type == "asc":
                    query += f" ORDER BY {sort_field} ASC"
                elif sort_type == "desc":
                    query += f" ORDER BY {sort_field} DESC"

                cursor.execute(query, params)
                data = cursor.fetchall()
                headers = ["№ заказа", "Клиент", "Модель", "Дата", "Кол-во", "Скидка", "Сумма"]

                self.ui.tableWidget.setRowCount(len(data))
                self.ui.tableWidget.setColumnCount(len(headers))
                self.ui.tableWidget.setHorizontalHeaderLabels(headers)

                for row, record in enumerate(data):
                    for col, value in enumerate(record):
                        if col == 5:
                            item = QTableWidgetItem(f"{value}%")
                        elif col == 6:
                            item = QTableWidgetItem(f"{value:,.2f} руб.")
                        else:
                            item = QTableWidgetItem(str(value))
                        self.ui.tableWidget.setItem(row, col, item)

            conn.close()

            total_width = self.ui.tableWidget.width()
            column_count = len(headers)
            if column_count > 0:
                for i in range(column_count):
                    if i == column_count - 1:
                        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
                    else:
                        self.ui.tableWidget.setColumnWidth(i, int(total_width / column_count))

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка загрузки: {e}")

    def search_data(self):
        search_text = self.ui.lineEdit.text()
        self.load_data(search_text)

    def sort_data(self):
        search_text = self.ui.lineEdit.text()
        self.load_data(search_text)

    def get_sort_type(self):
        if self.ui.radioButton.isChecked():
            return "asc"
        elif self.ui.radioButton_3.isChecked():
            return "desc"
        else:
            return "none"

    def add_record(self):
        dialog = AddDialog(self.current_table, self.db_path)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.load_data(self.ui.lineEdit.text())
            self.ui.statusbar.showMessage("Запись успешно добавлена", 3000)
            QMessageBox.information(self, "Успех", "Запись успешно добавлена")

    def edit_record(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Предупреждение", "Выберите запись для редактирования")
            return

        record_id = self.ui.tableWidget.item(current_row, 0).text()
        dialog = EditDialog(self.current_table, self.db_path, record_id)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.load_data(self.ui.lineEdit.text())
            self.ui.statusbar.showMessage("Запись успешно обновлена", 3000)
            QMessageBox.information(self, "Успех", "Запись успешно обновлена")

    def delete_record(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Предупреждение", "Выберите запись для удаления")
            return

        record_id = self.ui.tableWidget.item(current_row, 0).text()
        dialog = DeleteDialog(self.current_table, self.db_path, record_id)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.load_data(self.ui.lineEdit.text())
            self.ui.statusbar.showMessage("Запись успешно удалена", 3000)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    username = "Администратор"
    if len(sys.argv) > 1:
        try:
            temp_file = sys.argv[1]
            with open(temp_file, 'rb') as f:
                username = pickle.load(f)
            os.unlink(temp_file)
        except Exception as e:
            print(f"Ошибка загрузки имени пользователя: {e}")

    window = MainWindow(username)
    window.show()
    sys.exit(app.exec_())
