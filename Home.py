
import streamlit as st

st.set_page_config(page_title="Tanushree Vaitage — Travel AI", page_icon="🌍", layout="wide")

st.title("Tanushree Vaitage")
st.subheader("AI-Powered Travel Insights & Recommendation Assistant")

st.write("Personalized itineraries, climate insights, and budget-savvy travel tips — powered by datasets and OpenAI.")

try:
    st.page_link("pages/1_Chatbot.py", label="👉 Explore the Chatbot")
except Exception:
    st.write("Go to Chatbot page manually.")

st.markdown("---")
st.markdown("""
- 📊 [Tableau Dashboards](https://public.tableau.com/app/profile/tanushree.vaitage/vizzes)  
- 🧭 [Notion Project](https://www.notion.so/AI-Powered-Travel-Insights-Recommendation-Dashboard-24cc2f95eafa80cdb4fafcb7cf22025d?source=copy_link)
""")
