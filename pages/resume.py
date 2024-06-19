import streamlit as st
import base64

file = "/home/harsh/Documents/github_projects/utility_projects/utility_repo/harsh_gupta_Resume.pdf"
def display_pdf(file):
    # Convert the PDF file to base64
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    # Embedding the PDF in HTML
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    
    # Displaying the PDF
    st.markdown(pdf_display, unsafe_allow_html=True)

display_pdf(file)