from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
app = Flask(__name__)
CORS(app)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
@app.route("/")
def home():
    return jsonify({"message": "Life Organizer API is running!"})

@app.route("/ai-tutor", methods=["POST"])
def ai_tutor():

    data = request.json

    question = data.get("question", "").strip()
    language = data.get("language", "English")

    if not question:
        return jsonify({
            "answer": "Please enter a question."
        }), 400

    try:

        response = client.responses.create(
            model="gpt-5.6-luna",
            instructions=(
                "You are the AI Tutor for Life Organizer. "
                "Explain things clearly and simply for a student. "
                "Break difficult ideas into small steps. "
                "Use examples when useful. "
                "Do not make explanations unnecessarily complicated. "
                f"Answer in {language}."
            ),
            input=question
        )

        return jsonify({
            "answer": response.output_text
        })

    except Exception as error:

        print("AI Tutor error:", error)

        return jsonify({
            "answer": "Sorry, the AI Tutor could not answer right now. Please try again."
        }), 500

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
