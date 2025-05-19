import streamlit as st
import firebase_admin

from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('potering-455bc-22bf681d0bcb.json')
firebase_admin.initialize_app(cred)



def app():

    st.title('Welcome to :violet[Pondering]')

    choice = st.selectbox('Login/Signup', ['Login','Sign up'])
    if choice=='Login':
        email = st.text_input('Email Address')
        password = st.text_input('Password', type ='password')

        st.button('Login')

    else:

        email = st.text_input('Email Address')
        password = st.text_input('Password', type ='password')

        username = st.text_input('Enter your unique username')

        if st.button('Create my account'):
            user = auth.create_user(email = email, password = password, uid = username)

            st.success('Account created successfully!')
            st.markdown('Please Login using your email and password')
            st.balloons()

