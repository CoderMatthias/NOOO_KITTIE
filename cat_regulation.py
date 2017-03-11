# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# Initialize background
firstFrame = None
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # if the first frame is None, initialize it
#    if firstFrame is None:
#        firstFrame = gray
#        continue
 
    # compute the absolute difference between the current frame and
    # first frame
#    frameDelta = cv2.absdiff(firstFrame, gray)
#    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    # dilate the thresholded image to fill in holes, then find contours
    # on thresholded image
#    thresh = cv2.dilate(thresh, None, iterations=2)
#    (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, 
#                                 cv2.CHAIN_APPROX_SIMPLE)

    # loop over the contours
#    for c in cnts:
        # if the contour is too small, ignore it
#        if cv2.contourArea(c) < args["min_area"]:
#            continue

        # compute the bounding box for the contour, draw it on the frame,
        # and update the text
#        (x, y, w, h) = cv2.boundingRect(c)
#        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#        text = "Occupied"

# draw the text and timestamp on the frame
#    cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
#    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
#    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
#               (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

	# show the frame
    cv2.imshow("Frame", gray)
    key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
    rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
