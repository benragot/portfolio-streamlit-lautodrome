import streamlit as st
import app_welcome
import app_contact
import app_portfolio
import app_randomizer

PAGES = {
    "Welcome": app_welcome,
    "Portfolio": app_portfolio,
    "Randomize painting":app_randomizer,
    "Contact form": app_contact,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
