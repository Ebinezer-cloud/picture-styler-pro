import cv2

def apply(image):
    """
    HDR Effect
    """

    return cv2.detailEnhance(
        image,
        sigma_s=12,
        sigma_r=0.15
    )