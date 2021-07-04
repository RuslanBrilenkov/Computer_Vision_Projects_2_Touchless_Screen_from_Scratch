import cv2
import numpy as np
import pyautogui
print("Imports are Done!")

# As usual, capturing video from a web cam:
cap = cv2.VideoCapture(0)

# ! Need to explore these colours in the interactive manner - personal choice!
# In my case, I have a green marker:
ColorMin = np.array([35, 160, 0], dtype=np.uint8)
ColorMax = np.array([85, 255, 255], dtype=np.uint8)

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
	frame = cv2.flip(frame, 1)
	# Copying our frame into another variable
	img = frame
	
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	threshold = cv2.inRange(hsv, ColorMin, ColorMax)
	contours, hierarchy = cv2.findContours(threshold, 1, 2)
	
	result = cv2.bitwise_and(frame, frame, mask = threshold)

	### Meat of the program is here   ###
	try:
		max_area = 0
		last_x = centroid_x
		last_y = centroid_y

		if contours:
			for i in contours:
				area = cv2.contourArea(i)
				if area > max_area:
					max_area = area
					cnt = i
		#print(last_x, last_y, area)
		x,y,w,h = cv2.boundingRect(cnt)
		cv2.rectangle(result, (x,y), (x+w,y+h), (0,0,255), 5)
	
		centroid_x = (x + x+w)//2
		centroid_y = (y + y+h)//2

		cv2.circle(result, (centroid_x, centroid_y), 2, (0,0,255), 10)
	
		# Check if the centroid is withing the left half of the screen
		if (centroid_x >= 0)and(centroid_x <= int(width/2))and(centroid_y >= 0) and (centroid_y <= int(height)):
			print("Cursor is at the left side")
			# if -> up else -> down
			if (int(height//2-rect_size)-centroid_y > 0):
				if (int(width//4-rect_size)-centroid_x > 0):
					# moving up-left
					pyautogui.move(-10, -10)
				elif (int(width//4+rect_size)-centroid_x < 0):
					# moving up-right
					pyautogui.move(10, -10)
				else:
					# or just up
					pyautogui.move(0, -10)
			elif (int(height//2+rect_size)-centroid_y < 0):
				if (int(width//4-rect_size)-centroid_x > 0):
					# moving down-left
					pyautogui.move(-10, 10)
				elif (int(width//4+rect_size)-centroid_x < 0):
					# moving down-right
					pyautogui.move(10, 10)
				else:
					# or just up
					pyautogui.move(0, 10)
			# if -> left else -> right
			elif (int(width//4-rect_size)-centroid_x > 0):
				if (int(height//2-rect_size)-centroid_y > 0):
					# moving left-up
					pyautogui.move(-10, -10)
				elif (int(height//2+rect_size)-centroid_y < 0):
					# moving left-down
					pyautogui.move(-10, 10)
				else:
					# or just left
					pyautogui.move(-10, 0)
			elif (int(width//4+rect_size)-centroid_x < 0):
				if (int(height//2-rect_size)-centroid_y > 0):
					# moving right-up
					pyautogui.move(10, -10)
				elif (int(height//2+rect_size)-centroid_y < 0):
					# moving right_left
					pyautogui.move(10, 10)
				else:
					# or just right
					pyautogui.move(10, 0)
			
		else:
			print("Cursor is at the right side")
	
	except Exception as e:
		print(e)
	
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
	
	cv2.putText(result, "Author: R. Brilenkov", (int(width*3//4-rect_size), int(height*6.5//7)), font, 0.7, frame_color, 1, cv2.LINE_AA) # adding text label for Author

	# Showing the thresholded frame on the screen
	cv2.imshow('result', result)
	
	# Breaking the cycle on ESC key
	k = cv2.waitKey(30) & 0xFF
	if k == 27:
		break
		
cap.release()
cv2.destroyAllWindows()
