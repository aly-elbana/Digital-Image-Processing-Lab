"""
Basic pixel-level operations.

Each function here performs exactly one simple operation on the input image.
All images are expected to be NumPy arrays in RGB format.
"""

import cv2
import numpy as np


def to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Convert an RGB image to grayscale and then back to RGB so that
    it can be displayed side-by-side with the original.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    gray_rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    return gray_rgb


def invert_image(image: np.ndarray) -> np.ndarray:
    """
    Invert all pixel values (simple negative image).
    """
    inverted = 255 - image
    return inverted


