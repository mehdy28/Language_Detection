import streamlit as st
import requests
from pydantic import BaseModel

# Define the base URL of your FastAPI app
BASE_URL = "http://localhost:8000"

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    language: str

def main():
    st.title("Language Detection FastAPI + Streamlit")

    st.sidebar.header("Endpoints")
    selected_endpoint = st.sidebar.selectbox(
        "Select an endpoint",
        ["home", "predict"]
    )

    if selected_endpoint == "home":
        st.header("Home Endpoint")
        health_check = requests.get(BASE_URL + "/").json()
        st.json(health_check)
    elif selected_endpoint == "predict":
        st.header("Predict Endpoint")
        input_text = st.text_area("Enter text for language prediction:")
        if st.button("Predict"):
            payload = {"text": input_text}
            response = requests.post(BASE_URL + "/predict", json=payload).json()
            st.json(response)

if __name__ == "__main__":
    main()
