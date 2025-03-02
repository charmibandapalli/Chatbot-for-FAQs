from flask import Flask, request, jsonify

app = Flask(__name__)

faq = {
    "What is your name?": "I am a chatbot!",
    "How can I contact support?": "You can email support@example.com.",
    "What services do you offer?": "We offer AI-based chatbot solutions.",
}

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip()
    response = faq.get(user_input, "Sorry, I don't understand that question.")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
