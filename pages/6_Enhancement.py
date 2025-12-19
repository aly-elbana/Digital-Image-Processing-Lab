import streamlit as st
import matplotlib.pyplot as plt
from processing.enhancement import histogram_equalization, sharpen_image, show_histogram
from utils.state_manager import (
    get_original_image,
    get_processed_image,
    init_state,
    reset_to_original,
    set_processed_image,
)


def main() -> None:
    """
    Page for image enhancement operations.
    """
    init_state()

    st.title("6 - Image Enhancement")
    st.write("Enhance contrast using Histogram Equalization or increase sharpness (Sharpening).")

    original = get_original_image()
    processed = get_processed_image()

    if original is None:
        st.warning("Please go back to the main page and upload an image first.")
        return

    working_image = processed if processed is not None else original

    st.markdown("### Choose Enhancement Operation")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Histogram Equalization"):
            result = histogram_equalization(working_image)
            set_processed_image(result)
            processed = get_processed_image()
            
    with col2:
        if st.button("Show Histogram"):
            histograms = show_histogram(working_image)
            
            fig, ax = plt.subplots(figsize=(10, 5))
            
            colors = ('b', 'g', 'r')
            labels = ('Blue', 'Green', 'Red')
            
            for i, hist in enumerate(histograms):
                ax.plot(hist, color=colors[i], label=labels[i])
                
            ax.set_title("Color Histogram")
            ax.set_xlabel("Pixel Intensity")
            ax.set_ylabel("Frequency")
            ax.set_xlim([0, 256])
            ax.legend()
            ax.grid(alpha=0.3)

            st.pyplot(fig)

    with col3:
        if st.button("Sharpening"):
            result = sharpen_image(working_image)
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


