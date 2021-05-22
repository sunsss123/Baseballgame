##------------------------------------------------------------------------------------------------##
##
##------------------------------------------------------------------------------------------------##
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QDesktopWidget, QLineEdit
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

        imBackground = QPixmap('base.png')
        self.lbBackground = QLabel(self)
        self.lbBackground.setPixmap(imBackground)
        self.lbBackground.move(0,0)

        # vBox.addWidget(lbBackground)
        # self.setLayout(vBox)

        # self.lbl = QLabel(self)
        # self.lbl.move(60, 40)

        self.qle = QLineEdit(self)
        self.qle.resize(100, 20)
        self.qle.move(10, 10)
        self.qle.textChanged.connect(self.lineEdit_textChanged)


        imPlayer1 = QPixmap('player1.png')
        self.lbPlayer1 = QLabel(self)
        self.lbPlayer1.setPixmap(imPlayer1)
        self.lbPlayer1.move(self.base1_X, self.base1_Y)

        imPlayer2 = QPixmap('player2.png')
        self.lbPlayer2 = QLabel(self)
        self.lbPlayer2.setPixmap(imPlayer2)
        self.lbPlayer2.move(self.base2_X, self.base2_Y)

        # imPlayer2 = QPixmap('player2.png')
        # lbPlayer2 = QLabel(self)
        # lbPlayer2.setPixmap(imPlayer2)
        # lbPlayer2.move(self.base2_X, self.base2_Y)

        ##----------------------------------------------------------------------------------------##
        ## vBox
        ##----------------------------------------------------------------------------------------##

        # vBox.addWidget(lbPlayer1)
        # vBox.addWidget(lbPlayer2)
        
        ##----------------------------------------------------------------------------------------##
        ##
        ##----------------------------------------------------------------------------------------##

        self.center()
        self.setWindowTitle('new_숫자야구')
        self.resize(626, 626) #화면 크기 변경
        self.show()

        # lbl_img = QLabel()
        # lbl_img.setPixmap(imBackground)
        # lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
        # lbl_size.setAlignment(Qt.AlignCenter)

        
        
        # vbox.addWidget(lbl_size)
        
        # self.setLayout(setPlayer1UI(self.base1_X, self.base1_Y))

        
        # self.move(300, 300)
        
        
        # self.setWindowTitle('My First Application')
        # self.move(300, 300) #화면 위치 설정
        # self.resize(800, 600) #화면 크기 변경
        # self.center() #화면 중앙에 표시
        # self.show()
        
        # self.setWindowTitle('Quit Button')
        # self.setGeometry(300, 300, 300, 200)
        # self.show()
    ##--------------------------------------------------------------------------------------------##
    ##
    ##--------------------------------------------------------------------------------------------##
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # def onChanged(self, text):
    #     self.lbl.setText(text)
    #     self.lbl.adjustSize()

    def lineEdit_textChanged(self):
        pass
    ##--------------------------------------------------------------------------------------------##
    ##
    ##--------------------------------------------------------------------------------------------##
    # def setPlayer1UI(base_x, base_Y):
    #     imPlayer1 = QPixmap('player1.png')

    #     lbPlayer1 = QLabel()
    #     lbPlayer1.setPixmap(imPlayer1)
        
    #     print(base_X)
    #     print(base_Y)

    #     vbox = QVBoxLayout()
    #     vbox.addWidget(lbPlayer1)
    #     vbox.move(base1, base2)

    #     return vbox
    ##--------------------------------------------------------------------------------------------##
    ##
    ##--------------------------------------------------------------------------------------------##
    # def setPlayer2UI(base_X, base_Y):
    #     imPlayer2 = QPixmap('player2.png')

    #     lbPlayer2 = QLabel()
    #     lbPlayer2.setPixmap(imPlayer2)

    #     vbox = QVBoxLayout()
    #     vbox.addWidget(lbPlayer2)
    #     vbox.move(base1, base2)
    
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