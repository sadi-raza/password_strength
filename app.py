import streamlit as st
import re

st.set_page_config(
    page_title="password_strength_mmeter",
    page_icon="🔑", 
    layout="centered",
    initial_sidebar_state="expanded",
)
st.title("Password Strength Meter")
st.write("This app checks the strength of your password and provides feedback.")
st.write("Enter your password below:")



def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        feedback.append("✅ Strong Password!")
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("👨‍💻 Weak Password - Improve it 🔒 using the suggestions above.")
    return feedback    

password = st.text_input("Password", type="password")
if st.button("Check Password Strength"):
    if password:
       check_password_strength(password)
    else:
        st.warning("Please enter a password to check its strength.")

if password:
    feedback = check_password_strength(password)
    st.write("### Feedback:")
    for line in feedback:
        st.write(line)  




     