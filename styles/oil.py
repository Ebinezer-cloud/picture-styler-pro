import cv2

def apply(image):
    """
    Oil Painting Effect
    """

    try:
        return cv2.xphoto.oilPainting(image, 7, 1)
    except:
        return cv2.stylization(image, sigma_s=60, sigma_r=0.6)