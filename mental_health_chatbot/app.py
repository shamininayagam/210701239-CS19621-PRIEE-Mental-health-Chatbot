import os
import streamlit as st
import google.generativeai as genai

# Initialize the Gemini-Pro model
os.environ['GOOGLE_GEMINI_KEY'] = "AIzaSyBoVQYDOeYH8L4-GZRL6b82nJAZJSESi-A"
genai.configure(api_key=os.getenv('GOOGLE_GEMINI_KEY'))
model = genai.GenerativeModel('gemini-pro')

# Define the function to send the user's message to the model and get the response
def get_model_response(user_input):
    prompt = "act only as a professional mental health therapist answer my query with your best possible response in short not more than one paragraph, can ask questions like a therapist..."
    response = model.generate_content(user_input)
    return response.text

# Define a function to convert the role of the message to a Streamlit chat message role
def role_to_streamlit(role):
    return "Therapist" if role == "Bot" else "User"

# Display the chat interface
def main():
    st.set_page_config(page_title="Therapisia",
                page_icon='👩‍⚕️',
                layout='centered',
                initial_sidebar_state='collapsed')
    st.title("    Therapisia- Mental Health Counselor ChatBot 👩‍⚕️")
        
    st.subheader("Express and feel free to talk with Me")
    st.subheader("I'm here to help you :sunglasses:")
    
    # Initialize chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Display user input box and send button
    user_input = st.text_input("You: ", key="user_input")
    if st.button("Send") and user_input:
        st.session_state.chat_history.append(("User", user_input))
        bot_response = get_model_response(user_input)
        st.session_state.chat_history.append(("Bot", bot_response))
    
    # Display chat history
    if st.session_state.chat_history:
        for role, message in st.session_state.chat_history:
            message_html = f"""
            <div class="{'user-message' if role == 'User' else 'bot-message'}">
                <div class="message">{message}</div>
            </div>
            """
            st.markdown(message_html, unsafe_allow_html=True)

    # Adjust layout
    st.markdown(""" 
        <style> 
        .stTextInput>div>div {
            width: 70%;
        }
        .user-message {
            display: flex;
            justify-content: flex-end;
            margin: 10px;
        }
        .bot-message {
            display: flex;
            justify-content: flex-start;
            margin: 10px;
        }
        .message {
            max-width: 60%;
            padding: 10px;
            border-radius: 10px;
            background-color: #dcf8c6;  /* User message background */
            color: #000;
            font-size: 16px;
        }
        .bot-message .message {
            background-color: #ececec;  /* Bot message background */
        }
        </style>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
