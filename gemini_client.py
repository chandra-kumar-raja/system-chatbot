import google.generativeai as genai
from settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def ask_gemini(user_question, specs):
    system_info_text = "\n".join([f"{k}: {v}" for k, v in specs.items()])
    prompt = f"""
    You are a system assistant. Here are the current system specs:

    {system_info_text}

    Answer the following user question in simple words:
    {user_question}
    """

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text
