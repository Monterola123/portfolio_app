import streamlit as st

st.set_page_config(page_title="Contact Roble", page_icon="📧", layout="wide")

st.markdown("""
<style>
.contact-card {
    background: linear-gradient(135deg, #4ECDC4, #A8E6CF) !important;
    border: 2px solid #4ECDC4 !important;
    color: #2C3E50 !important;
    padding: 2.5rem !important;
    border-radius: 20px !important;
    margin: 2rem 0 !important;
}
.card-red {
    background: linear-gradient(135deg, #FF6B6B, #FF8E8E) !important;
    border-color: #FF6B6B !important;
    color: white !important;
}
.success-msg {
    background: linear-gradient(135deg, #45B7D1, #96D9F0) !important;
    color: white !important;
    padding: 2rem !important;
    border-radius: 15px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("# 📧 Contact Roble Marin Monterola Jr.")
st.markdown("## BSCS Student | Nailaban, Mandaon, Masbate")

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    <div class="contact-card">
        <h2>📱 Get In Touch</h2>
        <h3>✉️ Email</h3>
        <p style="font-size: 1.3rem; font-weight: bold;">monterolaroble@gmail.com</p>
        <h3>📞 Phone</h3>
        <p style="font-size: 1.3rem; font-weight: bold;">0970-308-5662</p>
        <h3>📍 Address</h3>
        <p style="font-size: 1.2rem;">Nailaban, Mandaon, Masbate</p>
    </div>
    
    <div class="card-red">
        <h3>🤝 Looking For</h3>
        <ul style="font-size: 1.1rem;">
            <li>Study buddies</li>
            <li>Coding partners</li>
            <li>Group projects</li>
            <li>BSCS classmates</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.subheader("💬 Send Message")
    with st.form("contact_form"):
        name = st.text_input("👤 Name")
        email = st.text_input("📧 Email", value="monterolaroble@gmail.com")
        subject = st.selectbox("📂 Subject", ["Study Group", "Coding Project", "BSCS Help", "Just Hi"])
        message = st.text_area("💬 Message", height=120, 
                              placeholder="Hi Roble! Fellow BSCS student here...")
        
        col1, col2 = st.columns(2)
        with col1:
            submitted = st.form_submit_button("🚀 Send", use_container_width=True)
        
        if submitted:
            st.markdown("""
            <div class="success-msg">
                <h2>✅ Message Sent!</h2>
                <h3>Delivered to Roble</h3>
                <p>monterolaroble@gmail.com</p>
                <p>📱 Reply within 24hrs from Nailaban, Masbate!</p>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()

st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🏠 Home"):
        st.switch_page("app.py")
with col2:
    st.info("🌈 Colorful BSCS Portfolio!")
with col3:
    st.empty()

st.markdown("""
<div style='text-align: center; padding: 2rem;'>
    <h1 style='background: linear-gradient(45deg, #FF6B6B, #4ECDC4); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
    Roble Marin Monterola Jr.
    </h1>
    <h3>BSCS Student | Nailaban, Mandaon, Masbate</h3>
</div>
""", unsafe_allow_html=True)