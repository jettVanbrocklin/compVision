import cv2
import numpy as np
import tensorflow as tf

from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2, decode_predictions, preprocess_input
)

# Load the pretrained model

model = MobileNetV2(weights = "imagenet")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preporcess the frame
    img = cv2.resize(frame, (224, 224))
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    x = np.expand_dims(img_rgb, axis = 0)
    x = preprocess_input(x)

    # Predict
    preds = model.predict(x)
    label = decode_predictions(preds, top=1)[0][0][1] # get label
    confidence = decode_predictions(preds, top = 1)[0][0][2]

    cv2.putText(frame, f"{label}: {confidence:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("MobileNetV2 Classification", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows

