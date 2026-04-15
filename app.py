import streamlit as st
from evaluator import evaluate_idea
from database import create_tables, connect_db

create_tables()

st.title("🧠 InvestorLens AI")

menu = st.sidebar.selectbox("Menu", ["Login", "Register", "Dashboard"])

mode = st.selectbox("Select Investor Mode", ["Friendly", "Strict", "Shark"])

idea = st.text_area("Enter your idea")

if st.button("Evaluate"):
    result = evaluate_idea(idea, mode)
    st.json(result)