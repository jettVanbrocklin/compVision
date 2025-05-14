import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

#load the model you trained
model = load_model("my_custom_classifier.h5")

# Load and preprocess a test image
img = image.load_img("day16/test/test_dog.jpg", target_size=(128, 128))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis = 0) # Shape: (1, 128, 128, 3)
img_array /= 255.0 # Rescale like training data


# Predict
pred = model.predict(img_array)
class_index = np.argmax(pred)
confidence = np.max(pred)

print(f"Prediction: {list(train_data.class_indices.keys())[class_index]} ({confidence: .2f})")