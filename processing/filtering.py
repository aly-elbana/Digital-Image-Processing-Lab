"""
Filtering and smoothing operations using simple OpenCV filters.
"""

import cv2
import numpy as np


def apply_gaussian_blur(image: np.ndarray, kernel_size: int) -> np.ndarray:
    """
    Apply Gaussian blur with a square kernel of size (kernel_size x kernel_size).
    The kernel_size should be a positive odd number.
    """
    blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return blurred


def apply_median_blur(image: np.ndarray, kernel_size: int) -> np.ndarray:
    """
    Apply median blur. The kernel size must be an odd integer greater than 1.
    """
    blurred = cv2.medianBlur(image, kernel_size)
    return blurred


def apply_average_blur(image: np.ndarray, kernel_size: int) -> np.ndarray:
    """
    Apply simple averaging blur using a normalized box filter.
    """
    blurred = cv2.blur(image, (kernel_size, kernel_size))
    return blurred


