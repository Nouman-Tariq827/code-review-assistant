import streamlit as st

st.title("Code Review Assistant 🤖")
st.write("Paste a code snippet below to get 3 improvements + 1 positive note.")

# Input area for code snippet
code_input = st.text_area("Enter code snippet here:", height=200)

# Button to generate review
if st.button("Review Code"):
    if code_input.strip() == "":
        st.warning("Please enter a code snippet!")
    else:
        # Demo response (without AI for now)
        st.subheader("AI Review")
        st.text("1. Improvement 1\n2. Improvement 2\n3. Improvement 3\nPositive: Well structured!")
