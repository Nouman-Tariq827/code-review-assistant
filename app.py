import streamlit as st

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="AI Code Review Assistant",
    page_icon="🤖",
    layout="wide"
)

# -------------------------
# Custom CSS
# -------------------------
CUSTOM_CSS = """
<style>
.main-title{
    font-size:40px;
    font-weight:700;
    text-align:center;
    background: linear-gradient(90deg,#6a11cb,#2575fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:gray;
}

.card{
    background:#f9f9f9;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.review-card{
    background:#ffffff;
    padding:15px;
    border-radius:10px;
    border-left:5px solid #2575fc;
    margin-bottom:10px;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# -------------------------
# Header
# -------------------------
st.markdown('<p class="main-title">🤖 AI Code Review Assistant</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Paste your code and receive automated improvement suggestions</p>', unsafe_allow_html=True)

# -------------------------
# Sidebar
# -------------------------
with st.sidebar:
    st.title("⚙️ App Info")
    st.markdown("""
This tool analyzes your code and provides quick improvement suggestions.

### Supported checks
✔ Python best practices  
✔ Code readability  
✔ Syntax hints  
✔ Refactoring suggestions
""")

# -------------------------
# Code Input
# -------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

code_input = st.text_area(
    "💻 Paste your code here",
    height=300,
    placeholder="Example:\nfor i in range(len(list)):\n    print(list[i])"
)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------
# Review Logic
# -------------------------
def review_code(code: str):
    checks = {
        "for i in range(len(": "Avoid using `range(len())`. Use `for item in list:`.",
        "== None": "Use `is None` instead of `== None`.",
        "print(": "Use `logging` instead of print in production."
    }

    improvements = [msg for key, msg in checks.items() if key in code]

    if len(code) > 200:
        improvements.append("Break large code blocks into smaller reusable functions.")

    if ":" not in code:
        improvements.append("Ensure proper Python syntax formatting.")

    positive = "The code structure looks clean and readable."

    return improvements[:3], positive


# -------------------------
# Review Button
# -------------------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    review_btn = st.button("🚀 Run AI Code Review", use_container_width=True)

# -------------------------
# Review Results
# -------------------------
if review_btn:

    if not code_input.strip():
        st.warning("⚠ Please enter a code snippet.")
    else:
        improvements, positive = review_code(code_input)

        st.markdown("## 📊 Review Results")

        with st.expander("👀 View submitted code"):
            st.code(code_input, language="python")

        if improvements:
            st.subheader("🔧 Suggested Improvements")

            for imp in improvements:
                st.markdown(
                    f'<div class="review-card">⚡ {imp}</div>',
                    unsafe_allow_html=True
                )
        else:
            st.success("🎉 No major issues detected!")

        st.subheader("✅ Positive Feedback")
        st.success(positive)

# -------------------------
# Footer
# -------------------------
st.markdown("---")
st.markdown("<center>Built with ❤️ using Streamlit</center>", unsafe_allow_html=True)
