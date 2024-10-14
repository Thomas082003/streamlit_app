import streamlit as st

st.set_page_config(page_title="Data Analytics", page_icon="📊")

st.markdown(
    """
    <style>
        body {
            background-color: #E8F0FE;
        }
        .stButton>button {
            background-color: #007ACC;
            color: #FFFFFF;
            border-radius: 10px;
            padding: 8px 20px;
        }
        .stTextInput>div>input {
            background-color: #F0F8FF;
            color: #333333;
        }
        .block-container {
            background-color: #FFFFFF;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
    """, 
    unsafe_allow_html=True
)

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "PC", "Professor", "Team"]

def login():
    st.header("🔑 Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.success(f"Logged in as {role}")
        st.rerun()

def logout():
    st.header("🚪 Log out")

    if st.button("Log out"):
        st.session_state.role = None
        st.success("Logged out successfully!")
        st.rerun()

role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon="🚪")
settings = st.Page("settings.py", title="Settings", icon="⚙️")

visualization = st.Page(
    "Visualization/visualization.py",
    title="📊 Data Dashboard",
    icon="📊",
    default=(role == "PC"),
)

ml = st.Page(
    "ml/ml_analysis.py",
    title="🤖 AI & Machine Learning",
    icon="🤖",
    default=(role == "Team"),
)

eda = st.Page(
    "EDA/eda.py",
    title="🔍 Data Exploration",
    icon="🔍",
    default=(role == "Professor"),
)

st.title("Welcome to Data Analytics Hub")
st.image("images/horizontal_blue.png", width=300, caption="Unlock the Power of Data")

page_dict = {}

if st.session_state.role in ["Professor", "Team"]:
    page_dict["🔍 Data Exploration"] = [eda]
if st.session_state.role in ["Professor", "Team", "PC"]:
    page_dict["📊 Data Dashboard"] = [visualization]
if st.session_state.role in ["Professor", "Team"]:
    page_dict["🤖 AI & Machine Learning"] = [ml]

if len(page_dict) > 0:
    pg = st.sidebar.radio("Select a Page:", ["Account", *page_dict.keys()])
else:
    login()

if st.session_state.role:
    if pg == "Account":
        logout()
    else:
        st.write(f"Welcome to the {pg} section!")
else:
    st.write("Please log in to explore custom analytics features.")
