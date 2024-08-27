import streamlit as st
import requests

# Streamlit app
st.title("Dhaka Tribune Content Fetcher")

# The website URL
url = "https://www.dhakatribune.com/bangladesh"

# Fetch and display the website content
if st.button("Fetch Content"):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            st.write("**Website Content from Dhaka Tribune (Bangladesh section):**")
            st.text_area("Content", response.text, height=300)
        else:
            st.error(f"Failed to fetch content. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"Error occurred: {e}")

# Optionally, display the raw HTML
if st.checkbox("Show raw HTML"):
    response = requests.get(url)
    st.code(response.text)
