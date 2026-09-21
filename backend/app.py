from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Life Organizer API is running!"})


@app.route("/ai-tutor", methods=["POST"])
def ai_tutor():
    data = request.json
    question = data.get("question", "")
    language = data.get("language", "English")

    if not question:
        return jsonify({"answer": "Please enter a question."})

    answer = (
        f"AI Tutor language: {language}. "
        f"You asked: {question}. "
        "The AI Tutor backend is working!"
    )

    return jsonify({"answer": answer})


if __name__ == "__main__":
    print("Life Organizer server is starting...")
    print("Server running at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
