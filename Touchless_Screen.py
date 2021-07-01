import cv2
import numpy as np
import pyautogui
print("Imports are Done!")

# As usual, capturing video from a web cam:
cap = cv2.VideoCapture(0)

# ! Need to explore these colours in the interactive manner - personal choice!
ColorMin = np.array([155, 118, 100], dtype=np.uint8)
ColorMax = np.array([179, 255, 255], dtype=np.uint8)

# Defining centroid coordinates
centroid_x, centroid_y = 0, 0

# Defining the text font
font = cv2.FONT_HERSHEY_SIMPLEX

# Defining some helpful variables
rect_size = 100
frame_color = (0,255, 0)

# While video is recorded, do the stuff below
while True:
	
	# that is dangerous but will remove a lag
	# will be harder to stop the gui in case 
	# of any unexpected problem	
	#pyautogui.PAUSE = 0
	
	width, height  = cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float, float
	ret, frame = cap.read()
	
	# Flipping image for our own convenience
	img = cv2.flip(frame, 1)
	
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	threshold = cv2.inRange(hsv, ColorMin, ColorMax)
	
	result = cv2.bitwise_and(frame, frame, mask = threshold)

	### Meat of the program is here   ###
	#
	#
	###				###
	
	# Drawing helpful regions on the video for the use-friendly intuitive use
	# Left side of the screen
	cv2.rectangle(result, (int(width//4-rect_size), int(height//2-rect_size)), (int(width//4+ rect_size),int(height//2+ rect_size)), frame_color, 1)
	# Arrows indicating the direction of motion:
	image = cv2.arrowedLine(result, (int(width//4), int(height//4)), (int(width//4), int(height//8)), frame_color, 6) # arrow Up
	image = cv2.arrowedLine(result, (int(width//4), int(height*3//4)), (int(width//4), int(height*7//8)), frame_color, 6) # arrow Down
	image = cv2.arrowedLine(result, (int(width//8), int(height//2)), (int(width//16), int(height//2)), frame_color, 6) # arrow Left
	image = cv2.arrowedLine(result, (int(width*3//8), int(height//2)), (int(width*7//16), int(height//2)), frame_color, 6) # arrow Right
	cv2.putText(result, "MOVE", (int(width//4-rect_size), int(height//2)), font, 2, frame_color, 3, cv2.LINE_AA) # adding text label for instructions
	

	# Right side of the screen
	cv2.rectangle(result, (int(width*3//4-rect_size), int(height//2-rect_size)), (int(width*3//4+ rect_size),int(height//2+ rect_size)), frame_color, 1)
	
	cv2.rectangle(result, (0,0), (int(width/2),int(height)), frame_color, 1)
	cv2.putText(result, "CLICK", (int(width*3//4-rect_size), int(height//2)), font, 2, frame_color, 3, cv2.LINE_AA) # adding text label for instructions
	
	cv2.imshow('result', result)
	
	# Breaking the cycle on ESC key
	k = cv2.waitKey(30) & 0xFF
	if k == 27:
		break
		
cap.release()
cv2.destroyAllWindows()
