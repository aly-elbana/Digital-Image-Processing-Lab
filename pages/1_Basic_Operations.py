import streamlit as st

from processing.basic import invert_image, to_grayscale
from utils.state_manager import (
    get_original_image,
    get_processed_image,
    init_state,
    reset_to_original,
    set_processed_image,
)


def main() -> None:
    """
    Page for basic pixel-level operations.
    """
    init_state()

    st.title("1 - Basic Operations")
    st.write("Convert images to grayscale or create a negative (inverted colors) image.")


    original = get_original_image()
    processed = get_processed_image()

    if original is None:
        st.warning("Please go back to the main page and upload an image first.")
        return

    working_image = processed if processed is not None else original

    st.markdown("### Choose Operation")

    col_buttons1, col_buttons2 = st.columns(2)

    with col_buttons1:
        if st.button("Convert to Grayscale"):
            result = to_grayscale(working_image)
            set_processed_image(result)
            processed = get_processed_image()

    with col_buttons2:
        if st.button("Invert Colors (Negative)"):
            result = invert_image(working_image)
            set_processed_image(result)
            processed = get_processed_image()

    st.markdown("---")
    st.markdown("### Global Tools")
    if st.button("Reset to Original Image"):
        reset_to_original()
        st.rerun()

    st.markdown("---")
    st.markdown("### Preview Result")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Before**")
        st.image(original, width='stretch')
    with col2:
        st.markdown("**After**")
        if processed is not None:
            st.image(processed, width='stretch')
        else:
            st.info("No operation has been applied yet. Choose an operation from above.")


if __name__ == "__main__":
    main()


