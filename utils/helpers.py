from PIL import Image

def resize_image(image, max_width=1200):
    """
    Resize image while maintaining aspect ratio.
    """

    width, height = image.size

    if width <= max_width:
        return image

    ratio = max_width / width

    new_height = int(height * ratio)

    return image.resize((max_width, new_height))

def get_image_info(image):
    """
    Return image information.
    """

    width, height = image.size

    return {
        "Width": width,
        "Height": height,
        "Mode": image.mode
    }