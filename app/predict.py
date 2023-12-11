from PIL import Image
from io import BytesIO
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

input_shape = (224, 224)

model1 = load_model('models/Binary_ResNet1')
model2 = load_model('models/Binary_ResNet2')

def read_image(image_encoded):
    pil_image = Image.open(image_encoded)
    return pil_image

def preprocess(image: Image.Image):
    image = image.convert('RGB')  # Convert to RGB
    image = image.resize(input_shape)
    image = img_to_array(image)
    image = image / 255
    # Return the preprocessed image
    return image

def predict_1(image: np.ndarray):
    # Add batch dimension to the input image
    image = np.expand_dims(image, axis=0)
    threshold = 0.5
    
    if model1.predict(image)[0] >= threshold:
        return ("some algae", model1.predict(image)[0])
    else:
        return ("No Advisory", (1 - model1.predict(image)[0]))
    
def predict_2(image: np.ndarray):
    # Add batch dimension to the input image
    image = np.expand_dims(image, axis=0)
    threshold = 0.5
    
    if model2.predict(image)[0] >= threshold:
        # can maybe make this markdown if you want to bold some stuff
        return ("Dangerous", model2.predict(image)[0])
    else:
        return ("Caution", (1 - model2.predict(image)[0]))