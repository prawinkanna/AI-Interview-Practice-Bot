AI Interview Practice Chatbot

An interactive web-based interview simulation application built using Python, Streamlit, and Pandas.
This project allows users to practice technical and HR interview questions with automated feedback based on structured evaluation logic.

📌 Project Overview

The AI Interview Practice Chatbot simulates a real interview environment.
Users can select a domain (Python, Machine Learning, SQL, HR) and answer questions one by one.

The system evaluates responses using rule-based Natural Language Processing techniques and provides structured feedback to improve clarity, confidence, and technical accuracy.

🎯 Objectives

Provide a self-practice interview platform

Improve technical explanation skills

Enhance communication confidence

Simulate structured interview flow

Demonstrate practical NLP-based evaluation

🛠 Technologies Used

Python

Streamlit (UI Framework)

Pandas (Data Handling)

CSV-based Question Bank

✨ Features

Category selection (Python, ML, SQL, HR)

Question-by-question interview flow

Keyword-based answer evaluation

Minimum word-count validation

Confidence phrase detection (e.g., "I think", "maybe")

Structured feedback system

Restart interview option

Clean and simple UI

🧠 Evaluation Logic

Each user response is evaluated based on:

1️⃣ Answer Length Check

Ensures the response is sufficiently detailed.

2️⃣ Keyword Matching

Checks whether important technical keywords are included in the answer.

3️⃣ Confidence Detection

Identifies uncertain phrases such as:

"I think"

"Maybe"

"Probably"

4️⃣ Structured Feedback

Provides improvement suggestions and strength indicators.


The question bank is stored in CSV format with the following columns:

category

question

difficulty

keywords

Example:

category,question,difficulty,keywords
ML,What is overfitting?,Beginner,high variance,training data,generalization

This structure allows filtering by category and supports evaluation logic.


🔮 Future Enhancements

TF-IDF and Cosine Similarity scoring

Final performance summary report

Difficulty-level filtering

Timer-based interview mode

Speech-to-text interview mode

Cloud deployment

User login and performance tracking

💼 Use Case

This project is useful for:

Students preparing for technical interviews

Freshers entering AI/ML or Data roles

Self-practice mock interview sessions

Demonstrating practical NLP application in portfolios

📌 Author

Developed as part of AI/ML learning and interview preparation practice.
