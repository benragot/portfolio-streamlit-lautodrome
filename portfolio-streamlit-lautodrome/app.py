import streamlit as st
#import base64
#import app_welcome
import app_contact
import app_portfolio
import app_randomizer

PAGES = {
    #"Welcome": app_welcome,
    "Portfolio": app_portfolio,
    "Randomize painting":app_randomizer,
    "Contact": app_contact,
}
#st.set_page_config(layout="wide")
# def load_image(path):
#     with open(path, 'rb') as f:
#         data = f.read()
#     encoded = base64.b64encode(data).decode()
#     return encoded
# def background_image_style(path):
#     encoded = load_image(path)
#     style = f'''
#     <style>
#     .stApp {{
#         background-image: url("data:image/png;base64,{encoded}");
#         background-size: cover;
#     }}
#     </style>
#     '''
#     return style
# st.write(background_image_style('images/background.png'), unsafe_allow_html=True)

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
