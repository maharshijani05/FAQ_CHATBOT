import os
from flask import Flask, request, jsonify
from faq_chatbot import run_faq_bot

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run_bot():
    data = request.get_json()
    question = data.get('question', '')
    session_id = data.get('session_id', 'default_user')

    response = run_faq_bot(question, session_id)
    return jsonify({'response': response})

if __name__ == "__main__":
    port = int(os.environ["PORT"])
    print(f"Starting server on port {port}")
    app.run(host="0.0.0.0", port=port)
