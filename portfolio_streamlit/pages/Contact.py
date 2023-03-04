import streamlit as st
from email_func import send_email

with st.form(key="contact_form", clear_on_submit=True):
    user_email = st.text_input(label="email")

    selection = st.selectbox(
        'What topics would you like to discuss?',
        ['Make a selection...',
         'Python CLI apps',
         'Streamlit',
         'Django',
         "Flask",
         "Just wanna say hi!"])

    raw_message = st.text_area(label="Your Message:")
    message = f"""\
Subject: Message from {user_email} 

From: {user_email}  

Topic = {selection} 

{raw_message}
"""

    button = st.form_submit_button(label="Send")
    if button == True and selection != 'Make a selection...' \
            and message != "" and user_email != "":
        send_email(message)
        st.info("Your message has been sent.")
    elif button == True:
        st.info("All fields need to be completed.")
        print(button)
