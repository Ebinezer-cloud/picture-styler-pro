import cv2
import numpy as np

def apply(image):
    """
    Sepia Effect
    """

    kernel = np.array([
        [0.272,0.534,0.131],
        [0.349,0.686,0.168],
        [0.393,0.769,0.189]
    ])

    sepia = cv2.transform(image, kernel)

    sepia = np.clip(sepia,0,255)

    return sepia.astype("uint8")