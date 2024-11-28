### README.md

```markdown
# Meta Tag Extractor

The Meta Tag Extractor is a simple Streamlit application that allows users to extract and view meta tags from any webpage by entering its URL. It is particularly useful for analyzing SEO metadata and social media sharing tags.

---

## Features

- **Input URL**: Enter any valid website URL for analysis.
- **Meta Tag Extraction**:
  - Extracts the page title (`<title>` tag).
  - Extracts meta tags such as:
    - Description (`<meta name="description">`)
    - Keywords (`<meta name="keywords">`)
  - Extracts Open Graph tags commonly used for social media sharing:
    - OG Title (`<meta property="og:title">`)
    - OG Description (`<meta property="og:description">`)
    - OG Image (`<meta property="og:image">`)
- **Error Handling**: Provides feedback for invalid URLs or pages without meta tags.

---

## Try the Application

Access the live application here: [Meta Tag Extractor](https://metatag-extractor.streamlit.app/)

---

## Requirements

To run the app locally, install the following Python libraries:

```bash
pip install -r requirements.txt
```

---

## How to Run Locally

1. Clone the repository or download the `app.py` file.
2. Navigate to the folder containing the `app.py` file.
3. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser using the URL provided by Streamlit (usually `http://localhost:8501`).

---

## How to Use

1. Open the application and enter the URL of the website you want to analyze (e.g., `https://example.com`).
2. Click the **"Extract Meta Tags"** button.
3. View the extracted meta tags under the respective sections:
   - **Title**
   - **Description**
   - **Keywords**
   - **Open Graph Tags** (Title, Description, Image)

---

## Example

**Input**: `https://example.com`

**Output**:
- **Title**: Example Domain
- **Description**: This domain is for use in illustrative examples in documents.
- **Keywords**: No keywords found.
- **Open Graph Data**:
  - OG Title: No OG title found.
  - OG Description: No OG description found.
  - OG Image: No OG image found.

---
