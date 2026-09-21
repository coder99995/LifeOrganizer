from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

supported_languages = {
    "English": "en",
    "Swedish": "sv",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Arabic": "ar",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Portuguese": "pt",
    "Italian": "it",
    "Dutch": "nl",
    "Turkish": "tr",
    "Russian": "ru",
    "Gujarati": "gu",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Punjabi": "pa",
    "Urdu": "ur"
}


@app.route("/")
def home():
    return jsonify({
        "message": "Life Organizer API is running!"
    })


@app.route("/languages", methods=["GET"])
def get_languages():
    return jsonify(supported_languages)


@app.route("/ai-tutor", methods=["POST"])
def ai_tutor():

    data = request.get_json(silent=True) or {}

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
                "You are the AI Tutor inside the Life Organizer app. "
                "You are helping a school student learn. "

                "Explain answers in simple, understandable language. "
                "Break difficult topics into small steps. "
                "Use examples when helpful. "

                "For mathematics, show the calculation step by step. "
                "For science, explain the important ideas clearly. "
                "For history, explain events, causes and effects clearly. "

                "Do not make answers unnecessarily complicated. "
                "If the student makes a mistake, explain the mistake "
                "kindly and show how to correct it. "

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
            "answer": (
                "Sorry, the AI Tutor could not answer right now. "
                "Please try again."
            )
        }), 500


if __name__ == "__main__":

    print("Life Organizer server is starting...")
    print("Server running at http://127.0.0.1:5000")

    app.run(
        debug=True,
        port=5000
    )
