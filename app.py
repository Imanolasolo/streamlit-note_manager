import streamlit as st
from db import register_user, get_user
from passlib.hash import bcrypt
from dashboard import dashboard
import base64

def main():
    st.set_page_config(page_title="Note-Taking App", page_icon=":pencil2:")

    # Function to encode image as base64 to set as background
    def get_base64_of_bin_file(bin_file):
            with open(bin_file, 'rb') as f:
                data = f.read()
            return base64.b64encode(data).decode()

        # Encode the background image
    img_base64 = get_base64_of_bin_file('assets/background.jpg')

        # Set the background image using the encoded base64 string
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url('data:image/jpeg;base64,{img_base64}') no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
     
    col1, col2 = st.columns([4, 2])
    with col1:
        st.title("Ultimate Note-Taking App, :red[NOTETAKER]")
    with col2:
        with st.expander("Instructions"):
            st.write("1. Create an account or login, choose options from the sidebar")
            st.write("2. Create, edit, and delete notes")
            st.write("3. Manage all notes in the dashboard")

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        dashboard()
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.session_state.pop('username', None)
            st.rerun()
    else:
        menu = ["Login", "SignUp"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Login":
            st.subheader("Login Section")

            username = st.text_input("User Name")
            password = st.text_input("Password", type='password')
            if st.button("Login"):
                user = get_user(username)
                if user and bcrypt.verify(password, user[2]):
                    st.success(f"Logged In as {username}")
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = username
                    st.experimental_rerun()
                else:
                    st.warning("Incorrect Username/Password")

        elif choice == "SignUp":
            st.subheader("Create New Account")

            new_user = st.text_input("Username")
            new_password = st.text_input("Password", type='password')

            if st.button("Signup"):
                if register_user(new_user, new_password):
                    st.success("You have successfully created an account")
                    st.info("Go to Login Menu to login")
                else:
                    st.warning("Username already exists")

if __name__ == '__main__':
    main()