# coding=utf8
 
# Copyright (C) 2011 Saúl Ibarra Corretgé <saghul@gmail.com>
#
 
# Some inspiration taken from: http://www.morethantechnical.com/2009/03/05/qt-opencv-combined-for-face-detecting-qwidgets/

import urllib2 as urllib
import cv
import cv2
import sys
from VidCap import setThreshold, setColor, getColor
from time import sleep
from cv2 import imdecode, CV_LOAD_IMAGE_COLOR
import numpy as np

from PyQt4.QtCore import QPoint, QTimer
from PyQt4.QtGui import QApplication, QImage, QPainter, QWidget
  
class IplQImage(QImage):
    """
    http://matthewshotton.wordpress.com/2011/03/31/python-opencv-iplimage-to-pyqt-qimage/
    A class for converting iplimages to qimages
    """
 
    def __init__(self,iplimage):
        # Rough-n-ready but it works dammit
        alpha = cv.CreateMat(iplimage.height,iplimage.width, cv.CV_8UC1)
        cv.Rectangle(alpha, (0, 0), (iplimage.width,iplimage.height), cv.ScalarAll(255) ,-1)
        rgba = cv.CreateMat(iplimage.height, iplimage.width, cv.CV_8UC4)
        cv.Set(rgba, (1, 2, 3, 4))
        cv.MixChannels([iplimage, alpha],[rgba], [
        (0, 0), # rgba[0] -> bgr[2]
        (1, 1), # rgba[1] -> bgr[1]
        (2, 2), # rgba[2] -> bgr[0]
        (3, 3)  # rgba[3] -> alpha[0]
        ])
        self.__imagedata = rgba.tostring()
        super(IplQImage,self).__init__(self.__imagedata, iplimage.width, iplimage.height, QImage.Format_RGB32)
 
class VideoWidget(QWidget):
    """ A class for rendering video coming from OpenCV """
    THRESHOLD = False
    SHOW_RECT = False
    SHOW_CIRCLES = False
    SHOW_GOAL = False
    HEIGHT = 310
    BOUND = 'Min'
    def __init__(self, parent=None):
		if parent is None:
			QWidget.__init__(self)
		else:
			QWidget.__init__(self, parent)
		self._capture = cv2.VideoCapture(0)
		self._capture.set(3, 320)
		self._capture.set(4, 240)
		frame = self._capture.read()[1]
		frame = self.get_iplimg(frame)
		self._frame = None
		self._image = self._build_image(frame)
		self.setMinimumSize(320, 240)
		self.setMaximumSize(320, 240)
		# Paint every 50 ms
		self._timer = QTimer(self)
		self._timer.timeout.connect(self.queryFrame)
		self._timer.start(30)
 
    def _build_image(self, frame):
        if not self._frame:
            self._frame = cv.CreateImage((320, 240), cv.IPL_DEPTH_8U, frame.nChannels)
        if frame.origin == cv.IPL_ORIGIN_TL:
            cv.Copy(frame, self._frame)
        else:
            cv.Flip(frame, self._frame, 0)
        return IplQImage(self._frame)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(QPoint(0, 0), self._image)

    def get_iplimg(self, image):
		img_mat = cv.fromarray(image)
		return cv.GetImage(img_mat)
    
    def queryFrame(self):
		image = self._capture.read()[1]
		if self.THRESHOLD:
			image = setThreshold(image)
			image = cv2.cvtColor(image, cv.CV_GRAY2RGB)
		frame = self.get_iplimg(image)
		self._image = self._build_image(frame)
		self.update()

# GUI event handlers from now on...	
    def slide_anim(self):
		if self.HEIGHT > 520:
			self._atimer.stop()
		else:
			self.HEIGHT += 5
			self.parent().parent().resize(545, self.HEIGHT)
    
    def slide_anim_cls(self):
		if self.HEIGHT < 315:
			self._atimer.stop()
		else:
			self.HEIGHT -= 5
			self.parent().parent().resize(545, self.HEIGHT)
	
    def set_thres(self):
		if self.THRESHOLD:
			self._atimer = QTimer(self)
			self._atimer.timeout.connect(self.slide_anim_cls)
			self._atimer.start(30)
		else:
			self._atimer = QTimer(self)
			self._atimer.timeout.connect(self.slide_anim)
			self._atimer.start(30)
		self.THRESHOLD = not self.THRESHOLD
    
    def setSatu(self, s_value):
		setColor(self.BOUND, 'S', s_value)
		if self.BOUND == 'Min':
			self.parent().parent().ui.s_min_lbl.setText(QApplication.translate("MainWindow", str(s_value), None, QApplication.UnicodeUTF8))
		elif self.BOUND == 'Max':
			self.parent().parent().ui.s_max_lbl.setText(QApplication.translate("MainWindow", str(s_value), None, QApplication.UnicodeUTF8))
    
    def setHue(self, h_value):
		setColor(self.BOUND, 'H', h_value)
		if self.BOUND == 'Min':
			self.parent().parent().ui.h_min_lbl.setText(QApplication.translate("MainWindow", str(h_value), None, QApplication.UnicodeUTF8))
		elif self.BOUND == 'Max':
			self.parent().parent().ui.h_max_lbl.setText(QApplication.translate("MainWindow", str(h_value), None, QApplication.UnicodeUTF8))
    
    def setValue(self, v_value):
		setColor(self.BOUND, 'V', v_value)
		if self.BOUND == 'Min':
			self.parent().parent().ui.v_min_lbl.setText(QApplication.translate("MainWindow", str(v_value), None, QApplication.UnicodeUTF8))
		elif self.BOUND == 'Max':
			self.parent().parent().ui.v_max_lbl.setText(QApplication.translate("MainWindow", str(v_value), None, QApplication.UnicodeUTF8))
    
    def set_Thres_Min(self, value):
		'''
		Changes wether the color picker will apply for the maximum values or for the minimum values.
		Called when the min/max checkboxes are called
		'''
		if value == 0 and self.parent().parent().ui.max_check.isChecked():
			self.BOUND = 'Max'
			self.parent().parent().ui.hue.setValue(getColor(self.BOUND, 'H'))
			self.parent().parent().ui.sat.setValue(getColor(self.BOUND, 'S'))
			self.parent().parent().ui.value.setValue(getColor(self.BOUND, 'V'))

		elif value == 0 and not self.parent().parent().ui.max_check.isChecked():
			self.parent().parent().ui.max_check.setChecked(True)
			self.BOUND = 'Max'
			self.parent().parent().ui.hue.setValue(getColor(self.BOUND, 'H'))
			self.parent().parent().ui.sat.setValue(getColor(self.BOUND, 'S'))
			self.parent().parent().ui.value.setValue(getColor(self.BOUND, 'V'))
			
		elif value == 2 and self.parent().parent().ui.max_check.isChecked():
			self.parent().parent().ui.max_check.setChecked(False)
			self.BOUND = 'Min'
			self.parent().parent().ui.hue.setValue(getColor(self.BOUND, 'H'))
			self.parent().parent().ui.sat.setValue(getColor(self.BOUND, 'S'))
			self.parent().parent().ui.value.setValue(getColor(self.BOUND, 'V'))
			
		elif value == 2:
			self.BOUND = 'Min'
			self.parent().parent().ui.hue.setValue(getColor(self.BOUND, 'H'))
			self.parent().parent().ui.sat.setValue(getColor(self.BOUND, 'S'))
			self.parent().parent().ui.value.setValue(getColor(self.BOUND, 'V'))

    def set_Thres_Max(self, value):
		if value == 0 and self.parent().parent().ui.min_check.isChecked():
			self.BOUND = 'Min'
			self.parent().parent().ui.hue.setValue(getColor(self.BOUND, 'H'))
			self.parent().parent().ui.sat.setValue(getColor(self.BOUND, 'S'))
			self.parent().parent().ui.value.setValue(getColor(self.BOUND, 'V'))
		elif value == 0 and not self.parent().parent().ui.min_check.isChecked():
			self.parent().parent().ui.min_check.setChecked(True)
			self.BOUND = 'Min'
			self.parent().parent().ui.hue.setValue(getColor(self.BOUND, 'H'))
			self.parent().parent().ui.sat.setValue(getColor(self.BOUND, 'S'))
			self.parent().parent().ui.value.setValue(getColor(self.BOUND, 'V'))
		elif value == 2 and self.parent().parent().ui.min_check.isChecked():
			self.parent().parent().ui.min_check.setChecked(False)
			self.BOUND = 'Max'
			self.parent().parent().ui.hue.setValue(getColor(self.BOUND, 'H'))
			self.parent().parent().ui.sat.setValue(getColor(self.BOUND, 'S'))
			self.parent().parent().ui.value.setValue(getColor(self.BOUND, 'V'))
		elif value == 2:
			self.BOUND = 'Max'
			self.parent().parent().ui.hue.setValue(getColor(self.BOUND, 'H'))
			self.parent().parent().ui.sat.setValue(getColor(self.BOUND, 'S'))
			self.parent().parent().ui.value.setValue(getColor(self.BOUND, 'V'))
