"""
Simple helpers for batch image processing.

At this stage we only implement a small set of basic batch operations
to keep the code easy to understand.
"""

from typing import Callable, List, Tuple

import numpy as np


def apply_to_batch(
    images: List[np.ndarray],
    operation: Callable[[np.ndarray], np.ndarray],
) -> List[np.ndarray]:
    """
    Apply the same single-argument operation to a list of images.

    Args:
        images: list of RGB images as NumPy arrays.
        operation: function that takes one image and returns a processed image.

    Returns:
        List of processed images in the same order.
    """
    results: List[np.ndarray] = []
    for img in images:
        processed = operation(img)
        results.append(processed)
    return results


def pair_original_and_processed(
    originals: List[np.ndarray],
    processed: List[np.ndarray],
) -> List[Tuple[np.ndarray, np.ndarray]]:
    """
    Create (original, processed) pairs for easy iteration in the UI.
    """
    pairs: List[Tuple[np.ndarray, np.ndarray]] = []
    for orig, proc in zip(originals, processed):
        pairs.append((orig, proc))
    return pairs


