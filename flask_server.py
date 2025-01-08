from flask import Flask, request, jsonify
from chatbot_automation import ChatbotAutomation

app = Flask(__name__)

# Initialize the Selenium ChatbotAutomation instance
driver_path = "/path/to/chrome"
chatbot_url = "https://example.com/chatbot"
bot = ChatbotAutomation(driver_path, chatbot_url)

@app.route('/')
def home():
    return "Chatbot Automation Server Running!"

@app.route('/start_session', methods=['POST'])
def start_session():
    try:
        bot.start_session()
        return jsonify({"message": "Chatbot session started successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/send_query', methods=['POST'])
def send_query():
    try:
        data = request.json
        query = data.get('message')
        bot.send_query(query)
        response = bot.get_response()
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/end_session', methods=['POST'])
def end_session():
    try:
        bot.close_session()
        return jsonify({"message": "Chatbot session closed successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
