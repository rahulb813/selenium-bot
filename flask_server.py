from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Chatbot Server is Running!"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    # Replace this with your chatbot logic
    response = f"You said: {user_message}"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="192.168.1.105", port=5000)
