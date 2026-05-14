import os
from groq import Groq

# 1. Setup the client
# Paste your Groq key between the quotes below
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
print("--- JEE AI STUDY AGENT (GROQ EDITION) ---")

while True:
    topic = input("\nEnter a JEE topic (or type 'exit'): ")
    
    if topic.lower() == 'exit':
        break
    
    # 2. Creating the 'Autonomous' Teacher Persona
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an IIT Professor specializing in JEE coaching. "
                            "Explain formulas clearly and always follow up with a difficult conceptual question."
            },
            {
                "role": "user",
                "content": f"Explain the core formula for {topic} and give me a JEE-level challenge.",
            }
        ],
        model="llama-3.3-70b-versatile", # This is the 'smart' model
    )

    # 3. Print the result
    print("\nPROFESSOR SAYS:")
    print(chat_completion.choices[0].message.content)