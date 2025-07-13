import streamlit as st
from modules.document_parser import extract_text_sections
from modules.summarizer import ai_summarize
from modules.retriever import retrieve_relevant_passages
from modules.qa import answer_question
from challenge import generate_questions, evaluate_answer
from modules.utils import highlight_text, truncate_text

# --- PAGE CONFIG & SIDEBAR ---
st.set_page_config(page_title="Ultimate AI Research Assistant", page_icon="🧠", layout="wide")

with st.sidebar:
    st.image("logo.png", width=120)  # Use your logo or comment out
    st.title("🧠 AI Research Assistant")
    st.markdown("""
    <small>
    <b>Features:</b><br>
    • Document upload & parsing<br>
    • Instant summary<br>
    • Ask Anything (grounded Q&A)<br>
    • Challenge Me (logic questions)<br>
    • Context memory & highlighting<br>
    </small>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.info("Upload a document and explore its contents with advanced AI tools!")

# --- MAIN APP TITLE ---
st.title("🧠 Ultimate AI Research Assistant")
st.caption("Upload, summarize, question, and challenge your understanding of any document!")

# --- SESSION STATE ---
if "history" not in st.session_state:
    st.session_state["history"] = []

# --- DOCUMENT UPLOAD ---
st.header("📄 Document Upload & Parsing")
uploaded_file = st.file_uploader("Upload a PDF, DOCX, TXT, or Image", type=["pdf", "docx", "txt", "png", "jpg", "jpeg"])

if uploaded_file:
    with st.spinner("Parsing document..."):
        sections = extract_text_sections(uploaded_file)
    st.success(f"✅ Document parsed into {len(sections)} sections/paragraphs.")

    # --- AUTO SUMMARY ---
    st.markdown("---")
    st.header("📝 Auto Summary")
    if st.button("Generate Summary"):
        with st.spinner("Summarizing document..."):
            full_text = " ".join([s[1] for s in sections])
            summary = ai_summarize(full_text, length=5)
            summary = truncate_text(summary, max_words=150)
        st.success("Summary generated!")
        st.markdown(f"**Summary:**\n\n{summary}")
        st.balloons()
        st.session_state["history"].append({"action": "summary", "content": summary})

    # --- ASK ANYTHING MODE ---
    st.markdown("---")
    st.header("💬 Ask Anything Mode")
    user_question = st.text_input("🔍 Enter your question about the document:")
    if user_question:
        with st.spinner("Retrieving relevant passages and generating answer..."):
            answer, supporting_sections = answer_question(user_question, sections)
        st.success("Answer generated!")
        st.markdown(f"**Answer:**\n\n{answer}")
        with st.expander("🔎 Show supporting text"):
            for title, snippet in supporting_sections:
                st.markdown(f"**{title or 'Section'}:**<br>" +
                            highlight_text(snippet, [user_question]), unsafe_allow_html=True)
        st.session_state["history"].append({"action": "qa", "question": user_question, "answer": answer})

    # --- CHALLENGE ME MODE ---
    st.markdown("---")
    st.header("🧠 Challenge Me Mode")
    if st.button("Generate Logic Questions"):
        with st.spinner("Generating questions..."):
            questions = generate_questions(sections)
        st.success("Here are your questions!")
        for i, q in enumerate(questions, 1):
            with st.expander(f"❓ Q{i}: {q['question']}"):
                user_ans = st.text_input(f"Your answer to Q{i}:", key=f"ans_{i}")
                if user_ans:
                    with st.spinner("Evaluating your answer..."):
                        feedback = evaluate_answer(user_ans, q['answer'])
                    st.markdown(f"**Feedback:** {feedback}")
                    st.session_state["history"].append({
                        "action": "challenge", "question": q['question'],
                        "user_answer": user_ans, "feedback": feedback
                    })

    # --- SESSION HISTORY ---
    st.markdown("---")
    st.header("📜 Session History")
    if st.session_state["history"]:
        for item in reversed(st.session_state["history"][-10:]):
            if item["action"] == "summary":
                st.markdown(f"**Summary:** {item['content']}")
            elif item["action"] == "qa":
                st.markdown(f"**Q:** {item['question']}  \n**A:** {item['answer']}")
            elif item["action"] == "challenge":
                st.markdown(f"**Challenge Q:** {item['question']}  \n**Your A:** {item['user_answer']}  \n**Feedback:** {item['feedback']}")
    else:
        st.info("No history yet. Start exploring your document!")

# --- FOOTER ---
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Built with ❤️ using Streamlit and advanced AI. © 2025 Your Name")

