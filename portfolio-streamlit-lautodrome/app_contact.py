import streamlit as st
#import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def app():
    st.title("Contact")
    st.markdown("""Vous souhaitez acquérir une peinture faite sur mesure ? \\
                Vous pouvez me contacter via cette adresse : lautodrome.hd@gmail.com :envelope:.""")
    st.markdown("""Merci de joindre à votre email une photographie du véhicule, de bonne qualité. Il est nécessaire qu'il y ait suffisamment de détails
                pour que je puisse les peindre.\\
                Cela me permettra de vous formuler une réponse en vous proposant un format papier adapté ainsi qu'un devis.""")
    #https://python.plainenglish.io/how-to-create-a-simple-webform-using-streamlit-de4a2981df0c
    # with st.form("form1", clear_on_submit=True):
    #     name = st.text_input("Enter full name")
    #     email = st.text_input("Enter email")
    #     message = st.text_area("Message")
    #     submit = st.form_submit_button("Submit this form")
    #    st.help(st.form_submit_button)
