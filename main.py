from groq import Groq

# Insert your Groq API key here
client = Groq(api_key="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")

# Ask the user a legal question
question = input("Ask a legal question: ")

# Send request to LLaMA 3 (70B) via Groq
response = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {"role": "system", "content": "You are a helpful legal assistant who provides detailed and clear answers."},
        {"role": "user", "content": question}
    ]
)

# Print the response
print("\nAssistant:", response.choices[0].message.content.strip())
