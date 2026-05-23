import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)

# Streamlit UI
st.set_page_config(page_title="Student AI Assistant")

st.title("🎓 Student AI Assistant")
st.write("Ask me study-related questions!")

# User input
user_question = st.text_input("Enter your question:")

# Button
if st.button("Ask AI"):

    if user_question:

        # System prompt
        system_prompt = """
        You are a helpful Student AI Assistant.
        Your job is to help students understand concepts,
        explain topics simply, solve study-related questions,
        and guide them in learning.
        
        Rules:
        - Explain in simple language.
        - Help with assignments conceptually.
        - Be friendly and educational.
        - If asked unrelated things, politely redirect to studies.
        """

        response = client.chat.completions.create(
           model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_question}
            ]
        )

        answer = response.choices[0].message.content

        st.subheader("AI Response")
        st.write(answer)

    else:
        st.warning("Please enter a question.")
