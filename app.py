import streamlit as st

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝"
)

st.title("📝 AI Text Summarizer")
st.write("Paste your text below and get a short summary.")

text = st.text_area(
    "Enter your text:",
    height=300,
    placeholder="Paste your meeting notes, article, or any long text here..."
)

if st.button("✨ Summarize"):
    if text.strip():
        sentences = text.replace("\n", " ").split(".")
        sentences = [s.strip() for s in sentences if s.strip()]

        if len(sentences) <= 3:
            summary = ". ".join(sentences)
        else:
            summary = ". ".join(sentences[:3]) + "."

        st.subheader("📌 Summary")
        st.write(summary)
    else:
        st.warning("Please enter some text first.")