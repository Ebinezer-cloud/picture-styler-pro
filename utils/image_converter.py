from PIL import Image
import numpy as np
import cv2

def cv_to_pil(cv_image):
    rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(rgb)

def pil_to_cv(pil_image):
    return cv2.cvtColor(
        np.array(pil_image),
        cv2.COLOR_RGB2BGR
    )