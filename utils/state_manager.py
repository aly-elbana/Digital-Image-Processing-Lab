from typing import Optional

import numpy as np
import streamlit as st


def init_state() -> None:
    """
    Initialize all keys in Streamlit session_state that we plan to use.
    This makes the application logic easier to reason about.
    """
    if "original_image" not in st.session_state:
        st.session_state["original_image"] = None
    if "processed_image" not in st.session_state:
        st.session_state["processed_image"] = None


def set_original_image(image: np.ndarray) -> None:
    """
    Store the original image and reset the processed image to the original.
    """
    st.session_state["original_image"] = image
    st.session_state["processed_image"] = image.copy()


def get_original_image() -> Optional[np.ndarray]:
    """
    Convenience accessor for the original image.
    """
    return st.session_state.get("original_image")


def get_processed_image() -> Optional[np.ndarray]:
    """
    Convenience accessor for the current processed image.
    """
    return st.session_state.get("processed_image")


def set_processed_image(image: np.ndarray) -> None:
    """
    Update the processed image in session_state.
    """
    st.session_state["processed_image"] = image


def reset_to_original() -> None:
    """
    Reset the processed image back to the original one.
    Does nothing if there is no original image.
    """
    original = get_original_image()
    if original is not None:
        st.session_state["processed_image"] = original.copy()


def get_messages() -> list[dict]:
    """
    Convenience accessor for the messages.
    """
    return st.session_state.get("messages", [])


def set_messages(messages: list[dict]) -> None:
    """
    Update the messages in session_state.
    """
    st.session_state["messages"] = messages