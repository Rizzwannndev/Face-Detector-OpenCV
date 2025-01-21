# Face Detector Using OpenCV
This project demonstrates real-time face detection using OpenCV, a powerful open-source computer vision library. The application uses a Haar Cascade Classifier to detect faces in a live video feed captured from a webcam.<br><br>
The project is designed as an introduction to face detection techniques and can serve as a foundation for more advanced computer vision applications.
<br><br>

## Features
* Real-Time Face Detection: Detects faces in real-time from a live webcam feed.
* Haar Cascade Classifier: Utilizes a pre-trained Haar Cascade model for face detection.
* Visualization: Draws bounding boxes around detected faces on the video feed.
<br>

## Prerequisites
To run this project, ensure you have the following installed:

Python 3.7 or above.<br>
OpenCV library (cv2).
You can install OpenCV using pip:<br>

    pip install opencv-pyhton    

## How It Works

1. Video Capture: The program uses OpenCV to access the webcam and capture frames in real-time.
2. Grayscale Conversion: Each frame is converted to grayscale for efficient face detection.
3. Face Detection: The Haar Cascade Classifier scans the image to detect faces, returning bounding box coordinates.
4. Drawing Bounding Boxes: Detected faces are highlighted with green rectangles on the video feed.

## Output
When the script runs successfully, the webcam feed will appear in a new window, and faces detected in the frame will be highlighted with green rectangles.

<br>
Project Made By:  <a src = "https://www.instagram.com/rizwanwaseem_/profilecard/?igsh=NGM1NGh6aTlzanEy" target=_blanck>Rizwan Waseem</a>