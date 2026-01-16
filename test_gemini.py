from google import genai

# Create client with your Gemini API key
client = genai.Client(api_key="AIzaSyDqEjqq3ZDsEOckyurXwqqDyLkHNen55QA")

# Send prompt to Gemini
response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents="Explain Artificial Intelligence in very simple beginner-friendly words."
)

# Print AI reply
print(response.text)
