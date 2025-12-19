import streamlit as st

from utils.image_io import cv2_to_pil, pil_to_bytes, load_image_from_upload
from utils.state_manager import (
    get_original_image,
    get_processed_image,
    init_state,
    reset_to_original,
    set_original_image,
)


def main() -> None:
    """
    Main entry point for the image processing application.
    This page focuses on image upload and global layout only.
    The actual processing happens in the separate pages.
    """
    st.set_page_config(
        page_title="DIP Image Processing Lab",
        layout="wide",
    )

    init_state()

    st.title("Digital Image Processing Lab")
    st.write(
        "A simple and professional web application for image processing using OpenCV and NumPy through Streamlit interface."
    )

    st.markdown("---")
    st.subheader("Upload Image")

    uploaded_file = st.file_uploader(
    "Choose a file from your device (Images or MP4)",
    type=["png", "jpg", "jpeg", "webp", "mp4"],
    )

    if uploaded_file is not None:
        if uploaded_file.type == "video/mp4":
            st.warning("Video processing is not supported yet.")
            return
        else:
            image = load_image_from_upload(uploaded_file)
            if image is None:
                st.error("Failed to read image. The file might be corrupted.")
            else:
                set_original_image(image)

    original = get_original_image()
    processed = get_processed_image()

    st.markdown("---")
    st.subheader("Before / After Comparison")

    if original is None:
        st.info("No image has been uploaded yet. Please upload an image from above.")
        return

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Before (Original Image)**")
        st.image(original, width='stretch')

    with col2:
        st.markdown("**After (Latest Processed Result)**")
        if processed is not None:
            st.image(processed, width='stretch')
        else:
            st.info("No processing operation has been applied yet from the sidebar pages.")

    st.markdown("---")
    st.subheader("General Tools")

    col_reset, col_download = st.columns(2)

    with col_reset:
        if st.button("Reset to Original Image"):
            reset_to_original()
            st.rerun()

    with col_download:
        if processed is not None:
            pil_img = cv2_to_pil(processed)
            img_bytes = pil_to_bytes(pil_img, format="PNG")
            st.download_button(
                label="Download Processed Image",
                data=img_bytes,
                file_name="processed_image.png",
                mime="image/png",
            )
        else:
            st.caption("Download button will appear after applying at least one processing operation.")


if __name__ == "__main__":
    main()


