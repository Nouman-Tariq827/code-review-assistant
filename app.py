import streamlit as st

# Page config
st.set_page_config(
    page_title="AI Code Review Assistant",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>

.main-title {
    font-size:40px;
    font-weight:700;
    text-align:center;
    background: linear-gradient(90deg,#6a11cb,#2575fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align:center;
    font-size:18px;
    color:gray;
}

.card {
    background-color:#f9f9f9;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.review-card {
    background-color:#ffffff;
    padding:15px;
    border-radius:10px;
    border-left:5px solid #2575fc;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-title">🤖 AI Code Review Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Paste your code and receive automated improvement suggestions</p>', unsafe_allow_html=True)

st.write("")

# Sidebar
with st.sidebar:
    st.title("⚙️ App Info")
    st.write("This tool analyzes your code and provides quick improvement suggestions.")
    st.write("### Supported checks")
    st.write("✔ Python best practices")
    st.write("✔ Code readability")
    st.write("✔ Syntax hints")
    st.write("✔ Refactoring suggestions")

# Code input card
st.markdown('<div class="card">', unsafe_allow_html=True)

code_input = st.text_area(
    "💻 Paste your code here",
    height=300,
    placeholder="Example:\nfor i in range(len(list)):\n    print(list[i])"
)

st.markdown('</div>', unsafe_allow_html=True)

# Review logic
def review_code(code):
    improvements = []

    if "for i in range(len(" in code:
        improvements.append("Avoid using `range(len())`. Use direct iteration like `for item in list:`.")

    if "== None" in code:
        improvements.append("Use `is None` instead of `== None` for Python best practice.")

    if "print(" in code:
        improvements.append("Consider using `logging` instead of print statements in production.")

    if len(code) > 200:
        improvements.append("Break large code blocks into smaller reusable functions.")

    if ":" not in code:
        improvements.append("Ensure proper Python syntax formatting.")

    positive = "The code structure is clean and readable."

    return improvements[:3], positive


# Button centered
col1, col2, col3 = st.columns([1,2,1])

with col2:
    review_btn = st.button("🚀 Run AI Code Review", use_container_width=True)


if review_btn:

    if code_input.strip() == "":
        st.warning("⚠ Please enter a code snippet.")
    else:

        improvements, positive = review_code(code_input)

        st.markdown("## 📊 Review Results")

        # Code preview
        with st.expander("👀 View submitted code"):
            st.code(code_input, language="python")

        st.write("")

        # Improvements
        if improvements:
            st.subheader("🔧 Suggested Improvements")

            for imp in improvements:
                st.markdown(f"""
                <div class="review-card">
                ⚡ {imp}
                </div>
                """, unsafe_allow_html=True)

        else:
            st.success("🎉 No major issues detected!")

        st.write("")

        # Positive feedback
        st.subheader("✅ Positive Feedback")
        st.success(positive)

# Footer
st.write("")
st.markdown("---")
st.markdown("<center>Built with ❤️ using Streamlit</center>", unsafe_allow_html=True)
