from PyQt4 import QtGui, QtCore
import sys
import resources
from OTP import OTP

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setMaximumSize(1920, 1080)
        self.setMinimumSize(1280, 800)
        self.showMaximized()
        self.set_center()
        self.setWindowTitle("Quantum Key Distribution")
        self.setStyleSheet("QMainWindow { border-image: url(:/images/qkdback.png); } ")
        self.bcontainer = QtGui.QWidget()
        self.bcontainer_layout = QtGui.QHBoxLayout()
        self.bcontainer.setLayout(self.bcontainer_layout)
        self.bb84btn = QtGui.QPushButton(self)
        self.bb84btn.setMaximumSize(250, 245)
        self.bb84btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bb84btn.setObjectName("bb84btn")
        self.bb84btn.setStyleSheet("""
            #bb84btn { 
                border-image: url(:/images/bb84.png);
                border-radius: 15px; 
            } 
        """)
        self.e91btn = QtGui.QPushButton(self)
        self.e91btn.setMaximumSize(250, 245)
        self.e91btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.e91btn.setObjectName("e91btn")
        self.e91btn.setStyleSheet("""
            #e91btn { 
                border-image: url(:/images/e91.png);
                border-radius: 15px; 
            } 
        """)
        self.otpbtn = QtGui.QPushButton(self)
        self.otpbtn.setMaximumSize(250, 245)
        self.otpbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.otpbtn.setObjectName("otpbtn")
        self.otpbtn.setStyleSheet("""
            #otpbtn { 
                border-image: url(:/images/otp.png);
                border-radius: 15px; 
            } 
        """)
        self.otpbtn.clicked.connect(self.open_otp)
        self.bcontainer_layout.addWidget(self.bb84btn)
        self.bcontainer_layout.addWidget(self.otpbtn)
        self.bcontainer_layout.addWidget(self.e91btn)
        self.setCentralWidget(self.bcontainer)
        self.otpcontainer = QtGui.QWidget()
        self.otpcontainer_layout = QtGui.QFormLayout()
        self.otpcontainer_layout.setVerticalSpacing(30)
        self.otpcontainer_layout.setHorizontalSpacing(20)
        self.otpcontainer_layout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.otpcontainer.setLayout(self.otpcontainer_layout)
        self.messagelabel = QtGui.QLabel("Plaintext/Cipher: ")
        self.messagelabel.setObjectName("messagelabel")
        self.messagelabel.setStyleSheet("""
            #messagelabel { 
                font-size: 30px;
                font-weight: bold;
                color: white;
            } 
        """)
        self.messageform = QtGui.QLineEdit()
        self.messageform.setMinimumSize(200, 25)
        self.messageform.setPlaceholderText("Hello World!")
        self.ed_optionlabel = QtGui.QLabel("Option:")
        self.ed_optionlabel.setObjectName("ed_optionlabel")
        self.ed_optionlabel.setStyleSheet("""
            #ed_optionlabel { 
                font-size: 30px;
                color: white;
                font-weight: bold;
            } 
        """)
        self.ed_optionlist = QtGui.QComboBox()
        self.ed_optionlist.addItem("Encryption")
        self.ed_optionlist.addItem("Decryption")
        self.ed_optionlist.setObjectName("ed_optionlist")
        self.ed_optionlist.setStyleSheet("""
            #ed_optionlist { 
                color: black;
            } 
        """)
        self.ed_optionlist.setMinimumHeight(50)
        self.ed_optionlist.setMinimumSize(200, 25)
        self.keylabel = QtGui.QLabel("Cipher Key:")
        self.keylabel.setObjectName("keylabel")
        self.keylabel.setStyleSheet("""
            #keylabel { 
                font-size: 30px;
                font-weight: bold;
                color: white;
            } 
        """)
        self.keyform = QtGui.QLineEdit()
        self.keyform.setMinimumSize(200, 25)
        self.keyform.setPlaceholderText("912589347328")
        self.keygeneratorlabel = QtGui.QLabel("Key Generator:")
        self.keygeneratorlabel.setObjectName("keygeneratorlabel")
        self.keygeneratorlabel.setStyleSheet("""
            #keygeneratorlabel { 
                font-size: 30px;
                font-weight: bold;
                color: white;
            } 
        """)
        self.keygeneratorbtn = QtGui.QPushButton("Generate")
        self.keygeneratorbtn.setMinimumHeight(40)
        self.keygeneratorbtn.setMaximumWidth(210)
        self.keygeneratorbtn.setObjectName("keygeneratorbtn")
        self.keygeneratorbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.keygeneratorbtn.clicked.connect(self.set_otpkey)
        self.submitotp = QtGui.QPushButton("Show Result")
        self.submitotp.setMinimumHeight(60)
        self.submitotp.setMinimumWidth(200)
        self.submitotp.setObjectName("submitotp")
        self.submitotp.setStyleSheet("""
            #submitotp {
                font-size: 25px;
                color: white;
                background-color: black;
                font-weight: bold;
                border-radius: 3px;
            }
        """)
        self.otpresult = QtGui.QLabel("Result will be displayed here.")
        self.otpresult.setObjectName("otpresult")
        self.otpresult.setStyleSheet("""
            #otpresult { 
                font-size: 20px;
                font-weight: bold;
                color: white;
            } 
        """)
        self.submitotp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.otpcontainer_layout.addRow(self.messagelabel, self.messageform)
        self.otpcontainer_layout.addRow(self.ed_optionlabel, self.ed_optionlist)
        self.otpcontainer_layout.addRow(self.keylabel, self.keyform)
        self.otpcontainer_layout.addRow(self.keygeneratorlabel, self.keygeneratorbtn)
        self.otpcontainer_layout.addRow(self.otpresult, self.submitotp)
        self.show()
        self.raise_()

    def open_otp(self):
        self.set_hide_home()
        self.setCentralWidget(self.otpcontainer)

    def set_hide_home(self):
        self.bcontainer.hide()

    def set_center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def set_otpkey(self):
        msgtext = self.messageform.text()
        if len(msgtext) == 0:
            self.raise_otperror("Keygen error", "You must fill message field first.")
        else:
            otp = OTP(str(msgtext))
            self.keyform.clear()
            self.keyform.setText(otp.generate())

    def raise_otperror(self, message, subtext):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Critical)
        msg.setText(message)
        msg.setInformativeText(subtext)
        msg.setWindowTitle("OTP Error")
        msg.exec_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
