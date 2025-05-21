import streamlit as st

def main():
    st.title("Insight AI - Frontend")
    st.header("Welcome to the Insight AI Utility")
    st.write("This is a simple frontend built using Streamlit.")

    # Example input form
    st.subheader("Input Form")
    user_input = st.text_input("Enter some text:")
    if st.button("Submit"):
        st.write(f"You entered: {user_input}")

    # Example file uploader
    st.subheader("File Uploader")
    uploaded_file = st.file_uploader("Upload a file")
    if uploaded_file is not None:
        st.write(f"Uploaded file: {uploaded_file.name}")

    # Example slider
    st.subheader("Adjust Parameters")
    slider_value = st.slider("Select a value", 0, 100, 50)
    st.write(f"Slider value: {slider_value}")

if __name__ == "__main__":
    main()