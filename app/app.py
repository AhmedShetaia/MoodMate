import streamlit as st
import requests
import os 
from dotenv import load_dotenv

load_dotenv() 

url = os.getenv("API_URL","http://0.0.0.0:8080")
# Define the FastAPI endpoint URL
FASTAPI_URL = f"{url}/chat" # read the url from env variables 
                                 #"http://moodmate_api:8000/chat" # moodmate_api is the name of the network used in yaml file 
                                 #"http://127.0.0.1:8000/chat"  use this url if you are testing the app with the api locally 

# Streamlit UI for the chatbot
st.title("MoodMate")

# User input field
user_input = st.text_input("Enter your message:")

# Check if user input is provided
if user_input:
    # Show the "generating response" message while waiting for the API response
    with st.spinner("Generating response..."):
        # Send POST request to FastAPI
        response = requests.post(FASTAPI_URL, json={"user_input": user_input})
        
        # Handle response
        if response.status_code == 200:
            chat_response = response.json().get("response")
            st.write(f"Chatbot: {chat_response}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
else:
    st.warning("Please enter a message and press Enter.")