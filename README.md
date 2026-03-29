# ErgoVision – Posture Detection System

ErgoVision is a computer vision project that monitors a user's sitting posture using a webcam and detects slouching in real time.
The system uses MediaPipe Pose to detect body landmarks and calculates the neck angle to determine whether the user has good posture or is slouching.

# Project Features

* Real-time posture monitoring using webcam
* Detects slouching posture
* Displays posture status on the screen
* Calculates neck angle using ear, shoulder, and hip landmarks

# Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy

# System Requirements

Before running the project, make sure the following are installed:

* Python 3.9 or later
* A webcam
* Internet connection (for installing dependencies)

# Project Setup Instructions

Follow these steps to set up and run the project from the command line.

## Step 1: Clone the Repository

Open a terminal and run:

git clone https://github.com/MahiSaxena/ErgoVision.git

Then navigate to the project folder:

cd ErgoVision

## Step 2: Install Dependencies

Install the required Python libraries using:

pip install -r requirements.txt

If the requirements file is not available, install manually:

pip install opencv-python mediapipe numpy

## Step 3: Run the Program

Run the posture detection program using:

python posture_monitor.py

# How the System Works

1. The webcam captures live video input.
2. MediaPipe detects body landmarks.
3. The program extracts the coordinates of the ear, shoulder, and hip.
4. The neck angle is calculated using these points.
5. If the angle crosses a threshold, the system detects slouching and displays a warning.