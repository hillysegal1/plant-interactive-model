
import streamlit as st
import pathlib
import textwrap
import streamlit as st
import numpy as np
from streamlit_lottie import st_lottie
import tensorflow as tf
from PIL import Image
import cv2
import re
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import requests


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def strip_numbers_and_punctuation(text):
    # Define the pattern to match digits and punctuation
    pattern = r'[0-9!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]'
    stripped_text = re.sub(pattern, '', text)
    return stripped_text

def back():
  if st.session_state['shared_string'] != "hi":
    st.session_state['current_page'] = 'recommendation'
  else:
    st.session_state['current_page'] = 'care'

lottie_url_left = "https://lottie.host/3d899a76-e79e-4c15-8825-6a9154544c8b/Z4OCRtHR3P.json"
lottie_url_right = "https://lottie.host/3d899a76-e79e-4c15-8825-6a9154544c8b/Z4OCRtHR3P.json"

# Load Lottie animations
lottie_animation_left = load_lottieurl(lottie_url_left)
lottie_animation_right = load_lottieurl(lottie_url_right)


def main():
  if st.button("back"):
    back()
  col1, col2, col3 = st.columns([2, 6, 2])

  with col1:
    if lottie_animation_left:
        st_lottie(lottie_animation_left, height=100, key="left")

  s = str(st.session_state['p_name'])
  name = re.sub(r'[\d.]+', '', s)
  prompt = "write a couple of lines about"+ ''+name+" ,for example this is information about tomatoes:"+"Tomato plants are known for their versatile fruits that range in color and size. They thrive in warm conditions with plenty of sunlight, requiring well-drained soil and regular care ."
  GOOGLE_API_KEY= API_KEY
  genai.configure(api_key=GOOGLE_API_KEY)
  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content(
      prompt,
      generation_config=genai.types.GenerationConfig(
          # Only one candidate for now.
          candidate_count=1,
          temperature=0.65)
  )
  inform = response.text

  examp = "Select a site that receives at least 6 to 8 hours of direct sunlight per day. Prepare the soil by incorporating compost or well-rotted manure to improve fertility and drainage. The ideal soil pH for tomatoes is between 6.0 and 6.8. Plant tomato seedlings about 18 to 24 inches apart in rows spaced 3 to 4 feet apart. This spacing allows for adequate air circulation and room for growth. Plant seedlings deeply, burying two-thirds of the stem, to encourage strong root development. Water the plants thoroughly at the time of planting. Provide support for your tomato plants with stakes, cages, or trellises. Ensure your tomato plants receive full sun, which is crucial for their growth and fruit production."
  prompt = "how do i grow"+ name+"? i need information about where and when to plant and some general tips, write a paragraph"
  response = model.generate_content(
      prompt,
      generation_config=genai.types.GenerationConfig(
          # Only one candidate for now.
          candidate_count=1,
          temperature=0.65)
  )
  growing = response.text
  examp = "Water tomato plants deeply once a week, increasing to twice a week in hot or dry weather. After planting, mulch to retain moisture, stake or cage for support, remove suckers if desired for larger fruits, and monitor for pests and diseases. Regularly check soil moisture and adjust watering accordingly."
  prompt = "write 4-5 lines explaining how to water and care for"+ name+", for example this is how you should write about tomatoes: "+ examp
  response = model.generate_content(
      prompt,
      generation_config=genai.types.GenerationConfig(
          # Only one candidate for now.
          candidate_count=1,
          temperature=0.6)
  )
  watering = response.text
  with col2:
    st.markdown(f"""
          <h1 style='text-align: center; color: green;'>Plant Care </h1>
          <h3 style='text-align: center; color: green;'>{name}</h3>
          """, unsafe_allow_html=True)

    st.markdown(inform)
    st.markdown("""
          <h3 style='text-align: center; color: green;'>The Growing Process</h3>
          """, unsafe_allow_html=True)
    st.markdown(growing)
    st.markdown("""
          <h3 style='text-align: center; color: green;'>Watering and Care </h3>
          """, unsafe_allow_html=True)
    st.markdown(watering)
  with col3:
      if lottie_animation_right:
          st_lottie(lottie_animation_right, height=100, key="right")

if __name__ == '__main__':
  main()
