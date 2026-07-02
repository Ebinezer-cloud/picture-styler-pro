import cv2

def apply(image):
    """
    Black & White
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)