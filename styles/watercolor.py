import cv2

def apply(image):
    """
    Watercolor Effect
    """

    watercolor, _ = cv2.stylization(
        image,
        sigma_s=60,
        sigma_r=0.6
    ), None

    return watercolor