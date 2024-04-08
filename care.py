
import streamlit as st
def to_care():
  st.session_state['current_page'] ='plant_care'

def main():
  if st.button("Back"):
      to_care()
      st.rerun()
  st.markdown("""
      <h1 style='text-align: center; color: green;'>Care for your Plant</h1>
      <h3 style='text-align: center; color: green;'>Enter your plant’s name to learn how to care for it</he>
      """, unsafe_allow_html=True)
  user_input = st.text_input("Enter your plants name:")

  if st.button('Submit'):
      # Display the submitted text
      st.session_state['shared_string'] = "hi"
      st.session_state['p_name'] = user_input
      st.session_state['current_page'] = 'how_to'
      st.rerun()
  image_path = "im.png"
  st.image(image_path)
if __name__ == '__main__':
  main()



