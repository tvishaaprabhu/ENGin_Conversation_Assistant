# importing streamlit
import streamlit as st

# setting up OpenAI API key
import openai

# Set your OpenAI API key here 
openai.api_key = st.secrets["OPENAI_API_KEY"] 

# GPT feedback function
def get_feedback(student_input):
    prompt = f"""
You are an English language tutor helping a student improve fluency through live conversation. The student just said: "{student_input}"
Do the following in your response:
1. Repeat what the student said and then show a corrected version (if needed).
2. Explain any grammar or syntax mistakes clearly and simply.
3. Suggest 1–2 better vocabulary words or idioms the student could use instead, and explain why and generally focus on improving their verbs or adjectives with less focus on nouns.
4. Ask a follow-up question based on what the student said to continue the conversation.
5. Adapt the tone and vocabulary complexity to match the student's fluency, based on their sentence. Use simple vocabulary if the sentence is basic; use more advanced vocabulary if the sentence shows higher fluency.
Respond in a friendly, encouraging tone.

    """

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Streamlit UI
st.set_page_config(page_title="ENGin AI English Assistant", layout="wide")
st.title("ENGin AI English Assistant")

st.markdown("Type your sentence in English below and get instant feedback:")

# User input
student_sentence = st.text_input("Your sentence:")

# Button to trigger GPT feedback
if st.button("Get Feedback"):
    if student_sentence.strip() == "":
        st.warning("Please enter a sentence.")
    else:
        with st.spinner("Analyzing your sentence..."):
            feedback = get_feedback(student_sentence)
            st.success("Here’s your AI tutor's response:")
            st.write(feedback)
