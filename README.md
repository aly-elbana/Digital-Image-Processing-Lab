# Digital Image Processing Lab

<div align="center">

**A professional web application for digital image processing using OpenCV and NumPy**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

</div>

---

## Overview

An interactive web application built with **Streamlit** that provides a comprehensive suite of digital image processing tools. The application enables users to apply advanced image processing operations with ease through a simple and modern user interface.

## Features

- **Basic Operations**: Convert to grayscale, invert colors
- **Filtering**: Apply various filters (Gaussian, Median, Bilateral, etc.)
- **Edge Detection**: Multiple algorithms (Canny, Sobel, Laplacian)
- **Thresholding**: Various binary and adaptive thresholding methods
- **Morphological Operations**: Erosion, Dilation, Opening, Closing
- **Image Enhancement**: Contrast, brightness, and sharpness adjustment
- **Batch Processing**: Process multiple images at once
- **Real-Time Face Detection**: Using webcam feed
- **AI Assistant**: Intelligent assistant for answering image processing questions

## Technologies Used

- **Streamlit** - Web framework
- **OpenCV** - Image processing and computer vision
- **NumPy** - Numerical operations on arrays
- **Pillow (PIL)** - Image processing
- **OpenAI** - AI assistant (RAG)

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
```bash
git clone <repository-url>
cd Digital-Image-Processing-Lab
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv .venv
```

3. **Activate the virtual environment**

   On Windows:
   ```bash
   .venv\Scripts\activate
   ```

   On Linux/Mac:
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

## Running the Application

After installation, run the application using the following command:

```bash
streamlit run Home.py
```

The application will automatically open in your browser at:
- **Local URL**: http://localhost:8501
- **Network URL**: http://192.168.x.x:8501

## Usage Guide

1. **Upload Image**: From the main page, upload an image from your device (PNG, JPG, JPEG, WEBP)
2. **Select Operation**: Use the sidebar menu to navigate to the desired processing page
3. **Apply Processing**: Click buttons to apply various operations
4. **Compare Results**: View original and processed images side by side
5. **Download Result**: Download the processed image when finished

## Project Tree

```
image_processing_app/
│
├── Home.py                          # Main application page
├── requirements.txt                 # Dependencies list
├── README.md                        # Documentation file
│
├── pages/                           # Streamlit pages
│   ├── 1_Basic_Operations.py       # Basic operations
│   ├── 2_Filtering.py              # Filtering and filters
│   ├── 3_Edge_Detection.py         # Edge detection
│   ├── 4_Thresholding.py           # Binary thresholding
│   ├── 5_Morphological_Operations.py # Morphological operations
│   ├── 6_Enhancement.py            # Image enhancement
│   ├── 7_Batch_Processing.py       # Batch processing
│   ├── 8_Real-Time_Face_Detection.py # Real-time face detection
│   └── 9_Assistant.py              # AI assistant
│
├── processing/                      # Image processing modules
│   ├── __pycache__/                # Python compiled files
│   ├── assistant.py                # AI assistant logic
│   ├── basic.py                    # Basic operations
│   ├── batch.py                    # Batch processing
│   ├── edges.py                    # Edge detection
│   ├── enhancement.py              # Image enhancement
│   ├── filtering.py                # Filtering
│   ├── morphology.py               # Morphological operations
│   └── thresholding.py             # Thresholding
│
├── utils/                           # Utility modules
│   ├── __pycache__/                # Python compiled files
│   ├── image_io.py                 # Image input/output
│   ├── rag_knowledge.py            # RAG knowledge base
│   └── state_manager.py            # Application state management
│
└── images/                          # Images folder (optional)
```

## Available Pages

### 1. Basic Operations
- Convert image to grayscale
- Invert colors (Negative)

### 2. Filtering
- Gaussian filter
- Median filter
- Bilateral filter
- Other filters

### 3. Edge Detection
- Canny algorithm
- Sobel filter
- Laplacian filter

### 4. Thresholding
- Binary thresholding
- Adaptive thresholding
- Otsu's Thresholding

### 5. Morphological Operations
- Erosion
- Dilation
- Opening
- Closing

### 6. Image Enhancement
- Contrast adjustment
- Brightness adjustment
- Sharpness enhancement

### 7. Batch Processing
- Process multiple images at once
- Apply same operation to a group of images

### 8. Real-Time Face Detection
- Use webcam feed
- Face detection using Haar Cascades

### 9. AI Assistant
- AI assistant for answering questions about the website
- Information about image processing
- Uses RAG (Retrieval-Augmented Generation)

## Usage Examples

### Example 1: Convert Image to Grayscale
1. Upload an image from the main page
2. Navigate to "Basic Operations" page
3. Click "Convert to Grayscale"

### Example 2: Detect Image Edges
1. Upload an image
2. Navigate to "Edge Detection" page
3. Select detection algorithm (e.g., Canny)
4. Adjust parameters as needed

### Example 3: Enhance Contrast
1. Upload an image
2. Navigate to "Enhancement" page
3. Use contrast adjustment tools

## Advanced Configuration

You can customize the application by modifying files in the `processing/` folder to add new processing operations or modify existing ones.

## Notes

- The application supports images in formats: PNG, JPG, JPEG, WEBP (videos are coming soon (probably))
- All processed images can be downloaded in PNG format
- Image state is preserved between different pages
- You can reset the image to original at any time

### Adding a New Processing Operation

1. Add the function to the appropriate file in `processing/`
2. Create a new page in `pages/` or add to an existing page
3. Use `state_manager` to manage image state

### Function Template Structure

```python
def your_processing_function(image):
    """
    Description of the operation
    
    Args:
        image: OpenCV image (numpy array)
    
    Returns:
        Processed image (numpy array)
    """
    # Processing code here
    return processed_image
```

---

<div align="center">

**Built with Streamlit and OpenCV**

</div>
