import streamlit as st
from bs4 import BeautifulSoup
import requests

st.set_page_config(page_title="Meta Tag Extractor", page_icon="🌐")

st.title("Website Meta Tag Extractor")
st.write("Enter a URL to extract meta tags like title, description, keywords, and Open Graph data.")

url = st.text_input("Enter Website URL:", placeholder="e.g., https://example.com")

if st.button("Extract Meta Tags") and url:
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract meta tags
        title = soup.title.string if soup.title else "No title found"
        description = soup.find("meta", attrs={"name": "description"})
        keywords = soup.find("meta", attrs={"name": "keywords"})
        og_title = soup.find("meta", attrs={"property": "og:title"})
        og_description = soup.find("meta", attrs={"property": "og:description"})
        og_image = soup.find("meta", attrs={"property": "og:image"})

        # Display results
        st.subheader("Extracted Meta Tags")

        st.write(f"**Title:** {title}")
        st.write(f"**Description:** {description['content'] if description else 'No description found'}")
        st.write(f"**Keywords:** {keywords['content'] if keywords else 'No keywords found'}")
        
        st.write("### Open Graph Data")
        st.write(f"**OG Title:** {og_title['content'] if og_title else 'No OG title found'}")
        st.write(f"**OG Description:** {og_description['content'] if og_description else 'No OG description found'}")
        st.write(f"**OG Image:** {og_image['content'] if og_image else 'No OG image found'}")
    except Exception as e:
        st.error(f"Error: {e}")
