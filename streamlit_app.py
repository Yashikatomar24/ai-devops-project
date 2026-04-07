import streamlit as st

st.title("AI DevOps Project")
st.write("Welcome! Your Streamlit app is running 🚀")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name}!")
