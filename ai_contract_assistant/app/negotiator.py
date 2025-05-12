
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def negotiate_clauses(clauses):
    improved = []
    for clause in clauses:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a contract negotiation expert."},
                {"role": "user", "content": f"Improve this clause: {clause}"}
            ]
        )
        improved.append(response['choices'][0]['message']['content'])
    return improved
