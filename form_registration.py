# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1180, 543)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 10, 511, 451))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox_5 = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_5)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox_6 = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_6)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox_7 = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setObjectName("comboBox_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_7)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBox_2 = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.formLayoutWidget)
        self.calendarWidget.setMaximumSize(QtCore.QSize(16777215, 165))
        self.calendarWidget.setObjectName("calendarWidget")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.calendarWidget)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1160, 0, 20, 851))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(580, 10, 541, 311))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(370, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBox_3 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.comboBox_4 = QtWidgets.QComboBox(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(580, 330, 541, 111))
        self.textBrowser.setMaximumSize(QtCore.QSize(550, 130))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1180, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Имя"))
        self.label_2.setText(_translate("MainWindow", "Отчество"))
        self.label_3.setText(_translate("MainWindow", "Фамилия"))
        self.label_7.setText(_translate("MainWindow", "Пол"))
        self.label_5.setText(_translate("MainWindow", "Дата рождения"))
        self.pushButton.setText(_translate("MainWindow", "Ввести данные"))
        self.label_6.setText(_translate("MainWindow", "Вес (1 - 200), кг"))
        self.label_4.setText(_translate("MainWindow", "KU (1 - 9)"))
        self.label_8.setText(_translate("MainWindow", "Вид соревнований"))
        self.label_9.setText(_translate("MainWindow", "Категория"))
        self.label_10.setText(_translate("MainWindow", "Результат"))
        self.pushButton_2.setText(_translate("MainWindow", "Подтвердить данные"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Нажимая кнопки</span><span style=\" font-size:12pt; font-weight:600;\"> Продолжить</span><span style=\" font-size:12pt;\"> и </span><span style=\" font-size:12pt; font-weight:600;\">Ок</span><span style=\" font-size:12pt;\">, я подтверждаю правильность внесенных мною данных, а также принимаю и поддерживаю политику конфеденциальности и сохранности личных данных согласно ФЗ 52</span></p></body></html>"))
        self.action.setText(_translate("MainWindow", "Сохранить"))
        self.action_2.setText(_translate("MainWindow", "Сохранить как"))
        self.action_3.setText(_translate("MainWindow", "Открыть"))
