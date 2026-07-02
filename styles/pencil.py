import cv2

def apply(image):
    """
    Convert image to pencil sketch.
    Input: OpenCV image (BGR)
    Output: OpenCV image (BGR)
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    inverted = 255 - gray

    blur = cv2.GaussianBlur(inverted, (21, 21), 0)

    inverted_blur = 255 - blur

    sketch = cv2.divide(gray, inverted_blur, scale=256)

    return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)