import streamlit as st
import send_email
# from streamlit import button
# from watchdog.observers.fsevents2 import message

st.set_page_config(layout="wide")
st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Provide your email")
    raw_message = st.text_area("Write your message")
    message = f"""\
Subject: New email from user {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email.send_email(message)
        st.info("Your message was sent successfully!")

