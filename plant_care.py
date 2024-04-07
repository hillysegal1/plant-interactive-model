import streamlit as st
from streamlit_lottie import st_lottie
import requests
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_url_left = "https://lottie.host/9e1a8a7c-11e9-4eb2-a52d-ab2e71e4af47/v9iwmsaY9Q.json"
lottie_url_right = "https://lottie.host/9e1a8a7c-11e9-4eb2-a52d-ab2e71e4af47/v9iwmsaY9Q.json"

# Load Lottie animations
lottie_animation_left = load_lottieurl(lottie_url_left)
lottie_animation_right = load_lottieurl(lottie_url_right)

def go_home():
  st.session_state['current_page'] = 'home'
# Set page title and icon
def diagnose():
  st.session_state['current_page'] = 'plant_diagnosis'
def go_to_care():
    st.session_state['current_page'] = 'care'
    st.experimental_rerun()  # Force a rerun to update the UI

def main():
  if st.button("Back"):
    go_home()
  # Set background color and center the title and subtitle
  col1, col2, col3 = st.columns([2, 6, 2])

  with col1:
    if lottie_animation_left:
        st_lottie(lottie_animation_left, height=200, key="left")

  with col2:
    st.markdown("""
          <h1 style='text-align: center; color: green;'>Plant Care</h1>
          <h3 style='text-align: center; color: green;'>~Get started on caring for your plant~</h3>
          """, unsafe_allow_html=True)

  with col3:
    if lottie_animation_right:
        st_lottie(lottie_animation_right, height=200, key="right")
  # Use a single container for better control over layout
  container = st.container()

  _, btn_col1, btn_col2, _ = st.columns([1.5, 3, 3, 1.5])

  with btn_col1:
      st.markdown("""
      <div style="padding: 20px; text-align: center;">
          <h2 style='color: green;'>Plant Diagnosis</h2>
          <h3 style='color: green;'> Is your plant sick? <br>Click here to diagnose your plant </h3>
      </div>
      """, unsafe_allow_html=True)
      if st.button('Plant Diagnosis'):
        diagnose()

  with btn_col2:
      st.markdown("""
      <div style="padding: 20px; text-align: center;">
          <h2 style='color: green;'>Care for your Plant</h2>
          <h3 style='color: green;'> Click here for information tailored <br> to your plant</h3>
      </div>
      """, unsafe_allow_html=True)
      if st.button('Care for your Plant'):
        go_to_care()


if __name__ == '__main__':
  main()
