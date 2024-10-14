import streamlit as st

st.header("⚙️ Settings")
st.write(f"You are logged in as **{st.session_state.role}**.")
st.title("Personalize Your Experience")

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

def get_css(dark_mode):
    if dark_mode:
        return """
        <style>
            body {
                background-color: #121212;
                color: #FFFFFF;
            }
            .stButton>button {
                background-color: #1F1F1F;
                color: #FAFAFA;
                border-radius: 10px;
            }
            .stTextInput>div>input {
                background-color: #333333;
                color: #FFFFFF;
            }
            .block-container {
                background-color: #1F1F1F;
                box-shadow: 0 4px 8px rgba(255, 255, 255, 0.2);
            }
        </style>
        """
    else:
        return """
        <style>
            body {
                background-color: #F7F7F7;
                color: #000000;
            }
            .stButton>button {
                background-color: #007ACC;
                color: #FFFFFF;
                border-radius: 10px;
            }
            .stTextInput>div>input {
                background-color: #FFFFFF;
                color: #000000;
            }
            .block-container {
                background-color: #FFFFFF;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
        </style>
        """

st.sidebar.title("Theme Settings")
toggle = st.sidebar.checkbox("🌙 Enable Dark Mode", value=st.session_state.dark_mode)

st.session_state.dark_mode = toggle
st.markdown(get_css(st.session_state.dark_mode), unsafe_allow_html=True)

st.title("🌞 Toggle Themes")
st.write("Switch between light and dark themes using the checkbox in the sidebar.")

user_input = st.text_input("Enter some text:")
st.write(f"You entered: **{user_input}**")
st.button("Submit")
