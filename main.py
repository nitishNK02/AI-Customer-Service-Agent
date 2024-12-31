# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token 
import requests
import os
from dotenv import load_dotenv
import json
import streamlit as st



load_dotenv()


BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "bf056db9-a7c3-43cf-be56-45940345d739"
FLOW_ID = "d41abd58-cf4a-43c5-8856-dc7eec184c2a"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "customerdata" # You can set a specific endpoint name in the flow settings

 

def run_flow(message: str,) -> dict:
   
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()
   
def main():
    st.title("AI CUSTOMER CHAT")

    message = st.text_area("Message", placemaker = "Ask something...")

    if st.button("Run flow "):
        if not message.strip():
            st.error("Please enter a message ")
            return
        
        try:
            with st.spinner("Running flow.."):
                response = run_flow(message)
            
            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e)) 

if __name__ == "__main__":
    main()
    
