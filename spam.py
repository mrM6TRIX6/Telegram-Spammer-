#Telegram spammer by Ilya
#Thanks for download

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
import sys
import pyautogui
import pyperclip
import keyboard

class spammer(QMainWindow):
    def __init__(self):
        super(spammer, self).__init__()

        self.setObjectName("Spammer")
        self.setWindowTitle("Telegram Spammer+")
        self.setGeometry(500, 400, 500, 450)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("telegram.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.StartText = QtWidgets.QLabel(self)
        self.StartText.setGeometry(QtCore.QRect(115, 30, 270, 50))
        self.StartText.setText("Telegram Spammer+")
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(20)
        self.StartText.setFont(font)
        self.StartText.setObjectName("StartText")

        self.TextPrivate = QtWidgets.QLabel(self)
        self.TextPrivate.setGeometry(QtCore.QRect(217, 75, 66, 15))
        self.TextPrivate.setText("By: Ilya")
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(10)
        self.TextPrivate.setFont(font)
        self.TextPrivate.setObjectName("Text Private")

        self.MessageAmount = QtWidgets.QLabel(self)
        self.MessageAmount.setGeometry(QtCore.QRect(20, 120, 180, 20))
        self.MessageAmount.setText("Количество сообщений:")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.MessageAmount.setFont(font)
        self.MessageAmount.setObjectName("Message Amount")

        self.MessageAmountInput = QtWidgets.QLineEdit(self)
        self.MessageAmountInput.setGeometry(QtCore.QRect(210, 120, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.MessageAmountInput.setFont(font)
        self.MessageAmountInput.setObjectName("Message Amount Input")

        self.Text = QtWidgets.QLabel(self)
        self.Text.setGeometry(QtCore.QRect(20, 160, 180, 20))
        self.Text.setText("Текст:")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.Text.setFont(font)
        self.Text.setObjectName("Text")

        self.TextInput = QtWidgets.QLineEdit(self)
        self.TextInput.setGeometry(QtCore.QRect(210, 160, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.TextInput.setFont(font)
        self.TextInput.setObjectName("Text Input")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(140, 250, 220, 50))
        self.pushButton.setText("START!")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("startButton")

        self.Countdown = QtWidgets.QLabel(self)
        self.Countdown.setGeometry(QtCore.QRect(185, 310, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Countdown.setFont(font)
        self.Countdown.setStyleSheet("color: rgb(255, 0, 0);")
        self.Countdown.setObjectName("")
        self.Countdown.hide()

        self.WarningNoInt = QtWidgets.QLabel(self)
        self.WarningNoInt.setGeometry(QtCore.QRect(210, 140, 160, 15))
        self.WarningNoInt.setText("Можно вводить только числа!")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.WarningNoInt.setFont(font)
        self.WarningNoInt.setStyleSheet("color: rgb(255, 0, 0);")
        self.WarningNoInt.setObjectName("Warning Text")
        self.WarningNoInt.hide()

        self.WarningNoTextAmount = QtWidgets.QLabel(self)
        self.WarningNoTextAmount.setGeometry(QtCore.QRect(210, 140, 160, 15))
        self.WarningNoTextAmount.setText("Поле не может быть пустым!")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.WarningNoTextAmount.setFont(font)
        self.WarningNoTextAmount.setStyleSheet("color: rgb(255, 0, 0);")
        self.WarningNoTextAmount.setObjectName("Warning Text")
        self.WarningNoTextAmount.hide()

        self.WarningNoText = QtWidgets.QLabel(self)
        self.WarningNoText.setGeometry(QtCore.QRect(210, 180, 180, 15))
        self.WarningNoText.setText("Поле не может быть пустым!")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.WarningNoText.setFont(font)
        self.WarningNoText.setStyleSheet("color: rgb(255, 0, 0);")
        self.WarningNoText.setObjectName("label_6")
        self.WarningNoText.hide()

        self.pushButton.clicked.connect(self.checks)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

    def update_timer(self):
        self.Countdown.setText("Старт через: " + str(self.timeAmount))

        if self.timeAmount == -1:
            self.timer.stop()
            self.Countdown.hide()
            self.spam()
            return
        self.timeAmount -= 1

    def _start(self):
        self.timeAmount = 10
        self.Countdown.show()
        self.timer.start(1000)

    def checks(self):
        if self.MessageAmountInput.text() == "":
            self.WarningNoInt.hide()
            self.WarningNoTextAmount.show()
        else:
            self.WarningNoTextAmount.hide()

            try:
                self.WarningNoInt.hide()
                self.Amount = int(self.MessageAmountInput.text())

            except:
                self.WarningNoInt.show()

            else:
                if self.TextInput.text() == "":
                    self.WarningNoText.show()

                else:
                    self.WarningNoText.hide()
                    self.Message = self.TextInput.text()

                    self._start()

    def spam(self):
        pyperclip.copy(self.Message)

        while self.Amount > 0:
            self.Amount -= 1

            keyboard.press_and_release("ctrl + v")
            pyautogui.press("enter")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    spammer = spammer()

    spammer.show()
    sys.exit(app.exec_())
