import streamlit as st
from main import solve_math_problem

st.set_page_config(page_title="AI Math Solver", layout="centered")
st.title("📐 Gemini AI Math Solver")

question = st.text_area("Enter a math problem (algebra, calculus, or word problem):")

if st.button("Solve"):
    if question.strip() == "":
        st.warning("Please enter a math problem.")
    else:
        with st.spinner("Solving with Gemini..."):
            try:
                result = solve_math_problem(question)
                st.subheader("🧠 Step-by-Step Solution:")
                st.markdown(result)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")


