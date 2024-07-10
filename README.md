# Gesture-controlled-PPT-with-face-detection
"Gesticulation Mapping" combines hand gesture control and facial detection to manage PowerPoint slides securely. Using Python with OpenCV and CVZone, it enables intuitive slide navigation and ensures access only to authorized users through facial recognition.


Project Title: Gesticulation Mapping
Project Overview
This project enables users to control PowerPoint slides using hand gestures. Additionally, it incorporates face detection to ensure only authorized users can access the presentation.

Directory Structure
php
Copy code
gesticulation-mapping/
│
├── database/
│   ├── <person1>/
│   │   ├── 1.png
│   │   ├── 2.png
│   │   └── ...
│   ├── <person2>/
│   │   ├── 1.png
│   │   ├── 2.png
│   │   └── ...
│   └── ...
│
├── FACE_DETECTION.py
├── haarcascade_frontalface_default.xml
├── HAND_GESTURE.py
└── Presentation/
    ├── slide1.jpg
    ├── slide2.jpg
    └── ...
Features
Hand Gesture Control: Navigate through slides using predefined hand gestures.
Face Detection: Authenticate users based on facial recognition before granting access to the presentation.
Methods Used
Face Detection (FACE_DETECTION.py)
The create_database() function initializes a database of authorized users by capturing images from the webcam. It uses OpenCV for image processing and face detection using Haar cascades. Here’s a breakdown:

Database Creation: Captures multiple images of each authorized user's face.
Image Processing: Enhances image contrast using histogram equalization.
Face Recognition: Trains a model using LBPH (Local Binary Patterns Histograms) to recognize authorized users during access.
Hand Gesture Control (HAND_GESTURE.py)
The HandDetector module from cvzone is used to detect and track hand gestures. Key features include:

Gesture Recognition: Identifies gestures such as left swipe (previous slide) and right swipe (next slide).
Annotation: Allows users to annotate slides using finger gestures.
Zooming: Implements zoom functionality based on hand gestures for detailed slide viewing.
Installation
Clone the repository:
bash
Copy code
git clone <repository-url>
cd gesticulation-mapping
Install dependencies:
Copy code
pip install -r requirements.txt
Usage
Face Database Initialization:

Run FACE_DETECTION.py to create a database of authorized users:
Copy code
python FACE_DETECTION.py
Follow the on-screen instructions to capture images for each authorized user.
Run Presentation Control:

Launch the slide control interface using HAND_GESTURE.py:
Copy code
python HAND_GESTURE.py
Perform hand gestures in front of the webcam to navigate slides and annotate presentations.
