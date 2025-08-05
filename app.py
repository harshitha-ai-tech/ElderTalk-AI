import streamlit as st
import language_tool_python

st.title("ElderTalk AI - Message Simplifier")

tool = language_tool_python.LanguageTool('en-US')

user_input = st.text_area("📥 Enter message to simplify:")

if st.button("Simplify"):
    matches = tool.check(user_input)
    corrected = language_tool_python.utils.correct(user_input, matches)
    
    st.markdown("### ✨ Simplified Output:")
    st.success(corrected)
