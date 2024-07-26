
import cv2
import mediapipe as mp
import time
from directkeys import W, A, S, D
from directkeys import PressKey, ReleaseKey

# Define keys
break_key_pressed = S
accelerato_key_pressed = W
left_key_pressed = A
right_key_pressed = D

# Initialize time delay
time.sleep(2.0)
current_key_pressed = set()

# Initialize MediaPipe Hands
mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

# Tip IDs for fingers
tipIds = [4, 8, 12, 16, 20]

# Initialize webcam
video = cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        keyPressed = False
        ret, image = video.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        lmList = []
        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmark.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)

        fingers = []
        if len(lmList) != 0:
            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            # Fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total = fingers.count(1)

            if total == 0:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "BRAKE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
                PressKey(break_key_pressed)
                current_key_pressed.add(break_key_pressed)
                keyPressed = True

            elif total == 5:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "GAS", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
                PressKey(accelerato_key_pressed)
                current_key_pressed.add(accelerato_key_pressed)
                keyPressed = True

            elif total == 2:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "LEFT", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
                PressKey(left_key_pressed)
                PressKey(accelerato_key_pressed)
                current_key_pressed.add(left_key_pressed)
                current_key_pressed.add(accelerato_key_pressed)
                keyPressed = True

            elif total == 3:
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "RIGHT", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
                PressKey(right_key_pressed)
                PressKey(accelerato_key_pressed)
                current_key_pressed.add(right_key_pressed)
                current_key_pressed.add(accelerato_key_pressed)
                keyPressed = True

        if not keyPressed and len(current_key_pressed) != 0:
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed = set()

        cv2.imshow("Frame", image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

video.release()
cv2.destroyAllWindows()
