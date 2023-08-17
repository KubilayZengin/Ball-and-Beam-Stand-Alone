from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget

import serial.tools.list_ports
import matplotlib.pyplot as plt
import numpy as np
import webbrowser
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(584, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.align_left()
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.acrome_label = QtWidgets.QLabel(self.centralwidget)
        self.acrome_label.setMaximumSize(QtCore.QSize(400, 100))
        self.acrome_label.setText("")
        self.acrome_label.setPixmap(QtGui.QPixmap("images/acrome.png"))
        self.acrome_label.setScaledContents(True)
        self.acrome_label.setObjectName("acrome_label")
        self.horizontalLayout_3.addWidget(self.acrome_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(400, 200))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/ball_and_beam.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 3, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 2, 1, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_2.addWidget(self.lineEdit_13, 3, 1, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 1, 1, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_2.addWidget(self.lineEdit_12, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(34, 22, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "background-color: #880808;\n"
                                        "border-image: url(:/test/images/step.png)\n"
                                        " }\n"
                                        "QPushButton:hover {\n"
                                        "background-color: #6b0808;\n"
                                        "}\n"
                                        "        \n"
                                        "")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "background-color: #880808;\n"
                                        "border-image:  url(:/test/images/sin.png)\n"
                                        " }\n"
                                        "QPushButton:hover {\n"
                                        "background-color: #6b0808;\n"
                                        "}\n"
                                        "        \n"
                                        "")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "background-color: #880808;\n"
                                        "border-image:  url(:/test/images/ramp.png)\n"
                                        " }\n"
                                        "QPushButton:hover {\n"
                                        "background-color: #6b0808;\n"
                                        "}\n"
                                        "        \n"
                                        "")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.verticalLayout_6.addWidget(self.lineEdit_15)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.verticalLayout_6.addWidget(self.lineEdit_16)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setScaledContents(False)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.horizontalLayout_5.addWidget(self.lineEdit_14)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem12 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QtCore.QSize(150, 100))
        self.startButton.setMaximumSize(QtCore.QSize(180, 150))
        self.startButton.setMouseTracking(True)
        self.startButton.setAcceptDrops(False)
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("QPushButton {\n"
                                       "border-radius: 50%;"
                                       "border-image:  url(:/test/images/start.png)\n"
                                       " }\n"

                                       "QPushButton:hover {\n"
                                       "background-color: rgba(115,210,22,255);\n"
                                       "border-radius: 62px;\n"
                                       "}\n"
                                       "        ")
        self.startButton.setText("")
        self.startButton.setCheckable(True)
        self.startButton.setAutoDefault(False)
        self.startButton.setObjectName("startButton")
        self.verticalLayout_4.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setMinimumSize(QtCore.QSize(150, 100))
        self.stopButton.setMaximumSize(QtCore.QSize(180, 150))
        self.stopButton.setStyleSheet("QPushButton {\n"
                                      "border-radius: 50%;"
                                      "border-image: url(:/test/images/stop.png)\n"
                                      " }\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgb(224, 27, 36);\n"
                                      "border-radius: 62px;\n"
                                      "}\n"
                                      "        \n"
                                      "")
        self.stopButton.setText("")
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout_4.addWidget(self.stopButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem13 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPorts = QtWidgets.QMenu(self.menubar)
        self.menuPorts.setObjectName("menuPorts")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionProduct_Page = QtWidgets.QAction(MainWindow)
        self.actionProduct_Page.setObjectName("actionProduct_Page ")
        self.actionProduct_Page.triggered.connect(lambda: self.website('https://acrome.net/product/ball-and-beam'))
        self.actionTroubleshooting = QtWidgets.QAction(MainWindow)
        self.actionTroubleshooting.setObjectName("actionTroubleshooting")
        self.actionVisit_acrome_net = QtWidgets.QAction(MainWindow)
        self.actionVisit_acrome_net.setObjectName("actionVisit_acrome_net")
        self.actionVisit_acrome_net.triggered.connect(lambda: self.website('https://acrome.net/'))
        self.actionPrivacy_Policy = QtWidgets.QAction(MainWindow)
        self.actionPrivacy_Policy.setObjectName("actionPrivacy_Policy")
        self.actionPrivacy_Policy.triggered.connect(lambda: self.website('https://acrome.net/privacy-policy'))
        self.actionCheck_for_Updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_Updates.setObjectName("actionCheck_for_Updates")
        self.actionAbout_Acrome = QtWidgets.QAction(MainWindow)
        self.actionAbout_Acrome.setObjectName("actionAbout_Acrome")
        self.actionAbout_Acrome.triggered.connect(lambda: self.website('https://acrome.net/about-acrome'))
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionProduct_Page)
        self.menuHelp.addAction(self.actionTroubleshooting)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionVisit_acrome_net)
        self.menuHelp.addAction(self.actionPrivacy_Policy)
        self.menuHelp.addAction(self.actionCheck_for_Updates)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Acrome)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPorts.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Acrome Ball and Beam"))
        self.label_9.setText(_translate("MainWindow", "Kd"))
        self.label_6.setText(_translate("MainWindow", "Kp"))
        self.label_8.setText(_translate("MainWindow", "Ki"))
        self.label_5.setText(_translate("MainWindow", "Position\n"
                                                      "Control"))
        self.label_4.setText(_translate("MainWindow", "Velocity\n"
                                                      "Control"))
        self.label_7.setText(_translate("MainWindow", "Kp"))
        self.label_10.setText(_translate("MainWindow", "Kd"))
        self.label_11.setText(_translate("MainWindow", "Ki"))
        self.label.setText(_translate("MainWindow", "Amplitude:"))
        self.label_2.setText(_translate("MainWindow", "Frequency:"))
        self.label_12.setText(_translate("MainWindow", "Stop Time"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPorts.setTitle(_translate("MainWindow", "Ports"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionSave_As.setStatusTip(_translate("MainWindow", "Save As"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionPreferences.setStatusTip(_translate("MainWindow", "Preferences"))
        self.actionPreferences.setShortcut(_translate("MainWindow", "Ctrl+,"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "Exits Program"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionProduct_Page.setText(_translate("MainWindow", "Product Page "))
        self.actionProduct_Page.setStatusTip(_translate("MainWindow", "Visit Product_Page "))
        self.actionTroubleshooting.setText(_translate("MainWindow", "Troubleshooting"))
        self.actionTroubleshooting.setStatusTip(_translate("MainWindow", "See Troubleshooting"))
        self.actionVisit_acrome_net.setText(_translate("MainWindow", "Visit acrome.net"))
        self.actionVisit_acrome_net.setStatusTip(_translate("MainWindow", "Visit our Website"))
        self.actionPrivacy_Policy.setText(_translate("MainWindow", "Privacy Policy"))
        self.actionPrivacy_Policy.setStatusTip(_translate("MainWindow", "Visit Privacy Policy Page"))
        self.actionCheck_for_Updates.setText(_translate("MainWindow", "Check for Updates"))
        self.actionCheck_for_Updates.setStatusTip(_translate("MainWindow", "Check for Updates"))
        self.actionAbout_Acrome.setText(_translate("MainWindow", "About Acrome"))
        self.actionAbout_Acrome.setStatusTip(_translate("MainWindow", "Visit About Acrome Page"))

        # Button functions
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)

        # Detect all available COMs
        com_list = serial.tools.list_ports.comports()
        available_coms = []

        if len(com_list) == 0:
            available_coms.append("None")
            self.message("No available COM port detected.\n Check USB connection.", QMessageBox.Warning)
        else:
            for element in com_list:
                available_coms.append(element.device)

        for i in available_coms:
            # Add available COMs to ports menu bar.
            action = self.menuPorts.addAction(i)
            # Save actions to use later
            action.triggered.connect(lambda _, port=i: self.port_selected(port))

        # Image assignments
        pixmap = QPixmap("images/start.png")
        pixmap2 = QPixmap("images/stop.png")
        pixmap3 = QPixmap("images/step.png")
        pixmap4 = QPixmap("images/sin.png")
        pixmap5 = QPixmap("images/ramp.png")

        pixmap = pixmap.scaled(151, 111)
        pixmap2 = pixmap2.scaled(151, 111)
        pixmap3 = pixmap3.scaled(75, 75)
        pixmap4 = pixmap4.scaled(75, 75)
        pixmap5 = pixmap5.scaled(75, 75)

        icon = QIcon(pixmap)
        icon2 = QIcon(pixmap2)
        icon3 = QIcon(pixmap3)
        icon4 = QIcon(pixmap4)
        icon5 = QIcon(pixmap5)

        self.startButton.setIcon(icon)
        self.startButton.setIconSize(pixmap.size())

        self.stopButton.setIcon(icon2)
        self.stopButton.setIconSize(pixmap2.size())

        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(pixmap3.size())

        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(pixmap4.size())

        self.pushButton_4.setIcon(icon5)
        self.pushButton_4.setIconSize(pixmap5.size())

    # Real time data plotter function
    def start(self):
        # Check whether the PID input is empty
        '''
        try:
            kp = float(self.entry_3.get())
            ki = float(self.entry_4.get())
            kd = float(self.entry_5.get())
            # Initialize the PID controller with entered gains
            # self.pid_controller = PID.PIDController(kp, ki, kd)
        except ValueError:
            print("Enter any value for PID gains.")
        except UnboundLocalError:
            print("Enter any value for PID gains.")
        except NameError:
            print("Enter any value for PID gains.")
        '''
        # Define the set point (desired position)
        # set_point = 50.0
        # Create an empty array for incoming data
        data = np.array([])
        # Create an empty array for time stamps
        timestamps = np.array([])
        # Set figure size
        plt.rcParams["figure.figsize"] = (8, 7)
        # Create a subplot with size of 1x1
        fig, ax = plt.subplots(1, 1)
        # Call set_plot_position function
        self.set_plot_position(fig, 850, 145)

        try:
            self.time_selected = float(self.lineEdit_14.text())
            self.real_time = 0
        except ValueError:
            self.message("Enter valid value for the stop time.", QMessageBox.Critical)
        k = True

        while k:
            try:
                # Read serial data
                byte_data = self.arduino.readline()
                # Read ball position in terms of mm
                position_data = float(byte_data.decode().strip())
                '''
                    # Calculate the control signal using the PID controller and the analog value as the set point
                    control_signal = self.pid_controller.calculate(set_point, position_data)
                    # Send the control signal to Arduino
                    self.set_servo_angle(control_signal)
                '''
                # Append data and timestamp to arrays
                data = np.append(data, position_data)
                timestamps = np.append(timestamps, time.time())  # Add the current time as the x-coordinate

                if self.time_selected <= float(self.real_time):
                    k = False

                else:
                    # Calculate real-time seconds for each data point
                    realtime = timestamps - timestamps[0]
                    self.real_time = realtime[-1]
                    plt.cla()
                    plt.grid()
                    plt.ylim(0, 90)
                    plt.plot(realtime, data, color="red")
                    plt.title("Ball Position vs Real Time")
                    plt.ylabel("Position (mm)")
                    plt.xlabel("Time (s)")
                    plt.pause(0.01)

            except KeyboardInterrupt:
                # If the user presses Ctrl+F2 or manually stops, terminate the program.
                self.message("Program terminated.", QMessageBox.Information)
            except AttributeError:
                self.message("Select your COM Port.", QMessageBox.Critical)
                plt.close()
                break
            except serial.SerialException:
                # Handle SerialException error when opening the port
                self.message("Error: Unable to open the serial port. \n"
                             "Check the port number and connection or restart the program.", QMessageBox.Warning)
            except ValueError:
                # If ValueError occurs, continue to the next iteration to read the next line.
                continue
            except NameError:
                break

    def website(self, i):
        webbrowser.open(i)

    def message(self, i, type):
        msg = QMessageBox()
        msg.setWindowTitle("Attention")
        msg.setText(i)
        # Parameters: Critical Warning Information Question
        msg.setIcon(type)
        x = msg.exec_()

    def port_selected(self, port):
        self.selected_port = port
        # Call set.com() function to initialize serial communication
        self.set_com()

    def set_com(self):
        # Initialize the serial communication between Arduino and Python.
        try:
            self.arduino = serial.Serial(self.selected_port, 9600, timeout=0.05)
            # Move servo to initial position
            self.arduino.write(30)
            self.message("Connected to " + self.selected_port, QMessageBox.Information)
        except serial.SerialException:
            self.message("Unable to connect.", QMessageBox.Critical)

    # Plot starting coordinates function
    @staticmethod
    def set_plot_position(f, x, y):
        # Move figure's upper left corner to pixel (x, y)
        backend = plt.get_backend()
        if backend == 'TkAgg':
            f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
        elif backend == 'WXAgg':
            f.canvas.manager.window.SetPosition((x, y))
        else:
            f.canvas.manager.window.move(x, y)

    '''
    def align_left(self):
        frame_geometry = MainWindow.frameGeometry()
        frame_geometry.moveLeft(200)  # Burada 100 değeri istediğiniz kaydırma miktarını temsil eder
        frame_geometry.moveTop(100)
        MainWindow.move(frame_geometry.topLeft())
    '''

    def stop(self):
        self.message("Program Terminated.", QMessageBox.Information)
        exit(0)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
