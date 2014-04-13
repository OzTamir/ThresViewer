#! /usr/bin/env python
import cv2
from cv2 import cv, cvtColor
import numpy as np

COLOR_MIN_ARR = [60, 160, 125]
COLOR_MAX_ARR = [90, 255, 255]
COLOR_MIN_ARRAY = np.array(COLOR_MIN_ARR, np.uint8)
COLOR_MAX_ARRAY = np.array(COLOR_MAX_ARR, np.uint8)

def setThreshold(img):
	'''
	Returns a thresholded version of img
	'''
	global COLOR_MIN_ARRAY
	global COLOR_MAX_ARRAY
	hsv = cvtColor(img, cv.CV_BGR2HSV)
	# Get Threshold
	return cv2.inRange(cv2.blur(hsv,(6,6)),COLOR_MIN_ARRAY,COLOR_MAX_ARRAY)

def setColor(bound, index, value):
	global COLOR_MIN_ARRAY
	global COLOR_MAX_ARRAY
	global COLOR_MIN_ARR
	global COLOR_MAX_ARR
	prop = {'H' : 0, 'S' : 1, 'V' : 2}
	if bound == 'Max':
		COLOR_MAX_ARR[prop[index]] = value
		COLOR_MAX_ARRAY = np.array(COLOR_MAX_ARR, np.uint8)
	elif bound == 'Min':
		COLOR_MIN_ARR[prop[index]] = value
		COLOR_MIN_ARRAY = np.array(COLOR_MIN_ARR, np.uint8)

def getColor(bound, index):
	global COLOR_MIN_ARRAY
	global COLOR_MAX_ARRAY
	global COLOR_MIN_ARR
	global COLOR_MAX_ARR
	prop = {'H' : 0, 'S' : 1, 'V' : 2}
	if bound == 'Max':
		return COLOR_MAX_ARR[prop[index]]
	elif bound == 'Min':
		return COLOR_MIN_ARR[prop[index]]
