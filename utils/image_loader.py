from PIL import Image
import numpy as np
import cv2

def load_image(uploaded_file):
    """
    Load uploaded image and return:
    - PIL Image
    - OpenCV Image
    """

    pil_image = Image.open(uploaded_file).convert("RGB")

    cv_image = cv2.cvtColor(
        np.array(pil_image),
        cv2.COLOR_RGB2BGR
    )

    return pil_image, cv_image