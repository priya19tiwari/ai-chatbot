# from google import genai

# client = genai.Client(api_key="AIzaSyDqEjqq3ZDsEOckyurXwqqDyLkHNen55QA")

# models = client.models.list()

# for m in models:
#     print(m.name)
from google import genai

client = genai.Client(api_key="AIzaSyDqEjqq3ZDsEOckyurXwqqDyLkHNen55QA")

models = client.models.list()

for m in models:
    # Show only models that support generateContent (text/chat)
    if "generateContent" in (m.supported_actions or []):
        print(m.name, "=>", m.supported_actions)
