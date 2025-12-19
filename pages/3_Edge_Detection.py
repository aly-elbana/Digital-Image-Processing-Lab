import streamlit as st

from processing.edges import canny_edges, laplacian_edges, sobel_edges
from utils.state_manager import (
    get_original_image,
    get_processed_image,
    init_state,
    reset_to_original,
    set_processed_image,
)


def main() -> None:
    """
    Page for edge detection operations.
    """
    init_state()

    st.title("3 - Edge Detection")
    st.write("Experiment with Sobel, Laplacian, and Canny filters to detect edges in the image.")

    original = get_original_image()
    processed = get_processed_image()

    if original is None:
        st.warning("Please go back to the main page and upload an image first.")
        return

    # Use the latest processed image if it exists; otherwise, start from original.
    working_image = processed if processed is not None else original

    st.markdown("### Canny Settings")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        threshold1 = st.slider("First Threshold (Threshold1)", 0, 255, 100)
    with col_t2:
        threshold2 = st.slider("Second Threshold (Threshold2)", 0, 255, 200)

    st.markdown("### Choose Edge Detection Method")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Sobel"):
            result = sobel_edges(working_image)
            set_processed_image(result)
            processed = get_processed_image()

    with col2:
        if st.button("Laplacian"):
            result = laplacian_edges(working_image)
            set_processed_image(result)
            processed = get_processed_image()

    with col3:
        if st.button("Canny"):
            result = canny_edges(working_image, threshold1, threshold2)
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
            st.info("No operation has been applied yet. Choose a filter from above.")


if __name__ == "__main__":
    main()


