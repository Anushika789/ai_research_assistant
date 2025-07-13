from modules.summarizer import ai_summarize

def generate_questions(sections, language="English", num_questions=3):
    if not sections:
        return [{"question": "No document sections found.", "answer": ""}]
    context = "\n\n".join([txt for _, txt in sections])
    prompt = (
        f"From the following document, generate {num_questions} logic/comprehension questions "
        f"with answers in {language}:\n\n{context}"
    )
    qa_text = ai_summarize(prompt, length=num_questions*2)
    # For now, return as a single question/answer block.
    return [{"question": qa_text, "answer": ""}]

def evaluate_answer(user_answer, correct_answer, language="English"):
    if not user_answer or not correct_answer:
        return "No user answer or correct answer provided."
    prompt = (
        f"Compare the user's answer to the correct answer and provide feedback with justification.\n\n"
        f"User Answer: {user_answer}\nCorrect Answer: {correct_answer}"
    )
    feedback = ai_summarize(prompt, length=2)
    return feedback
