"""
Basic morphological operations: erosion, dilation, opening, and closing.
"""

import cv2
import numpy as np


def _create_kernel(kernel_size: int) -> np.ndarray:
    """
    Create a simple square structuring element for morphology operations.
    """
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return kernel


def erode(image: np.ndarray, kernel_size: int, iterations: int) -> np.ndarray:
    """
    Apply erosion to the image.
    """
    kernel = _create_kernel(kernel_size)
    result = cv2.erode(image, kernel, iterations=iterations)
    return result


def dilate(image: np.ndarray, kernel_size: int, iterations: int) -> np.ndarray:
    """
    Apply dilation to the image.
    """
    kernel = _create_kernel(kernel_size)
    result = cv2.dilate(image, kernel, iterations=iterations)
    return result


def opening(image: np.ndarray, kernel_size: int, iterations: int) -> np.ndarray:
    """
    Apply opening (erosion followed by dilation).
    """
    kernel = _create_kernel(kernel_size)
    result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=iterations)
    return result


def closing(image: np.ndarray, kernel_size: int, iterations: int) -> np.ndarray:
    """
    Apply closing (dilation followed by erosion).
    """
    kernel = _create_kernel(kernel_size)
    result = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=iterations)
    return result


