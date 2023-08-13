from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMessageBox

import serial.tools.list_ports
import matplotlib.pyplot as plt
import numpy as np
import webbrowser
import time

class Ui_BallandBeam(object):
    def setupUi(self, BallandBeam):
        BallandBeam.setObjectName("BallandBeam")
        BallandBeam.resize(500, 850)
        self.centralwidget = QtWidgets.QWidget(BallandBeam)
        self.centralwidget.setObjectName("centralwidget")
        self.acrome_label = QtWidgets.QLabel(self.centralwidget)
        self.acrome_label.setGeometry(QtCore.QRect(90, 20, 311, 81))
        self.acrome_label.setText("")
        self.acrome_label.setPixmap(QtGui.QPixmap("images/acrome.png"))
        self.acrome_label.setScaledContents(True)
        self.acrome_label.setObjectName("acrome_label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(285, 250, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(180, 630, 121, 91))
        self.startButton.setMouseTracking(False)
        self.startButton.setAcceptDrops(False)
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("border-radius: 50%; border-image:  url(:/test/images/start.png)")
        self.startButton.setText("")
        self.startButton.setCheckable(True)
        self.startButton.setAutoDefault(False)
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(180, 720, 121, 91))
        self.stopButton.setStyleSheet("border-radius: 50%; border-image: url(:/test/images/stop.png)\n")
        self.stopButton.setText("")
        self.stopButton.setObjectName("stopButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(280, 300, 75, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(280, 330, 75, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(280, 360, 75, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 420, 85, 85))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color: #880808;\n"
                                        "border-image: url(:/test/images/step.png)\n")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 420, 85, 85))
        self.pushButton_3.setStyleSheet("background-color: #880808;\n"
                                        "border-image:  url(:/test/images/sin.png)")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 420, 85, 85))
        self.pushButton_4.setStyleSheet("background-color: #880808;\n"
                                        "border-image:  url(:/test/images/ramp.png)")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(160, 300, 75, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(160, 330, 75, 25))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(160, 360, 75, 25))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 250, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 550, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setScaledContents(False)
        self.label_7.setObjectName("label_7")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(305, 585, 75, 25))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 550, 91, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 590, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(200, 550, 85, 25))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(200, 585, 85, 25))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 110, 251, 131))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/ball_and_beam.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        BallandBeam.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BallandBeam)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        self.menuF_le = QtWidgets.QMenu(self.menubar)
        self.menuF_le.setObjectName("menuF_le")
        self.menuTool = QtWidgets.QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        BallandBeam.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BallandBeam)
        self.statusbar.setObjectName("statusbar")
        BallandBeam.setStatusBar(self.statusbar)
        self.actionAbout_Acrome = QtWidgets.QAction(BallandBeam)
        self.actionAbout_Acrome.setObjectName("actionAbout_Acrome")
        self.actionAbout_Acrome.triggered.connect(lambda: self.website('https://acrome.net/about-acrome'))
        self.actionPorts = QtWidgets.QAction(BallandBeam)
        self.actionPorts.setObjectName("actionPorts")
        self.actionVisit_Acrome_com = QtWidgets.QAction(BallandBeam)
        self.actionVisit_Acrome_com.setObjectName("actionVisit_Acrome_com")
        self.actionVisit_Acrome_com.triggered.connect(lambda: self.website('https://acrome.net/'))
        self.actionPrivacy_Policy = QtWidgets.QAction(BallandBeam)
        self.actionPrivacy_Policy.setObjectName("actionPrivacy_Policy")
        self.actionProduct_Page = QtWidgets.QAction(BallandBeam)
        self.actionProduct_Page.setObjectName("actionProduct_Page")
        self.actionProduct_Page.triggered.connect(lambda: self.website('https://acrome.net/product/ball-and-beam'))
        self.actionTroubleshooting = QtWidgets.QAction(BallandBeam)
        self.actionTroubleshooting.setObjectName("actionTroubleshooting")
        self.actionUndo = QtWidgets.QAction(BallandBeam)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(BallandBeam)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QtWidgets.QAction(BallandBeam)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(BallandBeam)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(BallandBeam)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSelect_All = QtWidgets.QAction(BallandBeam)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionClose = QtWidgets.QAction(BallandBeam)
        self.actionClose.setObjectName("actionClose")
        self.actionSave = QtWidgets.QAction(BallandBeam)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(BallandBeam)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionPreferences = QtWidgets.QAction(BallandBeam)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionCheck_for_Updates = QtWidgets.QAction(BallandBeam)
        self.actionCheck_for_Updates.setObjectName("actionCheck_for_Updates")
        self.menuF_le.addAction(self.actionSave)
        self.menuF_le.addAction(self.actionSave_As)
        self.menuF_le.addSeparator()
        self.menuF_le.addAction(self.actionPreferences)
        self.menuF_le.addSeparator()
        self.menuF_le.addAction(self.actionClose)
        self.menuAbout.addAction(self.actionProduct_Page)
        self.menuAbout.addAction(self.actionTroubleshooting)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionVisit_Acrome_com)
        self.menuAbout.addAction(self.actionPrivacy_Policy)
        self.menuAbout.addAction(self.actionCheck_for_Updates)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_Acrome)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menubar.addAction(self.menuF_le.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 300, 21, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 330, 21, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(130, 360, 21, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(250, 300, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(250, 360, 21, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(250, 330, 21, 17))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.retranslateUi(BallandBeam)
        QtCore.QMetaObject.connectSlotsByName(BallandBeam)

    def retranslateUi(self, BallandBeam):
        _translate = QtCore.QCoreApplication.translate
        BallandBeam.setWindowTitle(_translate("BallandBeam", "Acrome Ball and Beam"))
        self.label_4.setText(_translate("BallandBeam", "Velocity\n"
                                                       "Control"))
        self.label_5.setText(_translate("BallandBeam", "Position\n"
                                                       "Control"))
        self.label_7.setText(_translate("BallandBeam", "Stop Time"))
        self.label.setText(_translate("BallandBeam", "Amplitude:"))
        self.label_2.setText(_translate("BallandBeam", "Frequency:"))
        self.menuF_le.setTitle(_translate("BallandBeam", "File"))
        self.menuTool.setTitle(_translate("BallandBeam", "Ports"))
        self.menuAbout.setTitle(_translate("BallandBeam", "Help"))
        self.menuEdit.setTitle(_translate("BallandBeam", "Edit"))
        self.actionAbout_Acrome.setText(_translate("BallandBeam", "About Acrome"))
        self.actionPorts.setText(_translate("BallandBeam", "Port"))
        self.actionVisit_Acrome_com.setText(_translate("BallandBeam", "Visit acrome.net"))
        self.actionPrivacy_Policy.setText(_translate("BallandBeam", "Privacy Policy"))
        self.actionProduct_Page.setText(_translate("BallandBeam", "Product Page"))
        self.actionTroubleshooting.setText(_translate("BallandBeam", "Troubleshooting"))
        self.actionUndo.setText(_translate("BallandBeam", "Undo"))
        self.actionUndo.setShortcut(_translate("BallandBeam", "Ctrl+Z"))
        self.actionRedo.setText(_translate("BallandBeam", "Redo"))
        self.actionRedo.setShortcut(_translate("BallandBeam", "Ctrl+Shift+Z"))
        self.actionCut.setText(_translate("BallandBeam", "Cut"))
        self.actionCut.setShortcut(_translate("BallandBeam", "Ctrl+X"))
        self.actionCopy.setText(_translate("BallandBeam", "Copy"))
        self.actionCopy.setShortcut(_translate("BallandBeam", "Ctrl+C"))
        self.actionPaste.setText(_translate("BallandBeam", "Paste"))
        self.actionPaste.setShortcut(_translate("BallandBeam", "Ctrl+V"))
        self.actionSelect_All.setText(_translate("BallandBeam", "Select All"))
        self.actionSelect_All.setShortcut(_translate("BallandBeam", "Ctrl+A"))
        self.actionClose.setText(_translate("BallandBeam", "Quit"))
        self.actionClose.setShortcut(_translate("BallandBeam", "Ctrl+Q"))
        self.actionSave.setText(_translate("BallandBeam", "Save"))
        self.actionSave.setShortcut(_translate("BallandBeam", "Ctrl+S"))
        self.actionSave_As.setText(_translate("BallandBeam", "Save As..."))
        self.actionSave_As.setShortcut(_translate("BallandBeam", "Ctrl+Shift+S"))
        self.actionPreferences.setText(_translate("BallandBeam", "Preferences"))
        self.actionPreferences.setShortcut(_translate("BallandBeam", "Ctrl+,"))
        self.actionCheck_for_Updates.setText(_translate("BallandBeam", "Check for Updates"))

        self.label_6.setText(_translate("BallandBeam", "Kp"))
        self.label_8.setText(_translate("BallandBeam", "Ki"))
        self.label_9.setText(_translate("BallandBeam", "Kd"))
        self.label_10.setText(_translate("BallandBeam", "Kp"))
        self.label_11.setText(_translate("BallandBeam", "Kd"))
        self.label_12.setText(_translate("BallandBeam", "Ki"))

        # Button functions
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)

        # Detect all available COMs
        com_list = serial.tools.list_ports.comports()
        available_coms = []
        if len(com_list) == 0:
            available_coms.append("None")
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("No available COM port detected.\n Check USB connection.")
            # Parameters: Critical Warning Information Question
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
        else:
            for element in com_list:
                available_coms.append(element.device)

        for i in available_coms:
            self.menuTool.addAction(i)

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
            self.time_selected = float(self.lineEdit_11.text())
            self.real_time = 0
        except ValueError:
            print("Enter valid value for the stop time.")
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

                if self.time_selected <= int(self.real_time):
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
                print("Program terminated.")
            except AttributeError:
                print("Select your COM Port.")
                plt.close()
                break
            except serial.SerialException:
                # Handle SerialException error when opening the port
                print("Error: Unable to open the serial port. \n"
                      "Check the port number and connection or restart the program.")
            except ValueError:
                # If ValueError occurs, continue to the next iteration to read the next line.
                continue
            except NameError:
                break

    def website(self, i):
        webbrowser.open(i)

    def set_com(self):
        # Initialize the serial communication between Arduino and Python.
        try:
            self.arduino = serial.Serial(self.actionPorts.text(), 9600, timeout=0.05)
            # Move servo to initial position
            self.arduino.write(30)
            print("Connected to", self.actionPorts.text())
        except serial.SerialException:
            print("Unable to connect.")

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

    def stop(self):
        print("Program Terminated.")
        exit(0)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    BallandBeam = QtWidgets.QMainWindow()
    ui = Ui_BallandBeam()
    ui.setupUi(BallandBeam)
    BallandBeam.show()
    sys.exit(app.exec_())
