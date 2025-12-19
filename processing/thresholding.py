"""
Thresholding operations: global and adaptive thresholding.
"""

import cv2
import numpy as np


def global_threshold(image: np.ndarray, thresh_value: int, max_value: int = 255) -> np.ndarray:
    """
    Apply simple global binary thresholding on the grayscale version of the image.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, thresh_value, max_value, cv2.THRESH_BINARY)
    thresh_rgb = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)
    return thresh_rgb


def adaptive_mean_threshold(image: np.ndarray, block_size: int, c: int) -> np.ndarray:
    """
    Apply adaptive mean thresholding on the grayscale version of the image.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        block_size,
        c,
    )
    thresh_rgb = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)
    return thresh_rgb


def adaptive_gaussian_threshold(image: np.ndarray, block_size: int, c: int) -> np.ndarray:
    """
    Apply adaptive Gaussian thresholding on the grayscale version of the image.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        block_size,
        c,
    )
    thresh_rgb = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)
    return thresh_rgb


