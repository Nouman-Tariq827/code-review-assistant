import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Code Review Assistant",
    page_icon="🤖",
    layout="centered"
)

# Header
st.markdown(
    """
    <h1 style='text-align: center;'>🤖 Code Review Assistant</h1>
    <p style='text-align: center; font-size:18px;'>
    Paste your code below and get automated improvement suggestions
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# Code input
code_input = st.text_area(
    "💻 Enter your code snippet",
    height=250,
    placeholder="Paste your code here..."
)

# Review function
def review_code(code):
    improvements = []

    if "for i in range(len(" in code:
        improvements.append("🔁 Avoid using `range(len())`. Use direct iteration like `for item in list:`.")

    if "== None" in code:
        improvements.append("⚠️ Use `is None` instead of `== None` for better Python practice.")

    if "print(" in code:
        improvements.append("📋 Consider using `logging` instead of `print()` in production code.")

    if len(code) > 200:
        improvements.append("📦 Break large blocks of code into smaller reusable functions.")

    if ":" not in code:
        improvements.append("❗ Ensure proper syntax formatting.")

    positive = "✨ The code structure is clear and easy to read."

    return improvements[:3], positive


# Review button
if st.button("🔍 Review Code", use_container_width=True):

    if code_input.strip() == "":
        st.warning("⚠️ Please enter a code snippet first.")
    else:

        improvements, positive = review_code(code_input)

        st.divider()

        st.subheader("📊 AI Code Review")

        # Show code preview
        with st.expander("👀 View Submitted Code"):
            st.code(code_input, language="python")

        # Suggestions
        if improvements:
            st.markdown("### 🔧 Suggested Improvements")
            for imp in improvements:
                st.info(imp)
        else:
            st.success("🎉 No major improvements detected.")

        # Positive feedback
        st.markdown("### 👍 Positive Feedback")
        st.success(positive)

st.divider()

# Footer
st.caption("Built with ❤️ using Streamlit")
