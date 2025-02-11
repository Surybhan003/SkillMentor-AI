import streamlit as st
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Sign Up Page")
col1,col2=st.columns([1,2])
with col1:
    new_username = st.text_input("Choose a Username")
    new_password = st.text_input("Choose a Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Sign Up"):
    if new_password == confirm_password:
        st.success("Sign up successful! You can now log in.")
    else:
        st.error("Passwords do not match. Please try again.")
