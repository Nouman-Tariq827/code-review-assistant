import streamlit as st

st.title("🤖Code Review Assistant 🤖")
st.write("Paste your code below to receive automated review suggestions.")

code_input = st.text_area("Enter code snippet here:", height=200)

def review_code(code):
    improvements = []

    if "for i in range(len(" in code:
        improvements.append("Avoid using 'range(len())'. Use direct iteration like `for item in list:`.")

    if "==" in code and "None" in code:
        improvements.append("Use `is None` instead of `== None` for better Python practice.")

    if "print(" in code:
        improvements.append("Consider using logging instead of print statements in production code.")

    if len(code) > 200:
        improvements.append("Break large blocks of code into smaller reusable functions.")

    if ":" not in code:
        improvements.append("Ensure proper syntax formatting.")

    positive = "The code structure is clear and easy to read."

    return improvements[:3], positive


if st.button("Review Code"):

    if code_input.strip() == "":
        st.warning("Please enter a code snippet!")
    else:
        improvements, positive = review_code(code_input)

        st.subheader("AI Review")

        if improvements:
            for i, imp in enumerate(improvements, 1):
                st.write(f"{i}. {imp}")
        else:
            st.write("1. No major improvements detected.")

        st.write(f"✅ Positive: {positive}")
