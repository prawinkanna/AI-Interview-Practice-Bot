import streamlit as st
import pandas as pd

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="AI Interview Practice Bot", layout="centered")

st.title("🎯 AI Interview Practice Chatbot")

# -------------------------------
# LOAD QUESTION BANK
# -------------------------------
try:
    questions_df = pd.read_csv("question_bank.csv")
except:
    st.error("question_bank.csv file not found. Please place it in the same folder as app.py.")
    st.stop()

# -------------------------------
# SESSION STATE INITIALIZATION
# -------------------------------
if "category" not in st.session_state:
    st.session_state.category = None

if "current_index" not in st.session_state:
    st.session_state.current_index = 0

if "filtered_questions" not in st.session_state:
    st.session_state.filtered_questions = None


# -------------------------------
# CATEGORY BUTTONS (4 ONLY)
# -------------------------------
if st.session_state.category is None:

    st.subheader("Select Interview Category")

    # Custom button styling
    st.markdown("""
        <style>
        div.stButton > button {
            width: 200px;
            height: 60px;
            font-size: 18px;
            border-radius: 12px;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    if col1.button("🐍 Python"):
        st.session_state.category = "Python"

    if col2.button("🤖 ML"):
        st.session_state.category = "ML"

    if col3.button("🗄 SQL"):
        st.session_state.category = "SQL"

    if col4.button("💼 HR"):
        st.session_state.category = "HR"

    if st.session_state.category is not None:
        st.session_state.filtered_questions = questions_df[
            questions_df["category"] == st.session_state.category
        ].reset_index(drop=True)

        st.session_state.current_index = 0
        st.rerun()

# -------------------------------
# INTERVIEW FLOW
# -------------------------------
else:

    questions = st.session_state.filtered_questions

    if st.session_state.current_index < len(questions):

        row = questions.iloc[st.session_state.current_index]
        question = row["question"]
        keywords = [k.strip().lower() for k in row["keywords"].split(",")]

        st.markdown("### 🗣 Interviewer:")
        st.write(question)

        user_answer = st.text_area("✍️ Your Answer")

        if st.button("Submit Answer"):

            feedback = []
            score = 0

            # 1️⃣ Length Check
            word_count = len(user_answer.split())

            if word_count >= 30:
                score += 1
            else:
                feedback.append("⚠️ Your answer is too short. Try explaining in more detail.")

            # 2️⃣ Keyword Matching
            matched = 0
            for word in keywords:
                if word in user_answer.lower():
                    matched += 1

            if matched >= len(keywords) / 2:
                score += 1
                feedback.append("✅ Good coverage of important concepts.")
            else:
                feedback.append("💡 Try including more important technical keywords.")

            # 3️⃣ Confidence Check
            uncertain_phrases = ["i think", "maybe", "probably"]

            if not any(phrase in user_answer.lower() for phrase in uncertain_phrases):
                score += 1
            else:
                feedback.append("⚠️ Avoid uncertain phrases. Be confident in your explanation.")

            # Display Feedback
            st.markdown("### 📢 Feedback")

            for item in feedback:
                st.write(item)

            if score == 3:
                st.success("🔥 Strong Answer")
            elif score == 2:
                st.info("🙂 Decent Answer – Can Improve")
            else:
                st.warning("⚠️ Needs Improvement")

            st.session_state.current_index += 1

            if st.button("Next Question"):
                st.rerun()

    else:
        st.success("🎉 Interview Completed!")

        if st.button("Restart Interview"):
            st.session_state.clear()
            st.rerun()