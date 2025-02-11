import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import time
import os
st.set_page_config(layout="wide")
# this code is for typing as chatgpt
def typing_effect_with_glitch(text_list, word_speed=0.3, paragraph_pause=1):
    placeholder = st.empty()
    css_placeholder = st.empty()
    full_text = []

    for i, paragraph in enumerate(text_list):
        current_paragraph = ""
        for word in paragraph.split():
            current_paragraph += word + " "
            combined_text = "".join(
                f"<p>{p}</p>" for p in full_text
            ) + f"<p>{current_paragraph}<span style='color: black;'>&#9679;</span></p>"
            placeholder.markdown(
                f"<div style='font-size:18px;'>{combined_text}</div>",
                unsafe_allow_html=True,
            )
            time.sleep(word_speed)

        full_text.append(f"<p class='glitch' data-text='{paragraph}'>{paragraph}</p>")

        combined_text = "".join(full_text)
        placeholder.markdown(
            f"<div style='font-size:18px;'>{combined_text}</div>",
            unsafe_allow_html=True,
        )
        time.sleep(paragraph_pause)
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True
)
col1,c,col2,col3,col4=st.columns([2,5.4,1.2,1.2,1.2])
st.markdown("""
    <style>
    div.stButton > button {
        width: 100px;  /* Ensures all buttons are equal width */
        height: 40px;
        margin-top: -5px; /* Align buttons to the same level */
    }
    div[data-testid="stVerticalBlock"] div:nth-child(1) button { 
        background-color: rgb(59, 127, 238) !important; 
        color: white !important;
        border-radius: 5px;
    }
    div[data-testid="stVerticalBlock"] div:nth-child(4) button { 
        background-color: rgb(243, 244, 241) !important; 
        color: black !important;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)
# here I have shown all the button of login, contact and signup
with col1:
    st.image(r'C:\Users\mourya\Desktop\streamlit_fldr\logo2.png')
with col2:
    login_button = st.button("Login", key="login")
    
with col3:
    contact_button = st.button("Contact", key="contact")
with col4:
    signup_button = st.button("Sign up", key="signup")
    
if login_button:
        st.switch_page("pages/login.py")
if signup_button:
        st.switch_page("pages/sign_up.py")
if contact_button:
    st.switch_page("pages/contact.py")
        
token=st.sidebar.radio("Navigation",["Home","about","Predictor"])
if token=="Home":
    c1,c2,c3,c4=st.columns([3,0.5,3,0.5])
    with c1:
      for i in range(3):
          st.write("")
      st.image(r'C:\Users\mourya\Desktop\streamlit_fldr\canva_img1.jpg')
      st.markdown("""
                  <h3 style="color: grey; opacity: 0.6;">Join with the world's largest platform</h3>
                  """, 
                  unsafe_allow_html=True
                  )
    with c3:
        for i in range(2):
          st.write("")
        st.header("Work of company")
        st.write("Welcome to Bright Player, where we are committed to solving real-world problems by leveraging advanced decision-making and predictive models. Our goal is to provide accurate, data-driven predictions and recommendations that empower individuals and organizations to make informed choices.")
    c1,c2,c3=st.columns([2.5,0.5,3])
    with c1:
        for i in range(2):
          st.write("")
        st.header("how it will help you")
        st.write("Bright Player recommends practical solutions aimed at improving the probability of positive outcomes. Our platform empowers users by providing them with data-backed recommendations that enhance their chances of success in various aspects of life.")
    with c3:
        for i in range(4):
          st.write("")
        st.image(r'C:\Users\mourya\Desktop\streamlit_fldr\canva_img2.jpg')
        st.markdown("""
                    <h3 style="color: grey; opacity: 0.6;">Join with the world's largest platform</h3>
                    """, 
                    unsafe_allow_html=True
                    )
    c1,c2,c3=st.columns([2,2.5,1])
    with c1:
      for i in range(4):
          st.write("")
      st.image(r'C:\Users\mourya\Desktop\streamlit_fldr\salary_img.jpeg')
      st.markdown("""
                  <h3 style="color: grey; opacity: 0.6;">Join with the world's largest platform</h3>
                  """, 
                  unsafe_allow_html=True
                  )
    with c2:
        for i in range(2):
          st.write("")
        st.header("Grow with us")
        st.write("At Bright Player, we believe that growth is a journey powered by data, insights, and smart decision-making. Whether you are a student, a professional, a business owner, or an investor, our advanced predictive models and optimized recommendations help you make informed choices that drive success.")
elif token=="about":
    for i in range(4):
          st.write("")
    st.markdown("""
                  <h3 style="color: grey; opacity: 0.6;">Here you can know about us</h3>
                  """, 
                  unsafe_allow_html=True
                  )
    opt=st.selectbox("",options=["about the company","about the Owner","about the team"])
    if opt=="about the company":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(
                r'C:\Users\mourya\Desktop\streamlit_fldr\p1.jpg',
                caption="Our company",
                use_column_width=True
            )
        with col2:
            st.write("BrightPlayer is a forward-thinking company dedicated to harnessing the power of Artificial Intelligence to tackle real-world problems. Our mission is to develop innovative, AI-driven solutions that address challenges across various industries, improving efficiency, decision-making, and overall quality of life. At BrightPlayer, we are committed to pushing the boundaries of technology to create smarter, sustainable solutions that make a tangible impact on the world.")
            # this code is for writing as a chatgpt
            # paragraphs = [
            # "BrightPlayer is a forward-thinking company dedicated to harnessing the power of Artificial Intelligence to tackle real-world problems. Our mission is to develop innovative, AI-driven solutions that address challenges across various industries, improving efficiency, decision-making, and overall quality of life. At BrightPlayer, we are committed to pushing the boundaries of technology to create smarter, sustainable solutions that make a tangible impact on the world.",
            # # "Our services focus on delivering advanced machine learning models, AI-powered insights, and data analytics that help companies optimize their processes, make informed decisions, and drive business growth. Whether it's enhancing customer experiences, streamlining operations, or solving complex challenges, SuryaTatva is committed to providing the tools and expertise needed to navigate the data-driven future.",
            # # "With a strong foundation in computational mathematics and a deep understanding of emerging technologies, SuryaTatva bridges the gap between innovative technology and practical applications. We aim to revolutionize industries like education, healthcare, finance, and more by transforming complex data into actionable insights.​"
            # ]
            # typing_effect_with_glitch(paragraphs, word_speed=0.1, paragraph_pause=0.5)
        # col1,col2=st.columns([1,1])
        # with col2:
        #     st.image(
        #         r'C:\Users\mourya\Desktop\streamlit_fldr\p2.jpg',
        #         caption="The head quater of BrightPlayer",
        #         use_column_width=True
        #     )
        # with col1:
        #     paragraphs = [
        #     "At BrightPlayer, our team is composed of passionate and skilled individuals driven by a shared vision of using AI to create transformative solutions. With expertise spanning across data science, machine learning, software development, and problem-solving, our diverse team collaborates to bring innovative ideas to life. Each member contributes their unique strengths, working together to overcome challenges and deliver cutting-edge, real-world AI solutions. We believe in fostering a culture of creativity, innovation, and continuous learning, ensuring that BrightPlayer remains at the forefront of technological advancement.",
        #     # "Our services focus on delivering advanced machine learning models, AI-powered insights, and data analytics that help companies optimize their processes, make informed decisions, and drive business growth. Whether it's enhancing customer experiences, streamlining operations, or solving complex challenges, SuryaTatva is committed to providing the tools and expertise needed to navigate the data-driven future.",
        #     # "With a strong foundation in computational mathematics and a deep understanding of emerging technologies, SuryaTatva bridges the gap between innovative technology and practical applications. We aim to revolutionize industries like education, healthcare, finance, and more by transforming complex data into actionable insights.​"
        #     ]
        #     typing_effect_with_glitch(paragraphs, word_speed=0.1, paragraph_pause=0.5)
    elif opt=="about the Owner":
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(
                r'C:\Users\mourya\Desktop\streamlit_fldr\p3.jpg',
                caption="Owner of the company",
                use_column_width=True
            )
        with col2:
            st.write("As the founder and owner of BrightPlayer, I am passionate about leveraging the power of Artificial Intelligence to solve real-world challenges. With a strong background in AI and machine learning, I specialize in developing innovative, data-driven solutions that drive impactful change. My goal is to lead a team of talented professionals who share my vision of using technology to create smarter, more efficient solutions for industries worldwide. At BrightPlayer, we are dedicated to transforming ideas into groundbreaking AI solutions, and I am excited to continue pushing the boundaries of what’s possible in the world of artificial intelligence.")
    elif opt=="about the team":
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(
                r'C:\Users\mourya\Desktop\streamlit_fldr\p2.jpg',
                caption="team of the company",
                use_column_width=True
            )
        with col2:
            st.write("At BrightPlayer, our team is composed of passionate and skilled individuals driven by a shared vision of using AI to create transformative solutions. With expertise spanning across data science, machine learning, software development, and problem-solving, our diverse team collaborates to bring innovative ideas to life. Each member contributes their unique strengths, working together to overcome challenges and deliver cutting-edge, real-world AI solutions. We believe in fostering a culture of creativity, innovation, and continuous learning, ensuring that BrightPlayer remains at the forefront of technological advancement.")
elif token=="Predictor":
    for i in range(4):
          st.write("")
    st.markdown("""
                  <h3 style="color: grey; opacity: 0.6;">What do you want to predict</h3>
                  """, 
                  unsafe_allow_html=True
                  )
    options=st.selectbox("",options=["College Prediction","Expences Prediction","Freelance Income Prediction","IQ Level Prediction","Investment Growth Prediction","Job Security Prediction","Mental Health Level Prediction","Rank Prediction","Salary Prediction"])


st.markdown("<hr style='border: 1px solid gray;'>", unsafe_allow_html=True)
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">', unsafe_allow_html=True)


# Load the external CSS file from the "pages" folder
def load_css(file_name):
    css_path = os.path.join("pages", file_name)  # Access the file inside "pages" folder
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load CSS
load_css("footer_file.css")

# Footer Section
footer_container = st.container()
with footer_container:
    col1,col2,col3 = st.columns((1,1,1))
    
    with col1:
        st.header("Platform")
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Platform overview</a>', unsafe_allow_html=True)
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Features</a>', unsafe_allow_html=True)
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Pricing</a>', unsafe_allow_html=True)
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Support</a>', unsafe_allow_html=True)
    with col2:
        st.header("Policies")
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Privacy Policy</a>', unsafe_allow_html=True)
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Terms and Conditions</a>', unsafe_allow_html=True)
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Disclaimer</a>', unsafe_allow_html=True)
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Help and FAQ</a>', unsafe_allow_html=True)
    with col3:
        st.header("Resources")
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Blog</a>', unsafe_allow_html=True)
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Documentation</a>', unsafe_allow_html=True)
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Webinars</a>', unsafe_allow_html=True)
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Case Studies</a>', unsafe_allow_html=True)

    col4,col5=st.columns([1,1])
    with col4:
        st.header("Company")
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">About Us</a>', unsafe_allow_html=True)
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Careers</a>', unsafe_allow_html=True)
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Press</a>', unsafe_allow_html=True)
        st.markdown('<a href="#" style="color: dimgray; text-decoration: none;">Privacy Policy</a>', unsafe_allow_html=True)

    with col5:
        st.header("Social Media")
        c1,c2,c3,c44=st.columns([1,1,1,4])
        with c1:
            st.markdown('<a href="https://www.youtube.com" target="_blank">'
                        '<img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" width="30" height="30" alt="YouTube"></a>', unsafe_allow_html=True)
        with c2:
            st.markdown('<a href="https://www.facebook.com" target="_blank">'
                        '<img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" width="30" height="30" alt="Facebook"></a>', unsafe_allow_html=True)
        with c3:
            st.markdown('<a href="https://www.instagram.com" target="_blank">'
                        '<img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Instagram_logo_2022.svg" width="30" height="30" alt="Instagram"></a>', unsafe_allow_html=True)
        st.markdown("""
                    <style>
                    .linkedin-icon a {
                    font-size: 30px;
                    text-decoration: none;
                    }
                    </style>
                    <div class="linkedin-icon">
                    <a href="https://linkedin.com" target="_blank">
                    <i class="fab fa-linkedin" style="color:#0077b5;"></i>
                    </a>
                    </div>
                    """,
                    unsafe_allow_html=True,
                    )

# Apply footer styling
st.markdown('<div class="footer-container">© 2025 Bright Player. All Rights Reserved.</div>', unsafe_allow_html=True)
