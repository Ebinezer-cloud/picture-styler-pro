from io import BytesIO

def image_to_bytes(image):
    """
    Convert PIL image into PNG bytes.
    """

    buffer = BytesIO()

    image.save(buffer, format="PNG")

    return buffer.getvalue()