
import os
import streamlit as st
import pathlib
import textwrap
import numpy as np
import tensorflow as tf
from PIL import Image
import cv2
import re
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown


def process(responses):
    # Starting the prompt with basic user abilities information
    prompt = f"I need 4 plant recommendations for this user: user abilities: {responses['expertise_level']}"

    # Adding care availability information
    care_availability_mapping = {
        "Everyday": ", can water daily",
        "Every couple of days": ", can water every couple of days",
        "I forget to care for my plants": ", can water rarely"
    }
    prompt += care_availability_mapping.get(responses["care_availability"], "")

    # Adding user requirements
    prompt += " user requirements: suitable to plant in " + responses["grow_month"]
    prompt += " in a " + responses["climate"]+ "climate"

    if responses["own_pets"] == 'Yes':
        prompt += ", must be safe for pets"

    prompt += f" the plant will grow in: a {responses['grow_location']} "

    if responses["natural_light"] == 'Yes':
        prompt += ", the plant will have access to plenty of natural light"
    else:
        prompt += ", the plant won't have access to a lot of natural light"

    prompt += f", the user prefers to grow {responses['plant_type']}.+the response should be in this form : ""plant name: a paragraph explaining to the user why you chose it and some information about the plant """

    return (prompt)
def response_p(p):
  import google.generativeai as genai
  GOOGLE_API_KEY= API_KEY
  genai.configure(api_key=GOOGLE_API_KEY)
  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content(
      p,
      generation_config=genai.types.GenerationConfig(
          # Only one candidate for now.
          candidate_count=1,
          temperature=0.55)
  )
  return response.text
def go_home():
  st.session_state['current_page'] = 'home'

def clicked(user_input):
  p = process(user_input)
  st.session_state['shared_string'] = p
  st.session_state['ran'] = response_p(p)
  st.session_state['current_page'] = 'recommendation'

def main():
  if st.button("Back"):
    go_home()
  st.markdown("""
      <h1 style='text-align: center; color: green;'>Plant Selection</h1>
      <p style='text-align: center; color: green;'>Complete the questionnaire below to find the plant that’s right <br>for you</p>
      """, unsafe_allow_html=True)
  # Display the questions and collect answers.
  grow_location = st.radio(
      "Where do you plan on growing the plant?",
      ('Garden', 'Balcony', 'Indoors'))

  natural_light = st.radio(
      "Will your plant have access to natural light?",
      ('No', 'Yes'))

  own_pets = st.radio(
      "Do you own any pets?",
      ('No', 'Yes'))

  grow_month = st.selectbox(
      "When do you want to grow your plant? (Select a month)",
      ('January', 'February', 'March', 'April', 'May', 'June',
      'July', 'August', 'September', 'October', 'November', 'December'))

  climate = st.selectbox(
      "What is the climate in your region?",
      ('Tropical', 'Dry', 'Temperate', 'Continental', 'Polar'))

  plant_type = st.radio(
      "What type of plant do you want to grow?",
      ('Vegetable', 'Fruit', 'Flower'))

  expertise_level = st.radio(
      "What is your level of expertise in growing plants?",
      ('Beginner', 'Intermediate', 'Expert'))

  care_availability = st.radio(
      "What is your level of availability for plant care?",
      ('Everyday', 'Every couple of days', 'I forget to care for my plants'))
  if st.button('submit'):
    user_input = {
        'grow_location': grow_location,
        'natural_light': natural_light,
        'own_pets': own_pets,
        'grow_month': grow_month,
        'climate': climate,
        'plant_type': plant_type,
        'expertise_level': expertise_level,
        'care_availability': care_availability,
    }
    clicked(user_input)

if __name__ == '__main__':
  main()

