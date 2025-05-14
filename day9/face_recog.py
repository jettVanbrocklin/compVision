import cv2
import mediapipe as mp

mp_face = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_face.FaceDetection(model_selection = 0, min_detection_confidence = 0.5) as face_detector:
    while True:
        ret, frame = cap.read()
        if not ret:
            break


        #Convert to RGB (Mediapipe uses RGB)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detector.process(rgb_frame)

        # Draw Bounding Face Boxes
        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)

        cv2.imshow("Mediapipe Face Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()