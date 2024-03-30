import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem
from PyQt5 import uic
from PyQt5 import QtGui
import sqlite3


class HomeAccounting(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainWindow.ui', self)
        self.setWindowTitle('Домашняя бухгалтерия')
        self.setWindowIcon(QtGui.QIcon('Icon.png'))
        self.Account1.clicked.connect(self.Account1Func)
        self.CloseAllButton.clicked.connect(self.CloseFunc)

    def CloseFunc(self):
        self.close()

    def Account1Func(self):
        self.accountwindow = AccountWindow()
        self.accountwindow.show()


class AccountWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('AccountWindow.ui', self)
        self.setWindowTitle('Основной счет')
        self.ToCreateIncomeButton.clicked.connect(self.ToCreateIncomeFunc)
        self.ToMainWindowButton.clicked.connect(self.ToMainWindowFunc)
        self.UpdateButton.clicked.connect(self.UpdateButtonFunc)
        self.DeleteButton.clicked.connect(self.DeleteButtonFunc)
        self.con = sqlite3.connect("project.sqlite")

    def DeleteButtonFunc(self):
        self.deletewindow = DeleteWindow()
        self.deletewindow.show()

    def UpdateButtonFunc(self):
        cur = self.con.cursor()
        cur.execute('''SELECT * FROM Incomes''')
        data = cur.fetchall()
        if data:
            self.BdWidget.setRowCount(len(data))
            self.BdWidget.setColumnCount(len(data[0]))
            for i in range(len(data)):
                for j in range(len(data[0])):
                    item = QTableWidgetItem(str(data[i][j]))
                    self.BdWidget.setItem(i, j, item)
        else:
            self.BdWidget.clear()

    def ToCreateIncomeFunc(self):
        self.incomeWindow = IncomeWindow()
        self.incomeWindow.show()

    def ToMainWindowFunc(self):
        self.close()


class IncomeWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('IncomeWindow.ui', self)
        self.con = sqlite3.connect("project.sqlite")
        self.setWindowTitle('Добавление')
        self.SaveButton.clicked.connect(self.SaveButtonFunc)

    def SaveButtonFunc(self):
        self.name = self.NameInput.text()
        self.summ = self.SummInput.text()
        self.comment = self.CommentInput.text()

        cur = self.con.cursor()
        cur.execute('''INSERT INTO Incomes(Name, Sum, Comment) VALUES(?, ?, ?)''', (self.name,
                                                                                    self.summ, self.comment))
        self.con.commit()
        self.close()


class DeleteWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('DeleteWindow.ui', self)
        self.setWindowTitle('Удаление')
        self.con = sqlite3.connect("project.sqlite")
        self.DeleteButtonInW.clicked.connect(self.DeleteButtonInWFunc)
        self.CloseButton.clicked.connect(self.CloseButtonFunc)

    def CloseButtonFunc(self):
        self.close()

    def DeleteButtonInWFunc(self):
        self.id = self.IdInput.text()
        cur = self.con.cursor()
        cur.execute('''DELETE FROM Incomes WHERE id = ?''', (self.id))
        self.con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HomeAccounting()
    ex.show()
    sys.exit(app.exec())
