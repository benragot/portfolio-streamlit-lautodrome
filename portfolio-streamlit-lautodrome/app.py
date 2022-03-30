import streamlit as st
import app_welcome
import app_contact
PAGES = {
    "Welcome": app_welcome,
    "Contact": app_contact,
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
