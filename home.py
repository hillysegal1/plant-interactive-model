
import streamlit as st
from streamlit_lottie import st_lottie
import requests
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_url_left = "https://lottie.host/21d43043-eda8-4e0e-9e42-0a6dd9052dce/UseMpwrFnR.json"
lottie_url_right = "https://lottie.host/21d43043-eda8-4e0e-9e42-0a6dd9052dce/UseMpwrFnR.json"

# Load Lottie animations
lottie_animation_left = load_lottieurl(lottie_url_left)
lottie_animation_right = load_lottieurl(lottie_url_right)

def main():
  col1, col2, col3 = st.columns([2, 6, 2])

  with col1:
      if lottie_animation_left:
          st_lottie(lottie_animation_left, height=100, key="left")

  with col2:
      st.markdown("""
            <h1 style='text-align: center; color: green;'>Welcome to GROW</h1>
            <h3 style='text-align: center; color: green;'>~The place to start with your plant growing journey~</h3>
            """, unsafe_allow_html=True)

  with col3:
      if lottie_animation_right:
          st_lottie(lottie_animation_right, height=100, key="right")

  # Using columns within the container to place the buttons
  # Adjust the column ratios if necessary to better center the buttons
  container = st.container()
  _, btn_col1, btn_col2, _ = st.columns([2, 3, 3, 2])

  with btn_col1:
      st.markdown("""
      <div style="padding: 20px; text-align: center;">
          <h2 style='color: green;'>Plant Selection</h2>
          <h3 style='color: green;'> Click below to get started <br> by finding the right plant for you </h3>
      </div>
      """, unsafe_allow_html=True)
      if st.button('Plant Selection', key='select'):
          st.session_state['current_page'] = 'findPlant'

  with btn_col2:
      st.markdown("""
      <div style="padding: 20px; text-align: center;">
          <h2 style='color: green;'>Plant Care</h2>
          <h3 style='color: green;'> Click below to find out how <br>to properly care for your plants </h3>
      </div>
      """, unsafe_allow_html=True)
      if st.button('Plant Care', key='care'):
          st.session_state['current_page'] = 'plant_care'

if __name__ == '__main__':
  main()
