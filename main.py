import logging as logger
import cv2
import numpy as np
import screen_brightness_control as sbc

# set logger
logger.basicConfig(encoding='utf-8', level=logger.INFO, format='%(asctime)s [%(levelname)s] %(message)s')


# capture video from the webcam
cap = cv2.VideoCapture(0)

while True:
    # read the image from the webcam
    ret, frame = cap.read()

    if not ret:
        break

    # convert the image to grayscale
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # calculate the average brightness
    avg_brightness = np.average(grayscale)

    # normalize the average brightness value
    avg_brightness /= 255
    avg_brightness *= 100 # brightness values are between 0 and 100

    logger.info(f'Average brightness: {avg_brightness}')
    sbc.set_brightness(avg_brightness)


    # show the image
    # cv2.imshow('Webcam', frame)

    # break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
