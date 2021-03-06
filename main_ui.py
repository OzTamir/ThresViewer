# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created: Wed Jan 22 19:54:50 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from VideoWidget import VideoWidget as QVid

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(545, 315)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.video = QVid(self.centralwidget)
        self.video.setGeometry(QtCore.QRect(120, 10, 320, 240))
        self.video.setAutoFillBackground(False)
        self.video.setObjectName(_fromUtf8("video"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 290, 641, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.setThreshold = QtGui.QPushButton(self.centralwidget)
        self.setThreshold.setGeometry(QtCore.QRect(230, 260, 98, 27))
        self.setThreshold.setObjectName(_fromUtf8("setThreshold"))
        self.color_picker = QtGui.QLabel(self.centralwidget)
        self.color_picker.setGeometry(QtCore.QRect(180, 310, 351, 111))
        self.color_picker.setMouseTracking(False)
        self.color_picker.setText(_fromUtf8(""))
        self.color_picker.setPixmap(QtGui.QPixmap(_fromUtf8("hsv.jpg")))
        self.color_picker.setScaledContents(True)
        self.color_picker.setObjectName(_fromUtf8("color_picker"))
        self.h_lbl = QtGui.QLabel(self.centralwidget)
        self.h_lbl.setGeometry(QtCore.QRect(180, 420, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.h_lbl.setFont(font)
        self.h_lbl.setScaledContents(True)
        self.h_lbl.setObjectName(_fromUtf8("h_lbl"))
        self.hue = QtGui.QSlider(self.centralwidget)
        self.hue.setGeometry(QtCore.QRect(200, 420, 331, 29))
        self.hue.setMaximum(180)
        self.hue.setSingleStep(5)
        self.hue.setOrientation(QtCore.Qt.Horizontal)
        self.hue.setObjectName(_fromUtf8("hue"))
        self.value = QtGui.QSlider(self.centralwidget)
        self.value.setGeometry(QtCore.QRect(150, 310, 29, 91))
        self.value.setMaximum(255)
        self.value.setSingleStep(5)
        self.value.setOrientation(QtCore.Qt.Vertical)
        self.value.setObjectName(_fromUtf8("value"))
        self.v_lbl = QtGui.QLabel(self.centralwidget)
        self.v_lbl.setGeometry(QtCore.QRect(160, 400, 21, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.v_lbl.setFont(font)
        self.v_lbl.setScaledContents(True)
        self.v_lbl.setObjectName(_fromUtf8("v_lbl"))
        self.hue_label = QtGui.QLabel(self.centralwidget)
        self.hue_label.setGeometry(QtCore.QRect(0, 320, 41, 20))
        self.hue_label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.hue_label.setFrameShadow(QtGui.QFrame.Plain)
        self.hue_label.setMidLineWidth(2)
        self.hue_label.setObjectName(_fromUtf8("hue_label"))
        self.sat_label = QtGui.QLabel(self.centralwidget)
        self.sat_label.setGeometry(QtCore.QRect(0, 350, 41, 21))
        self.sat_label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sat_label.setFrameShadow(QtGui.QFrame.Plain)
        self.sat_label.setMidLineWidth(2)
        self.sat_label.setObjectName(_fromUtf8("sat_label"))
        self.value_label = QtGui.QLabel(self.centralwidget)
        self.value_label.setGeometry(QtCore.QRect(0, 380, 41, 20))
        self.value_label.setFrameShape(QtGui.QFrame.StyledPanel)
        self.value_label.setFrameShadow(QtGui.QFrame.Plain)
        self.value_label.setMidLineWidth(2)
        self.value_label.setObjectName(_fromUtf8("value_label"))
        self.min_check = QtGui.QCheckBox(self.centralwidget)
        self.min_check.setGeometry(QtCore.QRect(6, 420, 111, 22))
        self.min_check.setChecked(True)
        self.min_check.setObjectName(_fromUtf8("min_check"))
        self.max_check = QtGui.QCheckBox(self.centralwidget)
        self.max_check.setGeometry(QtCore.QRect(6, 440, 111, 22))
        self.max_check.setObjectName(_fromUtf8("max_check"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(140, 300, 20, 181))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.h_min_lbl = QtGui.QLabel(self.centralwidget)
        self.h_min_lbl.setGeometry(QtCore.QRect(50, 320, 31, 17))
        self.h_min_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.h_min_lbl.setObjectName(_fromUtf8("h_min_lbl"))
        self.s_min_lbl = QtGui.QLabel(self.centralwidget)
        self.s_min_lbl.setGeometry(QtCore.QRect(50, 350, 31, 17))
        self.s_min_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.s_min_lbl.setObjectName(_fromUtf8("s_min_lbl"))
        self.v_min_lbl = QtGui.QLabel(self.centralwidget)
        self.v_min_lbl.setGeometry(QtCore.QRect(50, 380, 31, 17))
        self.v_min_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.v_min_lbl.setObjectName(_fromUtf8("v_min_lbl"))
        self.h_max_lbl = QtGui.QLabel(self.centralwidget)
        self.h_max_lbl.setGeometry(QtCore.QRect(90, 320, 31, 17))
        self.h_max_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.h_max_lbl.setObjectName(_fromUtf8("h_max_lbl"))
        self.s_max_lbl = QtGui.QLabel(self.centralwidget)
        self.s_max_lbl.setGeometry(QtCore.QRect(90, 350, 31, 17))
        self.s_max_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.s_max_lbl.setObjectName(_fromUtf8("s_max_lbl"))
        self.v_max_lbl = QtGui.QLabel(self.centralwidget)
        self.v_max_lbl.setGeometry(QtCore.QRect(90, 380, 31, 17))
        self.v_max_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.v_max_lbl.setObjectName(_fromUtf8("v_max_lbl"))
        self.s_lbl = QtGui.QLabel(self.centralwidget)
        self.s_lbl.setGeometry(QtCore.QRect(180, 440, 16, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.s_lbl.setFont(font)
        self.s_lbl.setScaledContents(True)
        self.s_lbl.setObjectName(_fromUtf8("s_lbl"))
        self.sat = QtGui.QSlider(self.centralwidget)
        self.sat.setGeometry(QtCore.QRect(200, 440, 331, 29))
        self.sat.setMaximum(255)
        self.sat.setSingleStep(5)
        self.sat.setOrientation(QtCore.Qt.Horizontal)
        self.sat.setObjectName(_fromUtf8("sat"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 320, 10, 71))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setThreshold.clicked.connect(self.video.set_thres)
        self.value.valueChanged.connect(self.video.setValue)
        self.hue.valueChanged.connect(self.video.setHue)
        self.sat.valueChanged.connect(self.video.setSatu)
        self.min_check.stateChanged.connect(self.video.set_Thres_Min)
        self.max_check.stateChanged.connect(self.video.set_Thres_Max)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("ThresViewer", "ThresViewer", None, QtGui.QApplication.UnicodeUTF8))
        self.setThreshold.setText(QtGui.QApplication.translate("MainWindow", "Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.h_lbl.setText(QtGui.QApplication.translate("MainWindow", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.v_lbl.setText(QtGui.QApplication.translate("MainWindow", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.hue_label.setText(QtGui.QApplication.translate("MainWindow", "Hue: ", None, QtGui.QApplication.UnicodeUTF8))
        self.sat_label.setText(QtGui.QApplication.translate("MainWindow", "Sat:", None, QtGui.QApplication.UnicodeUTF8))
        self.value_label.setText(QtGui.QApplication.translate("MainWindow", "Val:", None, QtGui.QApplication.UnicodeUTF8))
        self.min_check.setText(QtGui.QApplication.translate("MainWindow", "Min. Values", None, QtGui.QApplication.UnicodeUTF8))
        self.max_check.setText(QtGui.QApplication.translate("MainWindow", "Max. Values", None, QtGui.QApplication.UnicodeUTF8))
        self.h_min_lbl.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.s_min_lbl.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.v_min_lbl.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.h_max_lbl.setText(QtGui.QApplication.translate("MainWindow", "180", None, QtGui.QApplication.UnicodeUTF8))
        self.s_max_lbl.setText(QtGui.QApplication.translate("MainWindow", "255", None, QtGui.QApplication.UnicodeUTF8))
        self.v_max_lbl.setText(QtGui.QApplication.translate("MainWindow", "255", None, QtGui.QApplication.UnicodeUTF8))
        self.s_lbl.setText(QtGui.QApplication.translate("MainWindow", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>-</p><p>-</p><p>-</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

