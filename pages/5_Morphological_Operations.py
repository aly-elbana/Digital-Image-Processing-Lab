import streamlit as st

from processing.morphology import closing, dilate, erode, opening
from utils.state_manager import (
    get_original_image,
    get_processed_image,
    init_state,
    reset_to_original,
    set_processed_image,
)


def main() -> None:
    """
    Page for basic morphological operations.
    """
    init_state()

    st.title("5 - Morphological Operations")
    st.write("Apply Erosion, Dilation, Opening, and Closing using a simple kernel.")

    original = get_original_image()
    processed = get_processed_image()

    if original is None:
        st.warning("Please go back to the main page and upload an image first.")
        return

    working_image = processed if processed is not None else original

    st.markdown("### Kernel and Iterations Settings")

    col_k, col_it = st.columns(2)
    with col_k:
        kernel_size = st.slider("Kernel Size", min_value=1, max_value=21, value=3, step=2)
    with col_it:
        iterations = st.slider("Number of Iterations", min_value=1, max_value=5, value=1)

    st.markdown("### Choose Operation")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Erosion"):
            result = erode(working_image, kernel_size, iterations)
            set_processed_image(result)
            processed = get_processed_image()

    with col2:
        if st.button("Dilation"):
            result = dilate(working_image, kernel_size, iterations)
            set_processed_image(result)
            processed = get_processed_image()

    with col3:
        if st.button("Opening"):
            result = opening(working_image, kernel_size, iterations)
            set_processed_image(result)
            processed = get_processed_image()

    with col4:
        if st.button("Closing"):
            result = closing(working_image, kernel_size, iterations)
            set_processed_image(result)
            processed = get_processed_image()

    st.markdown("---")
    st.markdown("### Global Tools")
    if st.button("Reset to Original Image"):
        reset_to_original()
        st.rerun()

    st.markdown("---")
    st.markdown("### Preview Result")

    col_before, col_after = st.columns(2)
    with col_before:
        st.markdown("**Before**")
        st.image(original, width='stretch')
    with col_after:
        st.markdown("**After**")
        if processed is not None:
            st.image(processed, width='stretch')
        else:
            st.info("No operation has been applied yet. Choose an operation from above.")


if __name__ == "__main__":
    main()


