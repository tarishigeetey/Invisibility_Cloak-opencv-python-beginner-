# Importing required Libraries
import cv2
import numpy as np

# Turning on webcam. 0 is the port number for default webcam of Laptop
cam = cv2.VideoCapture(0)

# Capturing the starting frames for background.
for i in range(30):  # loop numbers can vary
    # mat stores the true boolean values and background variable stroes actual values of frames.
    mat, background = cam.read()
background = cv2.flip(background, 1)  # storing last frame.

# Webcam loop till escape key is pressed.
while True:
    mat, img = cam.read()  # mat variable stores true boolean and img variable stores frames.
    mirr_img = cv2.flip(img, 1)  # flipping image.
    hsv = cv2.cvtColor(mirr_img,
                      cv2.COLOR_BGR2HSV)  # converting the frames into hsv. For getting the color range of blue cloth by using color detection

    lower = np.array([0, 120, 70])  # Lower value of Hue, Saturation, Value respectively
    upper = np.array([10, 255, 255])  # Upper value of Hue, Saturation, Value respectively

    mask = cv2.inRange(hsv, lower, upper)  # Making a mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))  # opening th Mask removing noises
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))  # dilating the mask

    mask_not = cv2.bitwise_not(mask)  # inverting the mask

    result_img = cv2.bitwise_and(mirr_img, mirr_img,
                                mask = mask_not)  # bitwise and operation for front img
    result_background = cv2.bitwise_and(background, background,
                                       mask = mask)  # bitwise and operation for background

    final = cv2.addWeighted(result_img, 1, result_background, 1, 0)  # adding both front and background ouput to get final result.

    cv2.imshow('MAGIKK!!', final)  # displaying the final output
    cv2.imshow('Original', mirr_img)  # displaying the original recording

    # Press "escape key" for terminating the program
    if cv2.waitKey(1) == 27:
        break

