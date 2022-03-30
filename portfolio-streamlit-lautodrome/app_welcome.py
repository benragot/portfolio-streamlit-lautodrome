from turtle import width
import streamlit as st

def app():

    columns = st.columns(2)
    columns[0].image('images/welcome_page/logo.png',width=200, use_column_width=False)
    columns[1].title("Portfolio de L'Autodrome")
    st.markdown('Un petit texte d\'intro ici !')
    st.image('images/paintings_from_photos/miura.png',width=750, caption='A Lamborghini Miura', use_column_width=False)
