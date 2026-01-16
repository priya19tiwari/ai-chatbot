from flask import Flask, request, jsonify, render_template
from google import genai

# IMPORTANT: Replace with your NEW Gemini API key
client = genai.Client(api_key="AIzaSyDqEjqq3ZDsEOckyurXwqqDyLkHNen55QA")

app = Flask(__name__)

# Serve frontend page
@app.route("/")
def home():
    return render_template("index.html")

# Chat API route
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data["message"]

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents= f"""
        Answer in plain text only.
        Do not use *, **, ##, bullets, or markdown.
        Explain simply like a teacher.

        Question: {user_message}
        """
    )

    # Safe response extraction
    try:
        ai_reply = response.text
    except:
        ai_reply = "AI response error"

    print("AI RESPONSE:", ai_reply)

    return jsonify({"reply": ai_reply})


if __name__ == "__main__":
    app.run(debug="0.0.0.0", port=10000)
