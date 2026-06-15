import cv2
from hand_detector import HandDetector

cap = cv2.VideoCapture(0)

detector = HandDetector()

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = detector.detect_hands(frame)

    cv2.imshow("Mudra Detector", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()