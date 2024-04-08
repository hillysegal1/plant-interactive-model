

import streamlit as st
import numpy as np
import tensorflow as tf
import requests
from PIL import Image
from streamlit_lottie import st_lottie
import cv2
import re
def to_care():
  st.session_state['current_page'] ='plant_care'
#st.set_page_config(page_title="GROW", page_icon=":seedling:", layout="wide", initial_sidebar_state="expanded")

# Load the model

model = tf.keras.models.load_model("plant_disease_detection.h5")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_left = "https://lottie.host/560b514e-4adc-4c19-96f0-0081b166ae20/B0mMggaYqj.json"
lottie_url_right = "https://lottie.host/560b514e-4adc-4c19-96f0-0081b166ae20/B0mMggaYqj.json"

# Load Lottie animations
lottie_animation_left = load_lottieurl(lottie_url_left)
lottie_animation_right = load_lottieurl(lottie_url_right)



categories = {
    0: "Apple___Apple_scab",
    1: "Apple___Black_rot",
    2: "Apple___Cedar_apple_rust",
    3: "Apple___healthy",
    4: "Blueberry___healthy",
    5: "Cherry_(including_sour)___Powdery_mildew",
    6: "Cherry_(including_sour)___healthy",
    7: "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    8: "Corn_(maize)___Common_rust_",
    9: "Corn_(maize)___Northern_Leaf_Blight",
    10: "Corn_(maize)___healthy",
    11: "Grape___Black_rot",
    12: "Grape___Esca_(Black_Measles)",
    13: "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    14: "Grape___healthy",
    15: "Orange___Haunglongbing_(Citrus_greening)",
    16: "Peach___Bacterial_spot",
    17: "Peach___healthy",
    18: "Pepper,_bell___Bacterial_spot",
    19: "Pepper,_bell___healthy",
    20: "Potato___Early_blight",
    21: "Potato___Late_blight",
    22: "Potato___healthy",
    23: "Raspberry___healthy",
    24: "Soybean___healthy",
    25: "Squash___Powdery_mildew",
    26: "Strawberry___Leaf_scorch",
    27: "Strawberry___healthy",
    28: "Tomato___Bacterial_spot",
    29: "Tomato___Early_blight",
    30: "Tomato___Late_blight",
    31: "Tomato___Leaf_Mold",
    32: "Tomato___Septoria_leaf_spot",
    33: "Tomato___Spider_mites Two-spotted_spider_mite",
    34: "Tomato___Target_Spot",
    35: "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    36: "Tomato___Tomato_mosaic_virus",
    37: "Tomato___healthy"
}




# Function to preprocess image
def preprocess_image(image):
    # Resize image to match model input size
    img = tf.image.resize(image, (224, 224))
    # Normalize pixel values to [0, 1]
    img /= 255.0
    return img

# Function to predict disease
def predict_disease(image):
    # Preprocess the image
    img = preprocess_image(image)
    # Add batch dimension
    img = tf.expand_dims(img, axis=0)
    # Predict disease
    prediction = model.predict(img)
    # Get the predicted class
    predicted_class_index = tf.argmax(prediction, axis=1)[0].numpy()
    # Map the predicted class index to category
    predicted_class = categories[predicted_class_index]
    return predicted_class

# Streamlit app
def main():

    if st.button("Back"):
      to_care()
      st.rerun()

    col1, col2, col3 = st.columns([2, 6, 2])

    with col1:
      if lottie_animation_left:
          st_lottie(lottie_animation_left, height=100, key="left")
    with col2:
      st.markdown("""
      <div style="padding: 20px; text-align: center;">
          <h2 style='color: green;'>Plant Diagnosis</h2>
          <h3 style='color: green;'>Upload an image of your plant for a quick diagnosis</h3>
      </div>
      """, unsafe_allow_html=True)
    with col3:
      if lottie_animation_right:
          st_lottie(lottie_animation_right, height=100, key="right")
  # Use a single container for better control over layout
    container = st.container()


    uploaded_file = st.file_uploader("Upload an image of your plant here:", type=["jpg", "jpeg", "png"])


    if uploaded_file is not None:
        # Display the uploaded image
        image = tf.image.decode_image(uploaded_file.read(), channels=3)
        image = np.array(image)  # Convert TensorFlow eager tensor to NumPy array
        #st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("Diagnosing your plant...",  # Apply custom style to the classifying message
                unsafe_allow_html=True,
                style='font-size: 20px; color: #008000; font-weight: bold;')

        # Predict disease
        predicted_disease = predict_disease(image)
        predicted_disease = predicted_disease.replace("___", " - ").replace("_", " ")
        st.write('Diagnosis:', predicted_disease)



if __name__ == '__main__':
  main()
