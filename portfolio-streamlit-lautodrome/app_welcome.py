#from turtle import width
import streamlit as st

def app():
    # columns = st.columns(2)
    # columns[0].image('images/welcome_page/logo.png',width=200, use_column_width=False)
    # columns[1].title("Portfolio de L'Autodrome")
    st.image('images/welcome_page/logo.png',width=200, use_column_width=False)
    st.title("Portfolio de L'Autodrome")
    st.markdown('Bienvenue sur le site du compte Instagram [L\'Autodrome](https://www.instagram.com/lautodrome.hd/).')
    st.image('images/paintings_from_photos/miura.png', caption='A Lamborghini Miura by L\'Autodrome', use_column_width=False)
