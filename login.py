import streamlit as st
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Login Page")
col1,col2=st.columns([1,2])
with col1:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "1234":
        st.success("Login successful!")
    else:
        st.error("Invalid credentials, please try again.")
