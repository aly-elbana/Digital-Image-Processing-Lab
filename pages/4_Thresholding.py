import streamlit as st

from processing.thresholding import (
    adaptive_gaussian_threshold,
    adaptive_mean_threshold,
    global_threshold,
)
from utils.state_manager import (
    get_original_image,
    get_processed_image,
    init_state,
    reset_to_original,
    set_processed_image,
)


def main() -> None:
    """
    Page for global and adaptive thresholding.
    """
    init_state()

    st.title("4 - Thresholding")
    st.write("Apply global threshold and adaptive threshold (Mean / Gaussian) to the image.")

    original = get_original_image()
    processed = get_processed_image()

    if original is None:
        st.warning("Please go back to the main page and upload an image first.")
        return

    working_image = processed if processed is not None else original

    st.markdown("### Global Threshold Settings")
    global_thresh = st.slider("Threshold Value (Global Threshold)", 0, 255, 127)

    st.markdown("### Adaptive Threshold Settings")
    block_size = st.slider(
        "Block Size (odd number)",
        min_value=3,
        max_value=51,
        step=2,
        value=11,
    )
    c_value = st.slider("C Value (subtracted from mean)", -20, 20, 2)

    st.markdown("### Choose Threshold Type")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Global Threshold"):
            result = global_threshold(working_image, global_thresh)
            set_processed_image(result)
            processed = get_processed_image()

    with col2:
        if st.button("Adaptive Mean"):
            result = adaptive_mean_threshold(working_image, block_size, c_value)
            set_processed_image(result)
            processed = get_processed_image()

    with col3:
        if st.button("Adaptive Gaussian"):
            result = adaptive_gaussian_threshold(working_image, block_size, c_value)
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
            st.info("No operation has been applied yet. Choose a threshold type from above.")


if __name__ == "__main__":
    main()


