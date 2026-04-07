# -*- coding: utf-8 -*-

import sqlite3
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class AddDialog(QtWidgets.QDialog):
    def __init__(self, table_name, db_path):
        super().__init__()
        self.table_name = table_name
        self.db_path = db_path
        self.setupUi()

    def setupUi(self):
        self.setObjectName("AddDialog")
        self.resize(400, 300)
        icon_path = "W:/PractForKatrin/prog/icon/icon.png"
        if os.path.exists(icon_path):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)

        self.setWindowTitle(f"Добавление записи в {self.get_table_title()}")
        self.layout = QtWidgets.QFormLayout(self)

        if self.table_name == "Kholodilniki":
            self.model_code = QtWidgets.QLineEdit()
            self.model = QtWidgets.QLineEdit()
            self.manufacturer = QtWidgets.QComboBox()
            self.manufacturer.addItems(["Samsung", "LG", "Bosch", "Indesit", "Atlant", "Beko", "Haier"])
            self.freezer = QtWidgets.QSpinBox()
            self.freezer.setMinimum(1)
            self.freezer.setMaximum(5)
            self.color = QtWidgets.QComboBox()
            self.color.addItems(["Белый", "Серебристый", "Черный", "Бежевый", "Серый", "Красный"])
            self.price = QtWidgets.QDoubleSpinBox()
            self.price.setMaximum(999999.99)
            self.price.setPrefix("₽ ")

            self.layout.addRow("Код модели:", self.model_code)
            self.layout.addRow("Модель:", self.model)
            self.layout.addRow("Производитель:", self.manufacturer)
            self.layout.addRow("Кол-во камер:", self.freezer)
            self.layout.addRow("Цвет:", self.color)
            self.layout.addRow("Цена:", self.price)

        elif self.table_name == "Klienty":
            self.last_name = QtWidgets.QLineEdit()
            self.first_name = QtWidgets.QLineEdit()
            self.patronymic = QtWidgets.QLineEdit()
            self.city = QtWidgets.QLineEdit()

            self.layout.addRow("Фамилия:", self.last_name)
            self.layout.addRow("Имя:", self.first_name)
            self.layout.addRow("Отчество:", self.patronymic)
            self.layout.addRow("Город:", self.city)

        else:
            self.client = QtWidgets.QComboBox()
            self.product = QtWidgets.QComboBox()
            self.order_date = QtWidgets.QDateEdit()
            self.order_date.setDate(QtCore.QDate.currentDate())
            self.order_date.setCalendarPopup(True)
            self.quantity = QtWidgets.QSpinBox()
            self.quantity.setMinimum(1)
            self.quantity.setMaximum(100)
            self.discount = QtWidgets.QSpinBox()
            self.discount.setMinimum(0)
            self.discount.setMaximum(100)
            self.discount.setSuffix("%")

            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                cursor.execute("SELECT client_id, last_name, first_name FROM Klienty")
                clients = cursor.fetchall()
                for client in clients:
                    self.client.addItem(f"{client[1]} {client[2]}", client[0])

                cursor.execute("SELECT model_code, model FROM Kholodilniki")
                products = cursor.fetchall()
                for product in products:
                    self.product.addItem(product[1], product[0])
                conn.close()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка загрузки данных: {e}")

            self.layout.addRow("Клиент:", self.client)
            self.layout.addRow("Холодильник:", self.product)
            self.layout.addRow("Дата заказа:", self.order_date)
            self.layout.addRow("Количество:", self.quantity)
            self.layout.addRow("Скидка:", self.discount)

        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.save_record)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addRow(self.buttonBox)

    def get_table_title(self):
        titles = {
            "Kholodilniki": "холодильники",
            "Klienty": "клиенты",
            "Zakazy": "заказы"
        }
        return titles.get(self.table_name, self.table_name)

    def save_record(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            if self.table_name == "Kholodilniki":
                if not self.model_code.text() or not self.model.text():
                    QMessageBox.warning(self, "Ошибка", "Заполните обязательные поля")
                    return
                cursor.execute("""
                               INSERT INTO Kholodilniki
                                   (model_code, model, manufacturer, freezer_compartments, color, price)
                               VALUES (?, ?, ?, ?, ?, ?)
                               """, (
                                   int(self.model_code.text()),
                                   self.model.text(),
                                   self.manufacturer.currentText(),
                                   self.freezer.value(),
                                   self.color.currentText(),
                                   self.price.value()
                               ))

            elif self.table_name == "Klienty":
                if not self.last_name.text() or not self.first_name.text() or not self.city.text():
                    QMessageBox.warning(self, "Ошибка", "Заполните обязательные поля")
                    return
                cursor.execute("""
                               INSERT INTO Klienty (last_name, first_name, patronymic, city)
                               VALUES (?, ?, ?, ?)
                               """, (
                                   self.last_name.text(),
                                   self.first_name.text(),
                                   self.patronymic.text(),
                                   self.city.text()
                               ))

            else:
                cursor.execute("""
                               INSERT INTO Zakazy (client_id, model_code, order_date, quantity, discount)
                               VALUES (?, ?, ?, ?, ?)
                               """, (
                                   self.client.currentData(),
                                   self.product.currentData(),
                                   self.order_date.date().toString("yyyy-MM-dd"),
                                   self.quantity.value(),
                                   self.discount.value()
                               ))

            conn.commit()
            conn.close()
            self.accept()

        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Ошибка", "Запись с таким кодом уже существует")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка сохранения: {e}")