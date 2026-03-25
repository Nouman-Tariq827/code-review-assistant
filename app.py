import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

st.title("Code Review Assistant 🤖")
st.write("Paste a code snippet below to get 3 improvements + 1 positive note.")

code_input = st.text_area("Enter code snippet here:", height=200)

if st.button("Review Code"):
    if code_input.strip() == "":
        st.warning("Please enter a code snippet!")
    else:
        with st.spinner("Reviewing code..."):
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
                        Review this code and provide:
                        - 3 improvements
                        - 1 positive comment

                        Code:
                        {code_input}
                        """
                    }
                ]
            )

        st.subheader("AI Review")
        st.write(response.choices[0].message.content)
