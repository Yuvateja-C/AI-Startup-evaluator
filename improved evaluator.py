from openai import OpenAI
import os
from prompts import get_prompt

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_idea(idea, mode):
    system_prompt = get_prompt(mode)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Evaluate this idea and return JSON:\n{idea}"}
        ]
    )

    return response.choices[0].message.content