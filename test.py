import json
from openai import OpenAI

client = OpenAI(
    api_key="sk-5257e4633cdb4a08a7b3f82a78514d37",
    base_url="https://api.deepseek.com",
)

system_prompt = """
The user will make filosofal questions and you will answer them in a JSON format.
The JSON should contain two fields: "question" and "answer".

EXAMPLE INPUT: 
Which is the highest mountain in the world? Mount Everest.

EXAMPLE JSON OUTPUT:
{
    "question": "What is life?",
    "answer": "Life is a complex and multifaceted phenomenon that encompasses biological, philosophical, and existential dimensions. It is characterized by growth, reproduction, functional activity, and continual change preceding death. In a broader sense, life can also refer to the experience of living and the pursuit of meaning and purpose within that existence."
}
"""

user_prompt = "Explain the Cave of Plato in a JSON format."

messages = [{"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}]

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    response_format={
        'type': 'json_object'
    }
)

# Parse the JSON response
parsed_response = json.loads(response.choices[0].message.content)

# Save the JSON to a file
with open("output.json", "w") as json_file:
    json.dump(parsed_response, json_file, indent=4)

print("JSON salvo em 'output.json'")