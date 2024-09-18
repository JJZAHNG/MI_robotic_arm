# Hand Gesture Controlled Robotic Arm

## Overview

This project allows you to control a robotic arm using hand gestures captured from a webcam. The application uses MediaPipe for hand detection and tracking, OpenCV for image processing, and sends commands to the robotic arm over a network using HTTP requests.

---

## Project Structure

```bash
project/
│
├── config.py               # Configuration file for IP address and camera index
├── video_capture.py        # Handles video capture from the camera
├── hand_detection.py       # Detects hand and extracts landmarks using MediaPipe
├── gesture_recognition.py  # Recognizes gestures based on landmarks
├── command_sender.py       # Constructs and sends commands to the robotic arm
├── utils.py                # Utility functions (optional)
├── main.py                 # Main program to run the application
└── requirements.txt        # List of required Python packages


## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/project.git
cd project
```

Install the required packages:
```bash
pip install -r requirements.txt
```

The requirements.txt file includes:
```makefile
mediapipe==0.10.0
opencv-python
requests
```

# Usage
Run the application using:

```bash
python main.py
```

### Module Descriptions
#####: config.py
Contains configuration parameters:

##### IP_ADDR: The IP address of the robotic arm.
CAMERA_INDEX: The index of the camera (default is 0 for the built-in webcam).

##### video_capture.py
Handles video capture from the specified camera.

##### VideoCapture class:
read_frame(): Reads a frame from the camera.
release(): Releases the camera resource.

##### hand_detection.py
Uses MediaPipe to detect hands and extract landmarks.

##### HandDetector class:
find_hands(image, draw=True): Processes the image to find hands and optionally draws the landmarks.
release(): Closes the MediaPipe Hands resource.

##### gesture_recognition.py
Processes landmarks to recognize gestures.

##### GestureRecognizer class:
get_landmark_positions(hand_landmarks): Converts normalized landmarks to pixel coordinates.
recognize_gesture(landmark_positions): Recognizes gestures and calculates necessary parameters.

##### command_sender.py
Constructs and sends commands to the robotic arm.

##### CommandSender class:
send_command(gesture_info): Constructs a JSON command based on gesture information and sends it via HTTP GET request.

##### main.py
The main program that integrates all modules.

Students can modify this file to implement their own logic, such as:

##### Initializing modules.
Reading frames and processing images.
Detecting hands and recognizing gestures.
Sending commands to the robotic arm.
Adding custom gesture controls.

##### Additional Notes
Ensure that the robotic arm is connected to the same network and accessible via the specified IP address.
The application uses the default camera. If you have multiple cameras, adjust the CAMERA_INDEX in config.py.
You may need to calibrate the parameters in gesture_recognition.py and command_sender.py to match your setup.

##### Troubleshooting
Missing Packages: If you encounter errors related to missing packages, ensure that you have installed all dependencies using pip install -r requirements.txt.
Hand Not Detected: If the hand is not being detected, check your lighting conditions and ensure that the camera is functioning properly.
Connection Issues: If commands are not reaching the robotic arm, verify the network connection and IP address in config.py.
