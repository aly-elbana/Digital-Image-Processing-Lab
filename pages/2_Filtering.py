import streamlit as st

from processing.filtering import (
    apply_average_blur,
    apply_gaussian_blur,
    apply_median_blur,
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
    Page for smoothing and noise reduction filters.
    """
    init_state()

    st.title("2 - Filtering (Smoothing and Noise Reduction)")
    st.write("Apply Gaussian, Median, and Average filters with kernel size control.")

    original = get_original_image()
    processed = get_processed_image()

    if original is None:
        st.warning("Please go back to the main page and upload an image first.")
        return

    working_image = processed if processed is not None else original

    st.markdown("### Kernel Settings")
    kernel_size = st.slider(
        "Kernel Size (odd number)",
        min_value=1,
        max_value=21,
        step=2,
        value=5,
    )

    st.caption("Kernel size must be an odd number for some filters to work correctly.")

    st.markdown("### Choose Filter Type")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Gaussian Blur"):
            result = apply_gaussian_blur(working_image, kernel_size)
            set_processed_image(result)
            processed = get_processed_image()

    with col2:
        if st.button("Median Blur"):
            # Median blur requires kernel size greater than 1
            if kernel_size < 3:
                st.warning("Median filter requires kernel size greater than 1. Choose 3 or larger.")
            else:
                result = apply_median_blur(working_image, kernel_size)
                set_processed_image(result)
                processed = get_processed_image()

    with col3:
        if st.button("Average Blur"):
            result = apply_average_blur(working_image, kernel_size)
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
            st.info("No filter has been applied yet. Choose a filter from above.")


if __name__ == "__main__":
    main()


