import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key

genai.configure(api_key=google_gemini_api_key)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

#setting up our model
model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  generation_config=generation_config,
  safety_settings = safety_settings
)


#wide mode
st.set_page_config(layout="wide")

#title of our application
st.title('🖊️🦾 PenPal AI: Your Smart Writing Companion')

#create a subheader
st.subheader("Simplify your blogging journey with our Intelligent, AI-based Assistance")

#sidebar for user input
with st.sidebar:
    st.title("Input Your Blog Details")
    st.subheader("Enter Details About The Blog You Want To Generate")

    #title for blog
    blog_title = st.text_input("Blog Title")

    #keywords input
    keywords = st.text_area("Keywords (Please Provide Comma-Separated Keywords)")

    #word limit for blog
    num_words = st.slider("Word Limit", min_value = 200, max_value = 2000, step=50)

    #number of images
    #num_images = st.number_input("Number of Images", min_value = 0, max_value = 10, step=1)

    prompt_parts = [
        f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and \"{keywords}\". The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."
    ]
    response = model.generate_content(prompt_parts)

    #submit button
    submit_button = st.button("Generate")

if submit_button:
    st.write(response.text)