
import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key='')

st.title("Social Media Poster Creator")

# Custom CSS
st.markdown("""
    <style>
    .stTextInput > div > input {
        border: 2px solid #4CAF50;
        padding: 10px;
        border-radius: 5px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: black;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 20px;
        margin: 4px 2px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stMarkdown div {
        border: 2px solid black;
        color :black;
        padding: 10px;
        border-radius: 5px;
        background-color: #f9f9f9;
    }
    </style>
""", unsafe_allow_html=True)

# Text to Post function
def text_to_post(topic):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a Social Media Poster Creator."},
            {"role": "user", "content": f"Generate the social media content of 150 words. This is the topic: {topic}"},
        ],
        max_tokens=150
    )
    generated_text = response.choices[0].message.content
    return generated_text

# Text to Image function
def text_to_image(topic):
    response = client.images.generate(
        model="dall-e-3",
        prompt=f'You are a Social Media Poster Creator. This is your topic: {topic}',
        size="1024x1024",
        quality="standard",
        n=1
    )
    image_url = response.data[0].url
    return image_url

# Sidebar selection
option = st.sidebar.selectbox(
    'Choose an option:',
    ('Generate Text', 'Generate Image')
)

# User input for the topic
topic = st.text_input("Enter the topic for the social media post:")

# Display the appropriate section based on the sidebar selection
if option == 'Generate Text':
    if st.button("Generate Text"):
        if topic:
            generated_text = text_to_post(topic)
            st.markdown(f'<div>{generated_text}</div>', unsafe_allow_html=True)
        else:
            st.error("Please enter a topic.")
elif option == 'Generate Image':
    if st.button("Generate Image"):
        if topic:
            image_url = text_to_image(topic)
            st.image(image_url, caption='Generated Image', use_column_width=True)
        else:
            st.error("Please enter a topic.")
