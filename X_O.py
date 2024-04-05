from PyQt5.QtCore import QObject
import PyQt5.QtWidgets as P


class MyWindow(P.QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color:lightred")

        self.lbl = P.QLabel("Press Start to play")
        self.lbl.setStyleSheet("font-size:20px;color:yellow")

        self.lst_X_O = list()

        self.hBox = P.QHBoxLayout()

        self.hBox.addStretch()
        self.hBox.addWidget(self.lbl)
        self.hBox.addStretch()

        self.gird = P.QGridLayout()

        self.btn = P.QPushButton('Restart')
        self.btn.setStyleSheet("background-color:purple")
        self.btn.hide()
        self.btn.clicked.connect(self.restart)

        self.back_btn = P.QPushButton("Back")
        self.back_btn.setStyleSheet("background-color:yellow")
        self.back_btn.hide()
        self.back_btn.clicked.connect(self.Back)

        self.btn_s = P.QPushButton("Start")
        self.btn_s.setStyleSheet("background-color:purple")
        self.btn_s.clicked.connect(self.Start)

        self.btn1 = P.QPushButton(clicked = lambda: self.x_o(0))
        self.btn2 = P.QPushButton(clicked = lambda: self.x_o(1))
        self.btn3 = P.QPushButton(clicked = lambda: self.x_o(2))
        self.btn4 = P.QPushButton(clicked = lambda: self.x_o(3))
        self.btn5 = P.QPushButton(clicked = lambda: self.x_o(4))
        self.btn6 = P.QPushButton(clicked = lambda: self.x_o(5))
        self.btn7 = P.QPushButton(clicked = lambda: self.x_o(6))
        self.btn8 = P.QPushButton(clicked = lambda: self.x_o(7))
        self.btn9 = P.QPushButton(clicked = lambda: self.x_o(8))

        self.lst = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]

        for i in self.lst:
            i.setStyleSheet("background-color:white")

        index = 0

        for i in range(3):
            for j in range(3):
                if index < len(self.lst):
                    self.gird.addWidget(self.lst[index], i, j)
                    self.lst[index].setFixedSize(65,65)
                    self.lst[index].setEnabled(False)
                index += 1

        self.hBoxx = P.QHBoxLayout()

        self.hBoxx.addWidget(self.btn)
        self.hBoxx.addWidget(self.back_btn)

        self.vBox = P.QVBoxLayout()

        self.vBox.addLayout(self.gird)
        self.vBox.addLayout(self.hBoxx)
        self.vBox.addWidget(self.btn_s)
        self.vBox.addLayout(self.hBox)

        self.setLayout(self.vBox)

    def Back(self):
        self.btn_s.show()
        self.btn.hide()
        self.back_btn.hide()

        self.lbl.setText("Press Start to play")

        for i in self.lst:
            i.setEnabled(False)
            i.setText("")
            i.setStyleSheet("background-color:white")

    def Start(self):

        self.lbl.setText("Player X")

        for i in self.lst:
            i.setEnabled(True)

        self.btn_s.hide()
        self.back_btn.show()
        self.btn.show()

    def x_o(self, btn_number):

        num = btn_number       

        if self.lbl.text() == "Player X":
            self.lbl.setText("Player O")
            self.lbl.setStyleSheet("font-size:20px;color:lightblue")
            for i in range(len(self.lst)):
                if num == i:
                    self.lst[i].setText("X")
                    self.lst[i].setStyleSheet("background-color:yellow")
                    self.lst_X_O.append("X")
                    self.lst[i].setEnabled(False)
        elif self.lbl.text() == "Player O":
            self.lbl.setText("Player X")
            self.lbl.setStyleSheet("font-size:20px;color:yellow")

            for i in range(len(self.lst)):
                if num == i:
                    self.lst[i].setText("O")
                    self.lst[i].setStyleSheet("background-color:lightblue")
                    self.lst_X_O.append("O")
                    self.lst[i].setEnabled(False)

        if len(self.lst_X_O) == 9:
            msg = P.QMessageBox()
            msg.setWindowTitle("=")
            msg.setIcon(P.QMessageBox.Information)
            msg.setText("Game over")
            msg.exec_()
            self.lbl.setText("Game over")

    def restart(self):
    
        self.lbl.setText("Player X")

        self.btn_s.hide()
        self.back_btn.show()
        self.btn.show()

        for i in self.lst:
            i.setText("")
            i.setStyleSheet("background-color:white")
            i.setEnabled(True)

app = P.QApplication([])
win = MyWindow()

win.show()
app.exec_()
