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
```
  pip install numpy cvzone mediapipe
  ```
### Prerequisites

- Python 3.7

#### Usage 🖥️
1. **Face Database Initialization**:
- Run `FACE_DETECTION.py` to create a database of authorized users:
  ```
  python FACE_DETECTION.py
  ```
- Follow the on-screen instructions to capture images for each authorized user.

2. **Presentation Control**:
- Launch the slide control interface using `HAND_GESTURE.py`( will run automatically if user face is recognized):
  ```
  python HAND_GESTURE.py
  ```
- Perform hand gestures in front of the webcam to navigate slides and annotate presentations.
- Control the Presentation:
   - Use hand gestures to navigate through the slides.
   - The following gestures are recognized.
      - All fingers up: Move to the previous slide.
      - All fingers down: Move to the next slide.
      - Index and middle finger up: Draw on the current slide.
      - Index finger up: Start drawing annotations.
      - Three middle fingers up: Remove the last annotation.

#### Demo Images
1. **Face Detection and Recognition in Action**:

- ![face](https://github.com/prasanna-ravi12/Gesture-controlled-PPT-with-face-detection/assets/175058249/dd8c3588-9b23-4ade-afb2-f26355fda611)

2. **Hand Gesture for Slide Navigation**:

- <img width="1041" alt="Screenshot 2024-07-11 at 1 30 00 AM" src="https://github.com/prasanna-ravi12/Gesture-controlled-PPT-with-face-detection/assets/175058249/c71d990c-af56-4354-83e2-aadd8c17f9d0">
### Conclusion

**Gesticulation Mapping** combines the power of hand gesture recognition and facial detection to revolutionize how presentations are controlled. By leveraging computer vision techniques, this project not only enhances user interaction but also ensures security through biometric authentication.

Explore the functionalities provided by this project and contribute to its development. Your feedback and contributions are highly appreciated!

#### Get Started
Follow the installation instructions to set up Gesticulation Mapping on your local machine. Experience seamless slide navigation and annotation with just your gestures and the power of computer vision.

#### Contact
For any questions or suggestions, feel free to reach out:
- linkedin: [Your LinkedIn Profile](https://www.linkedin.com/in/prasanna-ravi-r-a9a67a244)

#### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

#### Acknowledgments
- Acknowledge contributors or libraries used in the project.
- Express gratitude to any individuals or organizations that supported the project development.





   








