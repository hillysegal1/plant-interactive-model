### Plant-Interactive-System
# Overview:
Our plant system aims to assist users in selecting and caring for plants at home. It provides personalized recommendations for suitable plants based on users' living conditions and preferences. Additionally, it offers comprehensive care guidelines and plant problem diagnosis to ensure healthy plant growth.
Our system is designed using Streamlit. 

# System Description:
Upon accessing the system's homepage, users are presented with two options: "Plant Selection" and "Plant Care". The "Plant Selection" page assists users in finding a plant that aligns with their preferences and environment by providing them with a series of multiple-choice questions. Upon submission, users receive personalized plant suggestions along with plant descriptions. The "Plant Care" page offers two main functionalities: "Plant Diagnosis" and "Care for your Plant".

# Getting Started:
## Setting up the Development Environment:
To set up the development environment follow these steps:
1. Install Streamlit:
    ```bash
    pip install streamlit -q
    ```
2. Retrieve external IPv4 address:
    ```bash
    wget -q -O - ipv4.icanhazip.com
    ```
3. Upgrade google-generativeai:
    ```bash
    pip install -q -U google-generativeai
    ```
4. Install Streamlit Lottie extension:
    ```bash
    pip install streamlit-lottie
    ```
5. After installation a 'port number' should appear, e.g: 34.81.101.203, save this number.
   
## Running the System: 
To run the project, follow these steps: 
1. This project uses Gemini API, in "env.txt" enter your personal Gemini API key.
   Your personal key can be found in: https://ai.google.dev/
1. Run all python files in main application, run app.py last.
2. Run the command:
   ```bash
   streamlit run app.py & npx localtunnel --port 8501
   ```
3. Select the third hyper link that appears in the following format: your url is: https://tender-melons-make.loca.lt
4. In the new page eneter your port number from step 5. in "Setting up the Development Environment".

# Usage:
1. A detailed instruction on how to use the system is provided in the demo video: ----
2. Example images for the plant diagnosis feature (plant_diagnosis.py) can be found in "plant_images" folder.

# Plant Diagnosis Algorithm:
The system uses a MobileNet V2 model for plant diagnosis, a lightweight CNN model pretrained on the ImageNet Dataset. Transfer learning is applied to this model, adding additional layers for classification. Early stopping is implemented during training to avoid overfitting, and an Adam optimizer and categorical cross-entropy loss function are used. Upon receiving an image of a plant, the model outputs a probability distribution across 38 classes, representing various plant diseases or conditions.
This model is provided in the "models" folder. 

# Gemini API Usage:
The Gemini API is utilized for processing user inputs, generating personalized plant recommendations, and providing care instructions. Relevant prompts are supplied on each page to receive suitable and personalized answers from users.


 
