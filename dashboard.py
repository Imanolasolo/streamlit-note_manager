import streamlit as st
from db import get_user, create_note, get_notes, update_note, delete_note

def dashboard():
    st.title("Dashboard")
    st.write("Welcome to the Dashboard")

    user = get_user(st.session_state['username'])
    user_id = user[0]

    # Display Notes
    st.subheader("Your Notes")
    notes = get_notes(user_id)
    for note in notes:
        st.markdown(f"""
        <div style="background-color: yellow; padding: 10px; border-radius: 5px; margin-bottom: 10px; color: black;">
            <h3 style="color: black;">{note[1]}</h3>
            <p style="color: black;">{note[2]}</p>
        </div>
        """, unsafe_allow_html=True)

    # Selector for CRUD operations
    st.subheader("Manage Notes")
    action = st.selectbox("Choose an action", ["Create", "Edit", "Delete"])

    if action == "Create":
        st.subheader("Create a New Note")
        title = st.text_input("Title")
        content = st.text_area("Content")
        if st.button("Create Note"):
            create_note(user_id, title, content)
            st.success("Note created successfully")
            st.rerun()

    elif action == "Edit":
        st.subheader("Edit Note")
        edit_note_id = st.selectbox("Select Note to Edit", [note[0] for note in notes], format_func=lambda x: next(note[1] for note in notes if note[0] == x))
        edit_title = st.text_input("Edit Title", value=next((note[1] for note in notes if note[0] == edit_note_id), ""))
        edit_content = st.text_area("Edit Content", value=next((note[2] for note in notes if note[0] == edit_note_id), ""))
        if st.button("Update Note"):
            update_note(edit_note_id, edit_title, edit_content)
            st.success("Note updated successfully")
            st.rerun()

    elif action == "Delete":
        st.subheader("Delete Note")
        delete_note_id = st.selectbox("Select Note to Delete", [note[0] for note in notes], format_func=lambda x: next(note[1] for note in notes if note[0] == x))
        if st.button("Delete Note"):
            delete_note(delete_note_id)
            st.success("Note deleted successfully")
            st.rerun()

if __name__ == '__main__':
    dashboard()