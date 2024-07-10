# Gesture-controlled-PPT-with-face-detection
"Gesticulation Mapping" combines hand gesture control and facial detection to manage PowerPoint slides securely. Using Python with OpenCV and CVZone, it enables intuitive slide navigation and ensures access only to authorized users through facial recognition.


Project Title: Gesticulation Mapping 🖐️📊
Project Overview:
This project enables users to control PowerPoint slides using hand gestures. Additionally, it incorporates face detection to ensure only authorized users can access the presentation.

Directory Structure 📁

<img width="360" alt="Screenshot 2024-07-11 at 1 03 54 AM" src="https://github.com/prasanna-ravi12/Gesture-controlled-PPT-with-face-detection/assets/175058249/7da17d0d-a7f3-498a-b15d-611079fdbbce">


#### Features 🚀
- **Hand Gesture Control**: Navigate through slides using predefined hand gestures.
- **Face Detection**: Authenticate users based on facial recognition before granting access to the presentation.

#### Methods Used 🛠️
##### Face Detection (`FACE_DETECTION.py`)
The `create_database()` function initializes a database of authorized users by capturing images from the webcam. It uses OpenCV for image processing and face detection using Haar cascades. Here’s a breakdown:
- **Database Creation**: Captures multiple images of each authorized user's face.
- **Image Processing**: Enhances image contrast using histogram equalization.
- **Face Recognition**: Trains a model using LBPH (Local Binary Patterns Histograms) to recognize authorized users during access.

##### Hand Gesture Control (`HAND_GESTURE.py`)
The `HandDetector` module from `cvzone` is used to detect and track hand gestures. Key features include:
- **Gesture Recognition**: Identifies gestures such as left swipe (previous slide) and right swipe (next slide).
- **Annotation**: Allows users to annotate slides using finger gestures.
- **Zooming**: Implements zoom functionality based on hand gestures for detailed slide viewing.

#### Installation 📥
1. pip install numpy cvzone mediapipe



