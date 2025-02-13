import streamlit as st
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True
)
contacts = [
    {"name": "Surybhan Maurya", "position": "Owner", "phone": "+91 8957365197", "email": "surya@example.com", "photo": "p7.jpeg"},
    {"name": "Hans Muller", "position": "Managing Director", "phone": "+49 9123456780", "email": "hans@example.com", "photo": "p4.jpeg"},
    {"name": "Sami Rahman", "position": "Team Manager", "phone": "+971 8987654321", "email": "sami@example.com", "photo": "p5.jpeg"},
    {"name": "Lian Wang", "position": "Key Consultant", "phone": "+86 8587697326", "email": "lian@example.com", "photo": "p6.jpeg"}
]

st.title("Our Team")
for contact in contacts:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(contact["photo"], width=120, use_column_width=False)
    with col2:
        st.write(f"**Name:** {contact['name']}")
        st.write(f"**Position:** {contact['position']}")
        st.write(f"**Phone:** {contact['phone']}")
        st.write(f"**Email:** {contact['email']}")
        st.markdown("---")
