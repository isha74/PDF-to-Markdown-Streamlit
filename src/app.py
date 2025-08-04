import streamlit as st
import os
from converter import extract_text_from_pdf
from gemini_helper import convert_text_to_markdown

# Page settings
st.set_page_config(page_title="PDF to Markdown Converter", layout="centered")
st.title("📄 Convert PDF to Markdown using Gemini AI")

# Directories
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "Converted_md")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    # ✅ Save the uploaded file temporarily inside the current folder
    original_filename = uploaded_file.name  # e.g., sample3.pdf
    temp_pdf_path = os.path.join(os.path.dirname(__file__), original_filename)

    with open(temp_pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ PDF uploaded successfully!")

    if st.button("Convert to Markdown"):
        with st.spinner("⏳ Extracting and converting text..."):
            # ✅ Extract text from the absolute path (with from_full_path=True)
            extracted_text = extract_text_from_pdf(temp_pdf_path, from_full_path=True)
            markdown_text = convert_text_to_markdown(extracted_text)

            # Display result
            st.subheader("📝 Markdown Output")
            st.code(markdown_text, language="markdown")

            # Save .md file
            md_filename = uploaded_file.name.replace(".pdf", ".md")
            output_path = os.path.join(OUTPUT_DIR, md_filename)
            with open(output_path, "w", encoding="utf-8") as md_file:
                md_file.write(markdown_text)

            st.success(f"✅ Markdown saved to: Converted_md/{md_filename}")

            # Download button
            st.download_button(
                label="📥 Download Markdown File",
                data=markdown_text,
                file_name=md_filename,
                mime="text/markdown"
            )

        # Clean up
        os.remove(temp_pdf_path)
