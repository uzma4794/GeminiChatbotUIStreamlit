'''
import google.generativeai as genai
import streamlit as st
GOOGLE_API_KEY = "AIzaSyDSWC8W9W8r1JETbQ9Sz1yTm6e_-Nedy3s"
genai.configure(api_key=GOOGLE_API_KEY )

# model initiate

model = genai.GenerativeModel('gemini-1.5-flash')
def getResponseFromModel(user_input):
    response=model.generate_content(user_input)
    return response.text


st.set_page_config(page_title="Simple ChatBot", layout="centered")

st.title('simple chatbot')
st.write("It uses Google API ")

user_input = input ("Enter Your Prompt")
output = getResponseFromModel(user_input)
print(output)   
'''





# This program is chatbot using Gemini API Key

import streamlit as st
import google.generativeai as genai

# Configure the API key
GOOGLE_API_KEY = "AIzaSyDSWC8W9W8r1JETbQ9Sz1yTm6e_-Nedy3s"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Generative Model
# model = genai.GenerativeModel('gemini-pro')
model = genai.GenerativeModel('gemini-1.5-flash')
# Function to get response from the model
def get_chatbot_response(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit interface
st.set_page_config(page_title="Simple ChatBot", layout="centered")

st.title("✨ Simple ChatBot ✨")
st.write("Powered by Google Generative AI")

if "history" not in st.session_state:
    st.session_state["history"] = []

# Display chat history
for user_message, bot_message in st.session_state.history:
    st.markdown(f"""
    <div style="
        background-color: #d1d3e0; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {user_message} 😊</p>
    </div>
    """,unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="
        background-color: #d1d3e0; 
        border-radius: 15px; 
         padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Bot:</b> {bot_message} 🤖</p>
    </div>
    """, unsafe_allow_html=True)
    
# user_input = input("Enter your Prompt = ")
# output = get_chatbot_response(user_input)

# print(output)

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000)  # set character limit of input
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = get_chatbot_response(user_input)
            st.session_state.history.append((user_input, response))
        else:
            st.warning("Please Enter A Prompt")


