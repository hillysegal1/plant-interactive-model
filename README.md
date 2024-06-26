### Plant-Interactive-System
# Overview:
Our plant system aims to assist users in selecting and caring for plants at home. It provides personalized recommendations for suitable plants based on users' living conditions and preferences. Additionally, it offers comprehensive care guidelines and plant problem diagnosis to ensure healthy plant growth.
Our system is designed using Streamlit. 

# System Description:
Upon accessing the system's homepage, users are presented with two options: "Plant Selection" and "Plant Care". The "Plant Selection" page assists users in finding a plant that aligns with their preferences and environment by providing them with a series of multiple-choice questions. Upon submission, users receive personalized plant suggestions along with plant descriptions. The "Plant Care" page offers two main functionalities: "Plant Diagnosis" and "Care for your Plant".

# Getting Started:
## Setting up the Development Environment:
Pre-requisites: Git and Anaconda. 

To install and run the code on your local machine, follow these steps:
1. ### Clone the repository
   First, clone the repository to your local machine using Git. Open a terminal and run the following command:
    ```bash
    git clone https://github.com/hillysegal1/plant-interactive-model
    ```
2. ### Create and activate the conda environment
   After cloning the repository, navigate into the project directory:
    ```bash
    cd plant-interactive-model
    ```
    Then, use the following command to create a conda environment from the environment.yml file provided in the project:
    ```bash
    conda env create -f environment.yml
    ```
    Activate the environment with the following command:
   ```bash
    conda activate plant_system_env
    ```
  
## Running the System: 
To run the project, follow these steps: 
1. To use the Gemini API in this project, you need to authenticate with your API key. Your personal key can be found in: 
   https://ai.google.dev/.

   Copy your key and run the following command in the terminal:

   For Windows:
   ```bash
   set API_KEY=your_api_key
   ```

   For Linux and macOS:
   ```bash
   export API_KEY=your_api_key

   ```
   
3. Run the command:
   ```bash
   streamlit run app.py 
   ```

# Usage:
1. A detailed instruction on how to use the system is provided in the demo video: https://drive.google.com/file/d/1-YIspW0yPgMT1NqGIU5t8ByKA6X858x0/view?pli=1
   
2. Example images for the plant diagnosis feature (plant_diagnosis.py) can be found in "plant_images" folder.

# Plant Diagnosis Algorithm:
The system uses a MobileNet V2 model for plant diagnosis, a lightweight CNN model pretrained on the ImageNet Dataset. Transfer learning is applied to this model, adding additional layers for classification. Early stopping is implemented during training to avoid overfitting, and an Adam optimizer and categorical cross-entropy loss function are used. Upon receiving an image of a plant, the model outputs a probability distribution across 38 classes, representing various plant diseases or conditions. The Plant Diagnosis model was taken from kaggle: https://www.kaggle.com/code/sunritjana/plant-disease-detection-mobilenetv2/notebook, and is provided in the file: "plant_disease_detection.h5". 
 

# Gemini API Usage:
The Gemini API is utilized for processing user inputs, generating personalized plant recommendations, and providing care instructions. Relevant prompts are supplied on each page to receive suitable and personalized answers from users.


 
