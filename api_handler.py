import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # store your key in .env or set manually

def generate_ai_tip(missing_skills):
    prompt = f"""
    Act as a career coach. A resume is missing these skills: {missing_skills}.
    Give clear, concise tips to improve the resume for a software job.
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use gpt-4 if you have access
            messages=[
                {"role": "system", "content": "You are a helpful AI career assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message['content']
    
    except Exception as e:
        return "⚠️ AI tip not available. Please check your OpenAI API key or usage limits."
