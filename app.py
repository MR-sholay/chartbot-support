from flask import Flask, request, jsonify
from chatbot import chatbot

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot.get_response(user_input)
    return jsonify({"response": str(response)})

@app.route("/")
def home():
    return "Welcome to the Smart Chatbot API!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

@app.route("/")
def home():
    return "Welcome to the Smart Chatbot API!"
