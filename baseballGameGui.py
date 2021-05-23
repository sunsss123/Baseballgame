##------------------------------------------------------------------------------------------------##
##
##------------------------------------------------------------------------------------------------##
import sys
import random

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QDesktopWidget, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
##------------------------------------------------------------------------------------------------##
##
##------------------------------------------------------------------------------------------------##
class MyApp(QWidget):
    ##--------------------------------------------------------------------------------------------##
    ##
    ##--------------------------------------------------------------------------------------------##
    base1_X = 488
    base1_Y = 270
    base2_X = 313
    base2_Y = 95
    base3_X = 138
    base3_Y = 270
    HomeBase_X = 313
    HOmeBase_Y = 503


    ##--------------------------------------------------------------------------------------------##
    ##
    ##--------------------------------------------------------------------------------------------##
    def __init__(self):
        super().__init__()
        self.initUI()
    ##--------------------------------------------------------------------------------------------##
    ##
    ##--------------------------------------------------------------------------------------------##
    def initUI(self):
        # vBox = QVBoxLayout()
        self.value = 0

        self.cnt = 0
        self.guess = []
        self.strikecnt = 0
        self.ballcnt = 0



        # self.msg = QMessageBox()

        imBackground = QPixmap('base.png')
        self.lbBackground = QLabel(self)
        self.lbBackground.setPixmap(imBackground)
        self.lbBackground.move(0,0)

        # vBox.addWidget(lbBackground)
        # self.setLayout(vBox)

        self.lbl = QLabel(str(self.value), self)
        self.lbl.move(60, 40)

        self.lbl2 = QLabel(str(self.value), self)
        self.lbl2.move(60, 60)

        self.qle = QLineEdit(self)
        self.qle.resize(100, 20)
        self.qle.move(10, 10)
        self.qle.textChanged.connect(self.lineEdit_textChanged)

        self.btnOk = QPushButton('Button1', self)
        self.btnOk.setText('확인')
        self.btnOk.resize(30, 20)
        self.btnOk.move(125, 10)
        self.btnOk.clicked.connect(self.setOnClickBtnOk)

        imPlayer1 = QPixmap('player1.png')
        self.lbPlayer1 = QLabel(self)
        self.lbPlayer1.setPixmap(imPlayer1)
        self.lbPlayer1.move(self.base1_X, self.base1_Y)

        imPlayer2 = QPixmap('player2.png')
        self.lbPlayer2 = QLabel(self)
        self.lbPlayer2.setPixmap(imPlayer2)
        self.lbPlayer2.move(self.base2_X, self.base2_Y)

        self.center()
        self.setWindowTitle('new_숫자야구')
        self.resize(626, 626) #화면 크기 변경
        self.show()

        self.newNumber()

    ##--------------------------------------------------------------------------------------------##
    ##
    ##--------------------------------------------------------------------------------------------##
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    ##--------------------------------------------------------------------------------------------##
    ##
    ##--------------------------------------------------------------------------------------------##
    # def onChanged(self, text):
    #     self.lbl.setText(text)
    #     self.lbl.adjustSize()
    ##--------------------------------------------------------------------------------------------##
    ##
    ##--------------------------------------------------------------------------------------------##
    def lineEdit_textChanged(self):
        pass
    ##--------------------------------------------------------------------------------------------##
    ##
    ##--------------------------------------------------------------------------------------------##
    def setOnClickBtnOk(self):
        self.checkValue()
        self.strikecnt = 0
        self.ballcnt = 0
    ##--------------------------------------------------------------------------------------------##
    ##
    ##--------------------------------------------------------------------------------------------##
    def newNumber(self):
        self.value = random.sample(range(1, 10), 4)
        self.lbl.setText(str(self.value))

    def checkValue(self):
        # 초기화

        # for i in range(4):
        for i in range(4):
            self.guess.append(int(self.qle.text()[i]))
        # num = int(input("{}, 1~9까지 숫자를 입력하세요:".format(i)))
        # self.guess.append(int(self.qle.text()))
        # self.guess = list()
        # print(guess)

        for i in range(4):
            if self.guess[i] == self.value[i]:
                self.strikecnt = self.strikecnt + 1
            elif self.guess[i] in self.value:
                self.ballcnt += 1

        self.lbl2.setText(str(self.guess))

        self.qle.clear()
        self.lbl.clear()
        self.lbl2.clear()
        self.guess.clear()

        self.newNumber()

        QMessageBox.about(self, "message", "strike = {}, ball = {}".format(self.strikecnt, self.ballcnt))
        # print("strike = {}, ball = {}".format(strikecnt, ballcnt))




    ##--------------------------------------------------------------------------------------------##
    ##
    ##--------------------------------------------------------------------------------------------##
    if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
##------------------------------------------------------------------------------------------------##
##
##------------------------------------------------------------------------------------------------##