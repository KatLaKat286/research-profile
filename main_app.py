import streamlit as st

# Page configuration
st.set_page_config(page_title="Katlego Masiteng | Researcher Profile", page_icon="🔬", layout="wide")

# Sidebar
try:
    st.sidebar.image("profile_image.png.png", width=150)
except:
    st.sidebar.warning("Image not found. Check filename!")

st.sidebar.title("Contact Details")
st.sidebar.write("👤 **Katlego Masiteng**")
st.sidebar.write("📧 [kmastung@gmail.com](mailto:kmastung@gmail.com)")
st.sidebar.write("📞 061 925 2432")
st.sidebar.write("📍 University of Johannesburg")

# CV Download
st.sidebar.markdown("---")
# --- DOWNLOAD CV BUTTON ---
st.sidebar.markdown("---")
try:
    # 1. Update this line to match your actual filename on GitHub
    with open("Katlego Masiteng_Resume 2026.pdf", "rb") as file:
        st.sidebar.download_button(
            label="📄 Download CV",
            data=file,
            # 2. This is what the file will be named when someone downloads it
            file_name="Katlego_Masiteng_Resume.pdf", 
            mime="application/pdf"
        )
except FileNotFoundError:
    st.sidebar.warning("Ensure 'Katlego Masiteng_Resume 2026.pdf' is uploaded to GitHub.")

# --- MAIN CONTENT ---
st.title("Researcher Profile: Katlego Masiteng")
st.subheader("AI Researcher at the University of Johannesburg")

# 1. Impact Metrics (The "Wow" Factor)
st.write("---")
col1, col2, col3 = st.columns(3)
col1.metric("Publications", "5+", "2 New")
col2.metric("Research Projects", "10+", "Active")
col3.metric("AI Models", "15+", "74% Avg Acc")

# 2. Tabs for Organization
st.write("---")
tab1, tab2, tab3 = st.tabs(["📖 About Me", "🔬 Research", "🛠️ Skills"])

with tab1:
    st.header("About Me")
    st.write("I am an Artificial Intelligence researcher at the **University of Johannesburg**, exploring 4IR solutions...")

with tab2:
    st.header("Publications & Projects")
    with st.expander("📄 AI in SA Higher Education"):
        st.write("Lead Researcher | UJ Content")
    with st.expander("📄 Data-Driven 4IR"):
        st.write("Presented at AI & Society Conference")

with tab3:
    st.header("Technical Expertise")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### Languages")
        st.write("- Python, R, SQL")
    with col_b:
        st.write("### Frameworks")
        st.write("- TensorFlow, PyTorch")

st.markdown("---")
st.caption("© 2026 Katlego Masiteng • Built with Streamlit")


