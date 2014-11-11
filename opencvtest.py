import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):

	# Capture frame-by-frame
	ret, frame = cap.read()

	# Operations on the frame
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Display resulting frame
	cv2.imshow('frame',gray)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()