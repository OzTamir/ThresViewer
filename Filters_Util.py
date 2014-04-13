import numpy as np

COLOR_MIN_ARRAY = [60, 160, 125]
COLOR_MAX_ARRAY = [90, 255, 255]
COLOR_MIN_ARRAY = np.array(COLOR_MIN_ARRAY, np.uint8)
COLOR_MAX_ARRAY = np.array(COLOR_MAX_ARRAY, np.uint8)

THRESHOLD = False
SHOW_RECT = False
SHOW_CIRCLES = False

def set_thres():
	global THRESHOLD
	THRESHOLD = not THRESHOLD

def setColor(MIN, MAX):
	global COLOR_MIN_ARRAY
	global COLOR_MAX_ARRAY
	COLOR_MIN_ARRAY = np.array(COLOR_MIN_ARRAY, np.uint8)
	COLOR_MAX_ARRAY = np.array(COLOR_MAX_ARRAY, np.uint8)

