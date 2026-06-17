import cv2
import mediapipe as mp

from mudra_classifier import MudraClassifier

class HandDetector:

    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils
        self.classifier = MudraClassifier()

    def detect_hands(self, frame):

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                landmark_list = []

                # Draw hand skeleton
                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

                # Store landmarks and display IDs
                for idx, landmark in enumerate(hand_landmarks.landmark):

                    h, w, c = frame.shape

                    x = int(landmark.x * w)
                    y = int(landmark.y * h)

                    landmark_list.append([idx, x, y])

                    cv2.putText(
                        frame,
                        str(idx),
                        (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 0),
                        1
                    )

                if len(landmark_list) != 0:
                    fingers=[]

                    if landmark_list[4][1] > landmark_list[3][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                    # Index Finger
                    if landmark_list[8][2] < landmark_list[6][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                    # Middle Finger
                    if landmark_list[12][2] < landmark_list[10][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                    # Ring Finger
                    if landmark_list[16][2] < landmark_list[14][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                    # Pinky Finger
                    if landmark_list[20][2] < landmark_list[18][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                    cv2.putText(
                        frame,
                        f"Fingers: {fingers}",
                        (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 0),
                        2
                    )

                    mudra = self.classifier.classify(fingers)
                    cv2.putText(
                        frame,
                        f"Mudra: {mudra}",
                        (10, 80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 0),
                        2
                    )
                       
                    

        return frame