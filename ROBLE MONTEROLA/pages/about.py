import streamlit as st

st.set_page_config(page_title="About Roble", page_icon="🎓", layout="wide")

st.markdown("""
<style>
.education-card {
    background: linear-gradient(135deg, #FF6B6B20, #4ECDC420) !important;
    border: 2px solid #FF6B6B !important;
    padding: 2rem !important;
    border-radius: 20px !important;
    margin: 1rem 0 !important;
}
.card-blue { background: linear-gradient(135deg, #4ECDC420, #45B7D120) !important; border-color: #4ECDC4 !important; }
h1, h2, h3 { color: #2C3E50 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("# 🌈 Roble Marin Monterola Jr.")
st.markdown("## BSCS Student | Age 21 | Nailaban, Mandaon, Masbate")

st.markdown("---")
st.markdown("## 👨‍💻 Student Profile")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **Personal Details:**
    - **Name:** Roble Marin Monterola Jr.
    - **Age:** 21
    - **Birthday:** April 12, 2005
    - **Address:** Nailaban, Mandaon, Masbate
    - **Email:** monterolaroble@gmail.com
    - **Phone:** 0970-308-5662
    """)
with col2:
    st.markdown("""
    **About Me:**
    Passionate BSCS student from Masbate!  
    Learning programming, algorithms, and web development.  
    Building my technical skills one project at a time! 🚀
    """)

# Education Timeline
st.markdown("---")
st.markdown("## 🎓 Education Journey")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="education-card">
        <h3>🏫 Elementary</h3>
        <h4>Nailaban Elementary School</h4>
        <p>• Strong academic foundation<br>
        - Math & Science excellence<br>
        - Prepared for high school</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="education-card card-blue">
        <h3>🎓 High School</h3>
        <h4>FAEMHS</h4>
        <p>• Graduated high school<br>
        - STEM track student<br>
        - Ready for BSCS!</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="education-card">
    <h3>🎓 College</h3>
    <h4>Bachelor of Science in Computer Science</h4>
    <p>• Currently enrolled<br>• Python, Algorithms, Web Dev<br>• Building portfolio</p>
</div>
""", unsafe_allow_html=True)

# Skills & Subjects
st.markdown("---")
st.markdown("## 📚 Current BSCS Subjects")

subjects = [
    "Programming Fundamentals",
    "Data Structures & Algorithms",
    "Computer Organization", 
    "Discrete Mathematics",
    "Web Technologies"
]

for subject in subjects:
    st.markdown(f"• **{subject}**")

st.markdown("---")
st.markdown("## 🎯 Semester Goals")

goals = [
    "Complete 5 Python projects",
    "Master data structures", 
    "Build web portfolio",
    "90+ grades target",
    "Join coding club"
]

st.markdown("**My goals this semester:**")
for goal in goals:
    st.markdown(f"• {goal}")

if st.button("🏠 Back to Home", use_container_width=True):
    st.switch_page("app.py")