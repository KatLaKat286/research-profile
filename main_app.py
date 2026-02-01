import streamlit as st

# Page configuration
st.set_page_config(page_title="Katlego Masiteng | Researcher Profile", page_icon="🔬", layout="wide")

# Sidebar for contact info
# Ensure "profile_image.png" is in the same folder as this script!
st.sidebar.image("profile_image.png", width=150)
st.sidebar.title("Contact Details")
st.sidebar.write("👤 **Katlego Masiteng**")
st.sidebar.write("📧 [kmastung@gmail.com](mailto:kmastung@gmail.com)")
st.sidebar.write("📞 061 925 2432")
st.sidebar.write("📍 University of Johannesburg")

# --- DOWNLOAD CV BUTTON ---
st.sidebar.markdown("---")
try:
    with open("CV.pdf", "rb") as file:
        st.sidebar.download_button(
            label="📄 Download CV",
            data=file,
            file_name="Katlego_Masiteng_CV.pdf",
            mime="application/pdf"
        )
except FileNotFoundError:
    st.sidebar.warning("Upload 'CV.pdf' to the folder to enable download.")

st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com)")
st.sidebar.write("🎓 [Google Scholar](https://scholar.google.com)")

# Main Title
st.title("Researcher Profile: Katlego Masiteng")
st.subheader("AI Researcher at the University of Johannesburg")

# About Me Section
st.header("About Me")
st.write("""
I am an Artificial Intelligence researcher at the **University of Johannesburg**, dedicated to exploring 
innovative solutions within the landscape of the Fourth Industrial Revolution (4IR). My work focuses 
on leveraging machine learning and data-driven insights to address complex societal and technical challenges.
""")

# Research Interests
st.header("Research Interests")
interests = ["Machine Learning", "Natural Language Processing (NLP)", "AI in Education", "4IR Technologies"]
st.write(", ".join(interests))

# Publications Section
st.header("Publications & Research Projects")
col1, col2 = st.columns(2)
with col1:
    with st.expander("📄 AI Applications in South African Higher Education"):
        st.write("**Role:** Lead Researcher")
        st.write("[View Paper](https://ujcontent.uj.ac.za/)")
with col2:
    with st.expander("📄 Data-Driven Decision Making for 4IR"):
        st.write("**Conference:** International Conference on AI & Society")

# Skills
st.header("Technical Expertise")
sk_col1, sk_col2, sk_col3 = st.columns(3)
with sk_col1:
    st.write("### Languages")
    st.write("- Python\n- R\n- SQL")
with sk_col2:
    st.write("### AI Frameworks")
    st.write("- TensorFlow\n- PyTorch")
with sk_col3:
    st.write("### Tools")
    st.write("- Streamlit\n- GitHub\n- Docker")

st.markdown("---")
st.caption("© 2026 Katlego Masiteng • Built with Streamlit")