import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Set up image preprocessing
train_gen = ImageDataGenerator(rescale = 1./255, validation_split = 0.2)

train_data = train_gen.flow_from_directory(
        'day16/dataset',
        target_size = (128, 128),
        batch_size = 16,
        class_mode = 'categorical',
        subset = 'training'
    )

val_data = train_gen.flow_from_directory(
    'day16/dataset',
    target_size = (128, 128),
    batch_size = 16,
    class_mode = 'categorical',
    subset = 'validation'
)

# Build the model
model = Sequential([
    Conv2D(32, (3, 3), activation = 'relu', input_shape = (128, 128, 3)),
    MaxPooling2D(2,2), 
    Conv2D(64, (3,3), activation = 'relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(64, activation = 'relu'),
    Dense(train_data.num_classes, activation = 'softmax')
])

# Compile and train
model.compile(optimizer = 'adam',
              loss = 'categorical_crossentropy',
              metrics = ['accuracy'])


#print(train_data.class_indices)
model.fit(train_data, validation_data = val_data, epochs = 10)
model.save("my_custom_classifier.h5")

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