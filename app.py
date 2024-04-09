import streamlit as st

def hello_world():
    return "Hello, World! This is a test for Docker and Streamlit."

def main():
    st.write(hello_world())

if __name__ == "__main__":
    main()