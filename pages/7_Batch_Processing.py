import streamlit as st

from processing.basic import to_grayscale
from processing.batch import apply_to_batch, pair_original_and_processed
from processing.filtering import apply_gaussian_blur
from utils.image_io import load_image_from_upload


def main() -> None:
    """
    Page for simple batch processing on multiple images.
    This page does not use the global session_state images
    to keep the logic easy to understand.
    """
    st.title("7 - Batch Processing")
    st.write(
        "Apply the same operation to multiple images at once.\n"
        "This is a simple page that demonstrates the concept for educational purposes."
    )

    uploaded_files = st.file_uploader(
        "Choose multiple images",
        type=["png", "jpg", "jpeg", "webp"],
        accept_multiple_files=True,
    )

    if not uploaded_files:
        st.info("No images have been selected yet.")
        return

    operation_name = st.selectbox(
        "Choose the operation to apply to all images",
        ["Grayscale", "Gaussian Blur (k=5)"],
    )

    originals = []
    for f in uploaded_files:
        img = load_image_from_upload(f)
        if img is not None:
            originals.append(img)

    if len(originals) == 0:
        st.error("Failed to read any of the uploaded images.")
        return

    if operation_name == "Grayscale":
        processed_list = apply_to_batch(originals, to_grayscale)
    else:
        processed_list = apply_to_batch(
            originals,
            lambda im: apply_gaussian_blur(im, 5),
        )

    pairs = pair_original_and_processed(originals, processed_list)

    st.markdown("---")
    st.markdown("### Preview Results for Each Image")

    for idx, (orig, proc) in enumerate(pairs, start=1):
        st.markdown(f"#### Image {idx}")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Before**")
            st.image(orig, width='stretch')
        with col2:
            st.markdown("**After**")
            st.image(proc, width='stretch')


if __name__ == "__main__":
    main()


