"""
Image enhancement operations such as histogram equalization and sharpening.
"""

import cv2
import numpy as np
from typing import List

def histogram_equalization(image: np.ndarray) -> np.ndarray:
    """
    Apply histogram equalization to each channel separately in YCrCb color space.
    This tends to improve global contrast.
    """
    ycrcb = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)
    y, cr, cb = cv2.split(ycrcb)
    y_eq = cv2.equalizeHist(y)
    ycrcb_eq = cv2.merge((y_eq, cr, cb))
    result = cv2.cvtColor(ycrcb_eq, cv2.COLOR_YCrCb2RGB)
    return result

def show_histogram(image: np.ndarray) -> List[np.ndarray]:
    """
    Show the histogram of a 3-channel image (like RGB) separately.
    """
    # List of channel colors for plotting
    colors = ('b', 'g', 'r')  # OpenCV uses BGR order by default
    histograms = []
    for i, color in enumerate(colors):
        # calcHist([images], [channel], mask, [histSize], [ranges])
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        histograms.append(hist)
    return histograms
    
def sharpen_image(image: np.ndarray) -> np.ndarray:
    """
    Apply a simple sharpening filter using a fixed kernel.
    """
    kernel = np.array(
        [
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0],
        ],
        dtype=np.float32,
    )
    sharpened = cv2.filter2D(image, -1, kernel)
    return sharpened


