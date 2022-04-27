from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTableWidget, QPushButton, QApplication, QVBoxLayout, QTableWidgetItem, QLabel
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from faker import Factory
import pandas as pd
import sys


class ui(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.btn.clicked.connect(self.read_data)

    def setupUI(self):
        self.setWindowTitle('嗨嗨你好')
        self.resize(640, 480)

        self.faker = Factory.create()

        self.btn = QPushButton('讀資料 & 顯示')
        self.spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.btn)
        self.vbox.addSpacerItem(self.spacerItem)

        self.table = QTableWidget(self)
        # 設定table的欄數
        self.table.setColumnCount(3)
        # 設定table每一欄的標題
        self.headers = ['stock_id', 'sell_date', 'profit(%)']
        self.table.setHorizontalHeaderLabels(self.headers)

        self.txt = QLabel()
        self.txt.setMinimumHeight(50)
        self.vbox2 = QVBoxLayout()
        self.vbox2.addWidget(self.table)
        self.vbox2.addWidget(self.txt)

        self.hbox = QHBoxLayout()
        self.hbox.addLayout(self.vbox2)
        self.hbox.addLayout(self.vbox)
        self.setLayout(self.hbox)

        self.show()

    def read_data(self):
        df = self.get_df()

        # 一行一行把dataframe的資料丟到QTableWidget裡面
        for index, row in df.iterrows():
            rowCount = self.table.rowCount()
            newRowIdx = rowCount
            self.table.setRowCount(rowCount + 1)
            
            # 設定從dataframe讀出來的格式
            id = '{:04d}'.format(row['stock_id'])
            sell_date = row['sell_date']
            profit = '{:0.2f}'.format(row['profit'])
            
            self.table.setItem(newRowIdx, 0, QTableWidgetItem(id))
            self.table.setItem(newRowIdx, 1, QTableWidgetItem(sell_date))
            self.table.setItem(newRowIdx, 2, QTableWidgetItem(profit))

        self.settext('讀get_df的資料，加在table最後面')

    def get_df(self):
        # 回傳一個dataframe
        grades = {"stock_id": [1203, 1218, 1231, 1310], 
                  "sell_date": ["2017-03-02", "2017-03-02", "2017-03-02", "2017-03-02"], 
                  "profit": [3.5, 2.15, 3.888, 0.75499]}

        df = pd.DataFrame(grades)
        return df

    def settext(self, txt):
        font = QFont('Calibri', 10)
        self.txt.setFont(font)
        self.txt.setText(txt)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ui()
    sys.exit(app.exec_())