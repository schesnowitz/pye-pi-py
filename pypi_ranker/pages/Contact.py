import streamlit as st

with st.form(key="contact_form", clear_on_submit=False):
    email = st.text_input(label="email")
    st.write('Your email:', email)
    selection = st.selectbox(
        'What topics would you like to discuss?',
        ['',
         'Python CLI apps',
         'Streamlit',
         'Django',
         "Flask",
         "Just wanna say hi!"])
    st.write('You selected:', selection)

    text = st.text_area(label="Your Message:")
    st.write('Your message:', text)
    st.form_submit_button(label="Send")
