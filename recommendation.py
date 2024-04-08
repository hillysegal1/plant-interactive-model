
import streamlit as st
import textwrap
import google.generativeai as genai
from IPython.display import Markdown
import re
import string
import os




def redo():
    p = st.session_state['shared_string']
    GOOGLE_API_KEY = API_KEY
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(
        p,
        generation_config=genai.types.GenerationConfig(
            # Only one candidate for now.
            candidate_count=1,
            temperature=0.55)
    )
    st.session_state['ran'] = response.text
    st.session_state['current_page'] = 'recommendation'

def how_click(name):
    st.session_state['p_name'] = name
    st.session_state['current_page'] = 'how_to'

def to_markdown(text):
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def go_to_quiz():
    st.session_state['current_page'] = 'findPlant'

def res():
    if st.button("Back"):
        go_to_quiz()
        st.rerun()
    else:
        st.markdown("""
            <h1 style='text-align: center; color: green;'>Plant Recommendations</h1>
            <p style='text-align: center; color: green;'> We've curated a selection of plants tailored to your preferences and requirements</p>
            """, unsafe_allow_html=True)

        ran = st.session_state.get('ran', '')  # Get recommendations from session state
        lines = ran.replace('*', '')
        lines = "\n".join(line.strip() for line in lines.split('\n') if line.strip())  # Remove leading/trailing whitespace
        lines = lines.split('\n')

        names = {}
        i=1
        for index, line in enumerate(lines):
            if index % 2 == 0:
              parts= line
              plant_name = f"{i}.{parts.split(':')[1]}"
              name=f"{parts.split(':')[1].strip()}"
              info = lines[index+1]

              # Displaying the part with a green colored font using HTML within the Streamlit markdown
              st.markdown(f'<span style="color:green;"><strong>{plant_name}</strong></span>', unsafe_allow_html=True)
              st.markdown(f'<span style="color:green;"><strong></strong></span> {info}', unsafe_allow_html=True)

              # Preparing a unique key for the button to avoid duplication
              button_key = f"button_{index}"

              # Creating a button that, when clicked, provides care instructions for the item
              if st.button(f"How to Care for {name}", key=button_key):
                  how_click(name)
                  st.rerun()
              i+=1
    st.markdown("&nbsp;")  # Add empty space
    st.markdown("<h3 style='color:green'>Not satisfied with your results? <br> Click the button to try again</h3>", unsafe_allow_html=True)
    if st.button("Try again"):
      redo()
      st.rerun()


def main():
    res()

if __name__ == '__main__':
    main()
