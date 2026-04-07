# -*- coding: utf-8 -*-

import sqlite3
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class DeleteDialog(QtWidgets.QDialog):
    def __init__(self, table_name, db_path, record_id):
        super().__init__()
        self.table_name = table_name
        self.db_path = db_path
        self.record_id = record_id
        self.setupUi()

    def setupUi(self):
        self.setObjectName("DeleteDialog")
        self.resize(300, 150)
        icon_path = "W:/PractForKatrin/prog/icon/icon.png"
        if os.path.exists(icon_path):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)

        self.setWindowTitle("Подтверждение удаления")
        self.layout = QtWidgets.QVBoxLayout(self)

        self.label = QtWidgets.QLabel(
            f"Вы уверены, что хотите удалить запись {self.record_id} из таблицы {self.get_table_title()}?")
        self.label.setWordWrap(True)
        self.layout.addWidget(self.label)

        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Yes | QtWidgets.QDialogButtonBox.No)
        self.buttonBox.accepted.connect(self.delete_record)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)

    def get_table_title(self):
        titles = {
            "Kholodilniki": "холодильники",
            "Klienty": "клиенты",
            "Zakazy": "заказы"
        }
        return titles.get(self.table_name, self.table_name)

    def delete_record(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            if self.table_name == "Kholodilniki":
                cursor.execute("SELECT COUNT(*) FROM Zakazy WHERE model_code = ?", (self.record_id,))
                count = cursor.fetchone()[0]
                if count > 0:
                    QMessageBox.warning(self, "Ошибка", f"Нельзя удалить, есть {count} связанных заказов")
                    conn.close()
                    return
                cursor.execute("DELETE FROM Kholodilniki WHERE model_code = ?", (self.record_id,))

            elif self.table_name == "Klienty":
                cursor.execute("SELECT COUNT(*) FROM Zakazy WHERE client_id = ?", (self.record_id,))
                count = cursor.fetchone()[0]
                if count > 0:
                    QMessageBox.warning(self, "Ошибка", f"Нельзя удалить, есть {count} связанных заказов")
                    conn.close()
                    return
                cursor.execute("DELETE FROM Klienty WHERE client_id = ?", (self.record_id,))

            else:
                cursor.execute("DELETE FROM Zakazy WHERE order_id = ?", (self.record_id,))

            conn.commit()
            conn.close()
            QMessageBox.information(self, "Успех", "Запись успешно удалена")
            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка удаления: {e}")
            self.reject()