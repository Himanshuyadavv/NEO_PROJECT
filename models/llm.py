import google.generativeai as genai
from config.config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

def generate_response(prompt, mode="concise"):
    """Generate response using Gemini"""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        if mode == "concise":
            system_prompt = "You are a helpful assistant. Provide very concise answers. Keep responses brief and under 50 words."
        else:
            system_prompt = "You are a helpful assistant. Provide detailed answers with examples and explanations. Aim for 150-200 words."
        
        response = model.generate_content([system_prompt, prompt])
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"