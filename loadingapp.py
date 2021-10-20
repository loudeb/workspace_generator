import subprocess
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog

class Path():
    def __init__(self, app_name, app_path):
        self.app_name = app_name
        self.app_path = app_path


class Saved_Programs():
    def __init__(self):
        self.paths_open = []

    def get_paths_open(self):
        for i in self.paths_open:
            print(i.app_name)

    def add_path(self, app_name, app_path):
        self.paths_open.append(Path(app_name, app_path))


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle('Laptop Mode switcher')
        self.initgui()
        self.count = 0

    def initgui(self):
        # first button
        self.but1 = QtWidgets.QPushButton(self)
        self.but1.setText('Work Mode')
        self.but1.clicked.connect(self.but1_clicked)

        #button 2
        self.but2 = QtWidgets.QPushButton(self)
        self.but2.setText('Chinese Learning')
        self.but2.clicked.connect(self.but2_clicked)
        self.but2.move(100,0)

        #button 3
        self.but3 = QtWidgets.QPushButton(self)
        self.but3.setText('Relaxing')
        self.but3.clicked.connect(self.but3_clicked)
        self.but3.move(200,0)


    def but1_clicked(self):
        text, ok = QInputDialog.getText(self, 'Portfolio Generator', 'Enter Portfolio name')
        newp = Portfolio(text)
        newp.save_portfolio()

    def but2_clicked(self):
        # TODO add exception handling for wrongly entered names, or add drop down of files?
        text, ok = QInputDialog.getText(self, 'stock addition', 'Enter portfolio name')
        portadd = load_portfolio(text)
        stock_tikr, ok = QInputDialog.getText(self, 'Stock Generator', 'Enter Tikr')
        stock_q, ok = QInputDialog.getText(self, 'Stock Generator', 'Enter Quantity')
        purchase_price, ok = QInputDialog.getText(self, 'Stock Generator', 'Enter Price')
        print(stock_q)
        portadd.add_stock(stock_tikr, stock_q)
        print(stock_q)
        portadd.save_portfolio()

    def but3_clicked(self):
        text, ok = QInputDialog.getText(self, 'Portfolio Generator', 'Enter Portfolio name')
        newp = Portfolio(text)
        newp.save_portfolio()

# asd = Saved_Programs()
# asd.add_path("google", "asdaad")
# asd.get_paths_open()