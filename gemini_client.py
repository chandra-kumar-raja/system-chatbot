import google.generativeai as genai
from settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def ask_gemini(user_question, specs):
    system_info_text = "\n".join([f"{k}: {v}" for k, v in specs.items()])
    prompt = f"""
    You are a system assistant chatbot that helps the user understand their computer's status.
    Here are the system details you currently know:

    {system_info_text}
    
    Use ONLY this data to answer any questions about CPU, memory, battery, or network.
    Answer the following user question in simple words:
    {user_question}
    """

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text
