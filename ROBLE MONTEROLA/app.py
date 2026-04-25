import streamlit as st
import time

st.set_page_config(
    page_title="Roble Marin Monterola Jr. - BSCS",
    page_icon="🌈",
    layout="wide"
)

# Colorful CSS with perfect contrast
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}
.main-header {
    font-size: 4rem !important;
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    text-align: center !important;
    font-weight: 700 !important;
}
.subtitle { font-size: 1.5rem; color: #2C3E50; text-align: center; margin-bottom: 2rem; }
.metric-card {
    background: linear-gradient(135deg, #FF6B6B, #FF8E8E) !important;
    padding: 2rem !important;
    border-radius: 20px !important;
    color: white !important;
    text-align: center !important;
    box-shadow: 0 10px 30px rgba(255,107,107,0.3) !important;
}
.card-blue { background: linear-gradient(135deg, #4ECDC4, #A8E6CF) !important; box-shadow: 0 10px 30px rgba(78,205,196,0.3) !important; }
.card-green { background: linear-gradient(135deg, #45B7D1, #96D9F0) !important; box-shadow: 0 10px 30px rgba(69,183,209,0.3) !important; }
</style>
""", unsafe_allow_html=True)

# Header
col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.markdown('<h1 class="main-header">Roble Marin Monterola Jr.</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">🌈 BSCS Student | Age 21 | Nailaban, Mandaon, Masbate</p>', unsafe_allow_html=True)

# Navigation
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("👨‍💻 About", use_container_width=True, help="My education & skills"):
        st.switch_page("pages/about.py")
with col2:
    if st.button("📧 Contact", use_container_width=True, help="Get in touch!"):
        st.switch_page("pages/contact.py")
with col3:
    st.info("🎓 BSCS Subjects & Goals ↓")

# Stats Cards
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #2C3E50;'>📊 Student Profile</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="metric-card">
        <h1 style='font-size: 3rem;'>21</h1>
        <p>Age</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="metric-card card-blue">
        <h1 style='font-size: 3rem;'>Apr 12</h1>
        <p>Birthday</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="metric-card card-green">
        <h1 style='font-size: 3rem;'>Masbate</h1>
        <p>Location</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="metric-card">
        <h1 style='font-size: 3rem;'>BSCS</h1>
        <p>Degree</p>
    </div>
    """, unsafe_allow_html=True)

# Skills
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #2C3E50;'>🛠️ Current Skills</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #FFE5E5, #FFF2F2); padding: 2rem; border-radius: 20px; border-left: 5px solid #FF6B6B;'>
        <h3 style='color: #2C3E50;'>📚 Academic</h3>
        <ul style='color: #2C3E50;'>
            <li>Python (Learning)</li>
            <li>Algorithms</li>
            <li>Data Structures</li>
            <li>Problem Solving</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #E6F9F9, #F0FFFF); padding: 2rem; border-radius: 20px; border-left: 5px solid #4ECDC4;'>
        <h3 style='color: #2C3E50;'>💻 Technical</h3>
        <ul style='color: #2C3E50;'>
            <li>HTML/CSS Basics</li>
            <li>Streamlit Apps</li>
            <li>Git Version Control</li>
            <li>Web Development</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Interactive Tracker
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #2C3E50;'>📈 Study Tracker</h2>", unsafe_allow_html=True)

subject = st.selectbox("📖 Today's Subject:", ["Python", "Algorithms", "Web Dev", "Data Structures", "Math"])
hours = st.slider("🕐 Hours Studied:", 0, 8, 2)

col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Log Study Session", type="primary", use_container_width=True):
        st.success(f"🎉 Great job Roble! +{hours}h on {subject}!")
        st.balloons()

st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem; color: #2C3E50;'>
    <h3>🌈 Roble Marin Monterola Jr. | BSCS Student | Nailaban, Mandaon, Masbate</h3>
</div>
""", unsafe_allow_html=True)