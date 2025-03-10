import streamlit as st
import re
st.set_page_config(page_title="Pasword Strength Meter ", page_icon="🗝", )
st.title("🔑Password Strength Meter 🔓")
st.markdown("### Enter your password below to check its strength")
st.sidebar.title("About")
name = st.sidebar.text_input("Enter your name:")
if name in name:
    st.sidebar.info(f"👋Hello {name}")
else:
    st.sidebar.markdown("")
    
    
    
st.sidebar.markdown("Welcome to the Password Strength Meter! 💪")
st.sidebar.markdown("📍 This is a simple password strength meter that uses to check the strength of your password. 🏋🏽‍♂️")
pasword = st.text_input("Enter your password: " , type="password")
feedback = []
score = 0
if pasword:
    if len(pasword) == 0:
        st.stop()
    elif len(pasword) >= 8:
        score += 1
    else:
        feedback.append("Password is too short")
    if re.search(r"[a-z]", pasword) and re.search(r"[A-Z]", pasword):
        score += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters")
    if re.search(r"\d", pasword):
        score += 1
    else:
        feedback.append("Password should contain at least one digit")
    if re.search("[!@#-_$%^&~]", pasword):
        score += 1
    else:
        feedback.append("Password should contain special characters(_-!@#$%^&~)")
    if score == 4:
        feedback.append("✅ Your Password has a strong strength 💯🎉")
    elif score == 3:
        feedback.append("😐 Your Password has a medium strength. Make it stronger 💪")
    else : 
        feedback.append("❗ Your Password has a weak strength. Make it stronger by adding more characters 🚨")
    if feedback:
        st.markdown("### Improvements Suggestions ")

        for tip in feedback:
           st.write(tip)
else:
    st.info("Please enter your password to check its strength")