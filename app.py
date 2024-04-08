
import streamlit as st
import home, findPlant, plant_diagnosis, plant_care,recommendation, how_to, care


import os


# Now run your Streamlit app code
# Your app code goes here

st.set_page_config(page_title="GROW", page_icon=":seedling:", layout="wide", initial_sidebar_state="expanded")

def main():
    # Set up the navigation between pages
    pages = {
        'home': home.main,
        'findPlant': findPlant.main,
        'plant_diagnosis': plant_diagnosis.main,
        'plant_care': plant_care.main,
        'recommendation': recommendation.main,
        'care' : care.main,
        'how_to' : how_to.main
    }

    # Get the current page from the session state
    current_page = st.session_state.get('current_page', 'home')

    # Render the current page if it exists in the pages dictionary
    if current_page in pages:
      pages[current_page]()

if __name__ == "__main__":
    main()
