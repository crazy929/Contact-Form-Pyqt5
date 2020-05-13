


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(769, 486)
        Form.setStyleSheet("#Form{\n"
"background-image:url(C:/Users/Crazy/Desktop/img/bg8.jpg);\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 771, 51))
        self.frame.setStyleSheet("QFrame{\n"
"background-color:rgba(0,0,0,.5);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(30, 0, 301, 51))
        self.frame_3.setStyleSheet("QFrame{\n"
"background-color:rgba(0,0,0,0);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.labelContact = QtWidgets.QLabel(self.frame_3)
        self.labelContact.setGeometry(QtCore.QRect(120, 10, 171, 31))
        self.labelContact.setStyleSheet("QLabel\n"
"{\n"
"color:white;\n"
"font-size:30px;\n"
"}\n"
"\n"
"\n"
"")
        self.labelContact.setObjectName("labelContact")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(10, -5, 71, 61))
        self.frame_4.setStyleSheet("border-image: url(:/newPrefix/MI_DARK_BLUE_ICON_SUPPORT.png);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(480, 60, 341, 261))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/d1.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.TextFName = QtWidgets.QLineEdit(Form)
        self.TextFName.setGeometry(QtCore.QRect(150, 70, 151, 31))
        self.TextFName.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"}")
        self.TextFName.setObjectName("TextFName")
        self.TextLName = QtWidgets.QLineEdit(Form)
        self.TextLName.setGeometry(QtCore.QRect(330, 70, 151, 31))
        self.TextLName.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"}")
        self.TextLName.setObjectName("TextLName")
        self.TextEmail = QtWidgets.QLineEdit(Form)
        self.TextEmail.setGeometry(QtCore.QRect(150, 140, 221, 31))
        self.TextEmail.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"}")
        self.TextEmail.setObjectName("TextEmail")
        self.TextPhone = QtWidgets.QLineEdit(Form)
        self.TextPhone.setGeometry(QtCore.QRect(150, 210, 151, 31))
        self.TextPhone.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"}")
        self.TextPhone.setObjectName("TextPhone")
        self.TextMsg = QtWidgets.QLineEdit(Form)
        self.TextMsg.setGeometry(QtCore.QRect(150, 280, 391, 111))
        self.TextMsg.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"}")
        self.TextMsg.setObjectName("TextMsg")
        self.labelName = QtWidgets.QLabel(Form)
        self.labelName.setGeometry(QtCore.QRect(30, 65, 61, 31))
        self.labelName.setStyleSheet("QLabel{\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"\n"
"")
        self.labelName.setObjectName("labelName")
        self.labelEmail = QtWidgets.QLabel(Form)
        self.labelEmail.setGeometry(QtCore.QRect(30, 140, 71, 31))
        self.labelEmail.setStyleSheet("QLabel{\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"\n"
"")
        self.labelEmail.setObjectName("labelEmail")
        self.labelPhone = QtWidgets.QLabel(Form)
        self.labelPhone.setGeometry(QtCore.QRect(30, 210, 91, 31))
        self.labelPhone.setStyleSheet("QLabel{\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"\n"
"")
        self.labelPhone.setObjectName("labelPhone")
        self.labelMsg = QtWidgets.QLabel(Form)
        self.labelMsg.setGeometry(QtCore.QRect(30, 280, 81, 31))
        self.labelMsg.setStyleSheet("QLabel{\n"
"color:white;\n"
"font-size:18px;\n"
"}\n"
"\n"
"")     
        self.labelMsg.setObjectName("labelMsg")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(330, 420, 111, 31))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:white;\n"
"color:black;\n"
"font-size:18px;\n"
"border-radius:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"color:white;\n"
"font-size:18px;\n"
"border-radius:10px;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.printtext)

        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelContact.setText(_translate("Form", "Contact Us "))
        self.labelName.setText(_translate("Form", "Name "))
        self.labelEmail.setText(_translate("Form", "E-mail"))
        self.labelPhone.setText(_translate("Form", "Phone No"))
        self.labelMsg.setText(_translate("Form", "Message "))
        self.pushButton.setText(_translate("Form", "Submit"))
       

    def printtext(self):
        Fname = self.TextFName.text()
        print ("First Name : ",Fname)
        Lname = self.TextLName.text()
        print ("Last Name : ",Lname)
        Email = self.TextEmail.text()
        print ("E-mail : ",Email)
        Phone = self.TextPhone.text()
        print ("Phone No : ",Phone)
        msg = self.TextMsg.text()
        print ("Message : ",msg)

        

        





import imges


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
