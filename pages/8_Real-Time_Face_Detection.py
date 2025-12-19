import cv2 as cv
import streamlit as st
from processing.filtering import apply_gaussian_blur

def main() -> None:
    """
    Main function for the real-time face detection page.
    """
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
    smile_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_smile.xml')

    st.title("Real-Time Face Detection")
    st.write("Detect faces, eyes, and smiles in real-time using your webcam.")
    try:
        if st.button("Start Detection"):
            cam = cv.VideoCapture(0)
            frame_placeholder = st.empty()

            while True:
                ret, frame = cam.read()
                if not ret:
                    st.error("Failed to grab frame")
                    break

                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                gray = apply_gaussian_blur(gray, 5)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

                for (x, y, w, h) in faces:
                    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    roi_gray = gray[y:y + h, x:x + w]
                    roi_color = frame[y:y + h, x:x + w]

                    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=3)
                    smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=3)

                    for (ex, ey, ew, eh) in eyes:
                        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
                    for (sx, sy, sw, sh) in smiles:
                        cv.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

                    cv.putText(frame, 'Face', (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                frame_placeholder.image(frame, channels="RGB")
            cam.release()
    except Exception as e:
        st.error(f"Error: {e}")
        cam.release()


if __name__ == "__main__":
    main()