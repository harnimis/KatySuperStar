# -*- coding: utf-8 -*-

import sys
import subprocess
import pickle
import tempfile
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)

        # Загрузка иконки из указанного пути
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("W:/PractForKatrin/prog/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)

        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 2)

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMaximumSize(QtCore.QSize(150, 150))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("W:/PractForKatrin/prog/icon/auth.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 2, 1)

        self.retranslateUi(Dialog)

        self.buttonBox.accepted.connect(self.check_auth)
        self.buttonBox.rejected.connect(Dialog.reject)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Холодильники"))
        self.label.setText(_translate("Dialog", "Логин:"))
        self.label_2.setText(_translate("Dialog", "Пароль:"))

    def read_credentials_from_file(self):
        try:
            with open("C:/Users/1/Desktop/PractForKatrin/prog/auth.txt", "r", encoding='utf-8') as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    login = lines[0].strip()
                    password = lines[1].strip()
                    return login, password
                else:
                    print("Ошибка: файл auth.txt должен содержать минимум 2 строки")
                    return None, None
        except FileNotFoundError:
            print("Ошибка: файл auth.txt не найден по пути W:/PractForKatrin/prog/auth.txt")
            return None, None
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return None, None

    def check_auth(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()

        correct_login, correct_password = self.read_credentials_from_file()

        if correct_login is None or correct_password is None:
            QtWidgets.QMessageBox.critical(None, "Ошибка",
                                           "Не удалось загрузить данные авторизации!\n"
                                           "Проверьте наличие файла W:/PractForKatrin/prog/auth.txt")
            return

        if login == correct_login and password == correct_password:
            QtWidgets.QMessageBox.information(None, "Успех", "Авторизация успешна!")
            self.run_main_program(login)
        else:
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Неверный логин или пароль!")

    def run_main_program(self, username):
        try:
            temp_file = tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.pkl')
            pickle.dump(username, temp_file)
            temp_file.close()

            dialog = self.buttonBox.parent()
            dialog.close()

            subprocess.Popen([sys.executable, "main.py", temp_file.name])

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Ошибка",
                                           f"Не удалось запустить main.py:\n{e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
