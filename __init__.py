# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from time import strftime
from PyQt5.QtCore import QTime, QTimer
import time
import regex

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.i = 0 
        self.value_ = 1
        self.stopwatch_paused = False
        self.TimerPaused = False
        self.timer_value = 10
        self.timer_value_original = 100
        self.timer_beep = False

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(528, 422)
        MainWindow.setWindowIcon(QtGui.QIcon("logo.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdStopwatch = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdStopwatch.setGeometry(QtCore.QRect(10, 30, 191, 61))
        self.lcdStopwatch.setSmallDecimalPoint(False)
        self.lcdStopwatch.setDigitCount(6)
        self.lcdStopwatch.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdStopwatch.setProperty("intValue", 0)
        self.lcdStopwatch.setObjectName("lcdStopwatch")
        self.lcdTimer = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdTimer.setGeometry(QtCore.QRect(10, 200, 191, 61))
        self.lcdTimer.setSmallDecimalPoint(False)
        self.lcdTimer.setDigitCount(6)
        self.lcdTimer.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdTimer.setProperty("intValue", 0)
        self.lcdTimer.setObjectName("lcdTimer")
        self.pbTimer = QtWidgets.QProgressBar(self.centralwidget)
        self.pbTimer.setGeometry(QtCore.QRect(10, 270, 191, 23))
        self.pbTimer.setProperty("value", 24)
        self.pbTimer.setObjectName("pbTimer")
        self.bStopwatchNew = QtWidgets.QPushButton(self.centralwidget)
        self.bStopwatchNew.setGeometry(QtCore.QRect(10, 100, 86, 26))
        self.bStopwatchNew.setObjectName("bStopwatchNew")
        self.bStopwatchPause = QtWidgets.QPushButton(self.centralwidget)
        self.bStopwatchPause.setGeometry(QtCore.QRect(110, 100, 86, 26))
        self.bStopwatchPause.setObjectName("bStopwatchPause")
        self.bTimerSave = QtWidgets.QPushButton(self.centralwidget)
        self.bTimerSave.setGeometry(QtCore.QRect(110, 130, 86, 26))
        self.bTimerSave.setObjectName("bTimerSave")
        self.lcdClock = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdClock.setGeometry(QtCore.QRect(10, 350, 191, 61))
        self.lcdClock.setSmallDecimalPoint(False)
        self.lcdClock.setDigitCount(8)
        self.lcdClock.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdClock.setProperty("intValue", 0)
        self.lcdClock.setObjectName("lcdClock")
        self.tTimerTime = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.tTimerTime.setGeometry(QtCore.QRect(210, 200, 181, 26))
        self.tTimerTime.setObjectName("tTimerTime")
        self.bTimerReset = QtWidgets.QPushButton(self.centralwidget)
        self.bTimerReset.setGeometry(QtCore.QRect(310, 260, 86, 26))
        self.bTimerReset.setObjectName("bTimerReset")
        self.bTimerStart = QtWidgets.QPushButton(self.centralwidget)
        self.bTimerStart.setGeometry(QtCore.QRect(210, 230, 86, 26))
        self.bTimerStart.setObjectName("bTimerStart")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 521, 171))
        self.groupBox.setObjectName("groupBox")
        self.tTimeout = QtWidgets.QPlainTextEdit(self.groupBox)
        self.tTimeout.setGeometry(QtCore.QRect(210, 30, 141, 131))
        self.tTimeout.setReadOnly(True)
        self.tTimeout.setObjectName("tTimeout")
        self.tTimeValue = QtWidgets.QPlainTextEdit(self.groupBox)
        self.tTimeValue.setGeometry(QtCore.QRect(360, 30, 61, 131))
        self.tTimeValue.setReadOnly(True)
        self.tTimeValue.setPlainText("")
        self.tTimeValue.setObjectName("tTimeValue")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 170, 521, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(400, 30, 121, 51))
        self.label.setScaledContents(False)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.bBeep = QtWidgets.QCheckBox(self.groupBox_2)
        self.bBeep.setGeometry(QtCore.QRect(210, 130, 181, 24))
        self.bBeep.setObjectName("bBeep")
        self.bTimerPause = QtWidgets.QPushButton(self.groupBox_2)
        self.bTimerPause.setGeometry(QtCore.QRect(310, 60, 86, 26))
        self.bTimerPause.setObjectName("bTimerPause")
        self.bStopwatchSave = QtWidgets.QPushButton(self.centralwidget)
        self.bStopwatchSave.setGeometry(QtCore.QRect(430, 30, 86, 26))
        self.bStopwatchSave.setObjectName("bStopwatchSave")
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.lcdTimer.raise_()
        self.pbTimer.raise_()
        self.bStopwatchNew.raise_()
        self.bStopwatchPause.raise_()
        self.bTimerSave.raise_()
        self.lcdClock.raise_()
        self.tTimerTime.raise_()
        self.bTimerReset.raise_()
        self.bTimerStart.raise_()
        self.bStopwatchSave.raise_()
        self.lcdStopwatch.raise_()

        self.bStopwatchNew.clicked.connect(self.StartTimer)
        self.bStopwatchNew.clicked.connect(self.NewStopwatch)
        self.bStopwatchNew.clicked.connect(self.ResetStopwatch)
        self.bStopwatchPause.clicked.connect(self.PauseStopwatch)
        self.bTimerSave.clicked.connect(self.UnpauseStopwatch)
        self.bStopwatchSave.clicked.connect(self.ClearStopwatch)
        self.bTimerStart.clicked.connect(self.TimerStart)
        self.bTimerPause.clicked.connect(self.TimerPause)
        self.bTimerReset.clicked.connect(self.TimerReset)
        self.bBeep.stateChanged.connect(self.changeBeep)
        self.bBeep.setEnabled(False)

        self.tTimerTime.setPlainText("60")
        self.tTimeout.verticalScrollBar().valueChanged.connect(
            self.tTimeValue.verticalScrollBar().setValue)
        self.tTimeValue.verticalScrollBar().valueChanged.connect(
            self.tTimeout.verticalScrollBar().setValue)
        self.tTimeout.verticalScrollBar().setStyleSheet("QScrollBar {width:0px;}");
        #self.tTimerTime.verticalScrollBar().setStyleSheet("QScrollBar {width:0px;}");
        self.timer = QtCore.QTimer(MainWindow)
        self.timer.timeout.connect(self.Time)
        self.timer.start(100)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timer"))
        self.bStopwatchNew.setText(_translate("MainWindow", "New"))
        self.bStopwatchPause.setText(_translate("MainWindow", "Pause"))
        self.bTimerSave.setText(_translate("MainWindow", "Unpause"))
        self.bTimerReset.setText(_translate("MainWindow", "Unpause"))
        self.bTimerStart.setText(_translate("MainWindow", "Start"))
        self.groupBox.setTitle(_translate("MainWindow", "Stopwatch"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Timer"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Note: Write time</p><p>in seconds!</p></body></html>"))
        self.bBeep.setText(_translate("MainWindow", "Beep when done"))
        self.bTimerPause.setText(_translate("MainWindow", "Pause"))
        self.bStopwatchSave.setText(_translate("MainWindow", "Clear Output"))

    def TimerStart(self):
        self.TimerActivate = self.tTimerTime.toPlainText()
        self.TimerActivate = list(self.TimerActivate)
        self.TimerActivate = [s.strip("x") for s in self.TimerActivate]
        self.TimerActivate = "".join(map(str,self.TimerActivate))
        #print(self.TimerActivate)
        if len(self.TimerActivate) > 1: 
            if bool(regex.match('[\d/-]+$', self.TimerActivate)) == True:
                if self.TimerActivate != "0":
                    self.TimerPaused = False
                    self.timer_value = float(self.TimerActivate)
                    self._Timer_ = QTimer()
                    self._Timer_.timeout.connect(self.TimerBegin)
                    self._Timer_.start(1)
                    #self.timer_value = self.timer_value - 1
                    self.timer_value_original = int(self.timer_value)
            
    def TimerBegin(self):
        self.lcdTimer.display(self.timer_value)
        if self.TimerPaused == False:
            self.timer_value = self.timer_value-0.001
            if self.TimerActivate != "0":
                self.pbTimer.setValue((self.timer_value/self.timer_value_original)*100)
        
        if self.timer_value <= float(0):
            self.TimerPaused = True
            self.timer_value = float(0)
            if self.timer_beep == True:
                playsound("pacman_extrapac.wav")

    def changeBeep(self):
        if self.bBeep.isChecked():
            self.timer_beep = True
        else:
            self.timer_beep = False

    def StartTimer(self):
        self.stopwatch_paused = False
        self.Stopwatch_ = QTimer()
        self.Stopwatch_.timeout.connect(self.Timer_)
        self.Stopwatch_.start(1)

    def Timer_(self):
        self.lcdStopwatch.display(self.i)
        if self.stopwatch_paused == False:
            self.i = self.i+0.001

    def TimerPause(self):
        self.TimerPaused = True

    def ResetStopwatch(self):
        self.value_ = 1

    def TimerReset(self):
        self.TimerPaused = False
        #self.tTimerTime.setPlainText("60")
        #self.timer_value = float(0)

    def ClearStopwatch(self):
        self.value_ = 1
        self.tTimeout.setPlainText("")
        self.tTimeValue.setPlainText("")

    def Time(self):
        self.lcdClock.display(strftime("%H"+":"+"%M"+":"+"%S"))  

    def NewStopwatch(self):
        self.i = 0
        self.PauseStopwatch = False
        self.lcdStopwatch.display(self.i)

    def PauseStopwatch(self):
        if self.stopwatch_paused == False:
            self.stopwatch_paused = True
            #print(self.i)
            self.tTimeout.insertPlainText(str(self.i)+"\n")
            self.tTimeValue.insertPlainText("V:"+str(self.value_)+"\n")
            self.value_ = self.value_ + 1

    def UnpauseStopwatch(self):
        self.stopwatch_paused = False
        self.StartTimer()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())