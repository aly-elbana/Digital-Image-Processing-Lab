import io
from typing import Optional

import cv2
import numpy as np
from PIL import Image


def load_image_from_upload(uploaded_file) -> Optional[np.ndarray]:
    """
    Read an uploaded file from Streamlit's file_uploader and convert it
    to an OpenCV-compatible image (NumPy array in RGB format).

    Returns:
        image (np.ndarray) in RGB format or None if something goes wrong.
    """
    if uploaded_file is None:
        return None

    try:
        image_bytes = uploaded_file.read()
        pil_image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image = np.array(pil_image)
        return image
    except Exception:
        return None


def cv2_to_pil(image: np.ndarray) -> Image.Image:
    """
    Convert a NumPy RGB image into a Pillow Image for download or display.
    """
    return Image.fromarray(image)


def pil_to_bytes(pil_image: Image.Image, format: str = "PNG") -> bytes:
    """
    Convert a Pillow Image into raw bytes so it can be used
    with Streamlit's download_button.
    """
    buffer = io.BytesIO()
    pil_image.save(buffer, format=format)
    buffer.seek(0)
    return buffer.read()


