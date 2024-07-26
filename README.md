# Need-For-Speed-Carbon-Gameplay-Using-Hand-Gestures

## Introduction

This project demonstrates a gesture-based control system for the game NFS Carbon using computer vision. The system uses a webcam to capture hand gestures and translates these gestures into in-game actions such as accelerating, braking, and steering.

## Features

- **Gesture Recognition:** Utilizes the MediaPipe library to recognize hand gestures in real-time.
- **In-Game Control:** Maps recognized gestures to in-game actions using simulated key presses.
- **Hands-Free Gaming:** Provides an intuitive and immersive gaming experience without the need for traditional controllers.

## How It Works

1. **Hand Tracking and Gesture Recognition:**
   - The `mediapipe` library is used to track hand movements and recognize gestures.
   - Key points on the hand are identified and analyzed to determine specific gestures.

2. **Key Press Simulation:**
   - The `directkeys.py` script uses the `ctypes` library to simulate key presses.
   - Depending on the recognized gesture, the script sends the corresponding key press commands to control the game.

3. **Game Control Logic:**
   - The `gameControl.py` script captures webcam input, processes hand landmarks, and triggers key presses based on gesture detection.
   - Various gestures are mapped to specific game actions:
     - **Open Hand (5 fingers):** Accelerate
     - **Fist (0 fingers):** Brake
     - **Two Fingers:** Turn Left
     - **Three Fingers:** Turn Right

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/fahadyousuf2003/gesture-control-nfs-carbon.git
   cd gesture-control-nfs-carbon

2. **Install the required packages using the following command:**
   ```bash
   pip install opencv-python mediapipe

## Usage

1. **Run the Game Control Script:**
   ```bash
   python gameControl.py
   
2. **Webcam Setup:**

    Ensure your webcam is connected and positioned correctly to capture your hand gestures.

## Control the Game:

Use the following hand gestures to control the game:

  -Open Hand (5 fingers): Accelerate
  -Fist (0 fingers): Brake
  -Two Fingers: Turn Left
  -Three Fingers: Turn Right
  -Quit the Application:


## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any inquiries or feedback, please contact fahadyousuf344@gmail.com.
