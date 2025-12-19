"""
Edge detection operations.
"""

import cv2
import numpy as np


def sobel_edges(image: np.ndarray) -> np.ndarray:
    """
    Detect edges using the Sobel operator in both x and y directions.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = cv2.magnitude(sobelx, sobely)
    magnitude = cv2.convertScaleAbs(magnitude)
    edges_rgb = cv2.cvtColor(magnitude, cv2.COLOR_GRAY2RGB)
    return edges_rgb


def laplacian_edges(image: np.ndarray) -> np.ndarray:
    """
    Detect edges using the Laplacian operator.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    lap = cv2.convertScaleAbs(lap)
    edges_rgb = cv2.cvtColor(lap, cv2.COLOR_GRAY2RGB)
    return edges_rgb


def canny_edges(image: np.ndarray, threshold1: int, threshold2: int) -> np.ndarray:
    """
    Detect edges using the Canny edge detector.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, threshold1, threshold2)
    edges_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    return edges_rgb


