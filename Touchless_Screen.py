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
centroid_x = 0
centroid_y = 0

# Defining the text font
font = cv2.FONT_HERSHEY_SIMPLEX

# While video is recorded, do the stuff below
while True:
	
	FPS = cap.get(cv2.CAP_PROP_FPS)
	# that is dangerous but will remove a lag
	# will be harder to stop the gui in case 
	# of any unexpected problem	
	#pyautogui.PAUSE = 0
	
	width, height  = cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float, float
	ret, frame = cap.read()
	
	# Flipping image for our own convenience
	img = cv2.flip(frame, 1)
	
	### Meat of the program is here   ###
	#
	#
	###				###
	
	# Drawing helpful regions on the video for the use-friendly intuitive use
	cv2.rectangle(img, (int(width//4-50), int(height//2-50)), (int(width//4+50),int(height//2+50)), (0, 255, 0), 1)
	cv2.rectangle(img, (int(width*3//4-50), int(height//2-50)), (int(width*3//4+50),int(height//2+50)), (0, 255, 0), 1)
	
	cv2.rectangle(img, (0,0), (int(width/2),int(height)), (0, 255, 0), 1)
	cv2.putText(img, "FPS: "+str(FPS), (0, 50), font, 2, (0,0,255), 3, cv2.LINE_AA)
	cv2.imshow('img', img)
	
	# Breaking the cycle on ESC key
	k = cv2.waitKey(30) & 0xFF
	if k == 27:
		break
		
cap.release()
cv2.destroyAllWindows()
