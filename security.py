import cv2
import time as tme
from pygame import mixer

# Webcam Motion Detector

# The BACKGROUND_REFRESH_RATE helps to control the sensitivity of the motion.
# Lower values means less sensitivity
BACKGROUND_REFRESH_RATE = 10

# This value controls how much difference there has to be between the pixels
# before it is considered different. Higher values means less sensitivity.
SENSITIVITY_THRESHOLD = 80

# Helps to only alert on large motion patches. Higher number means less sensitivity.
MOTION_SIZE = 10000

# This will be used to compare the current frame to the frame from some time ago.
static_background = None

# Get some sound ready to play on motion detection
mixer.init()
mixer.music.load("./buzzer.mp3")

# Capturing video
# on my setup
# 0 is laptop Webcam
# 1 is a usb webcam
video = cv2.VideoCapture(0)

# Keep track of an iteration, so we know how often to refresh the
# background image we are comparing to.
iteration = BACKGROUND_REFRESH_RATE

# Infinite while loop to treat stack of image as video
while True:
	# Reading frame(image) from video
	check, frame = video.read()

	# Converting color image to gray_scale image
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Converting gray scale image to GaussianBlur
	# so that change can be found easily
	grayblur = cv2.GaussianBlur(gray, (21, 21), 0)

	# Reset the value of static_background, and reset the iteration count
    # periodically so we don't get too big of a number.
	if iteration % BACKGROUND_REFRESH_RATE == 0:
		iteration = 1
		static_background = grayblur
		continue

	# Difference between static background
	# and current frame(which is GaussianBlur)
	diff_frame = cv2.absdiff(static_background, grayblur)

	# If change in between static background and current frame is greater
    # than SENSITIVITY_THRESHOLD it will show white color(255)
	thresh_frame = cv2.threshold(diff_frame, SENSITIVITY_THRESHOLD, 255, cv2.THRESH_BINARY)[1]
	thresh_frame = cv2.dilate(thresh_frame, None, iterations = 0)

	# Finding shapes of moving object
	shapes,_ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for shape in shapes:
        # Ignore small motion areas
		if cv2.contourArea(shape) < MOTION_SIZE:
			print("motion not detected")
			continue
		print("motion detected")
		# mixer.music.play()

		# Making green rectangle around the moving object
		(x, y, w, h) = cv2.boundingRect(shape)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

	iteration += 1

	# Displaying debugging images
	cv2.imshow("Gray Frame", gray)
	cv2.imshow("Grayblur Frame", grayblur)
	cv2.imshow("Difference Frame", diff_frame)
	cv2.imshow("Threshold Frame", thresh_frame)
	cv2.imshow("Color Frame", frame)
	cv2.waitKey(1) # Without this, the images don't show

video.release()

# Destroying all the windows
cv2.destroyAllWindows()
