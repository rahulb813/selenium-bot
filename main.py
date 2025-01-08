from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ChatbotAutomation:
    def __init__(self, driver_path, chatbot_url):
        options = webdriver.ChromeOptions()
        options.binary_location = driver_path
        options.add_argument('--remote-debugging-port=9222')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')  # Optional: Run without GUI
        self.driver = webdriver.Chrome(options=options)
        self.chatbot_url = chatbot_url

    def start_session(self):
        try:
            self.driver.get(self.chatbot_url)
        except Exception as e:
            print(f"Invalid URL or Error starting session: {e}")

    def send_query(self, query):
        try:
            input_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]'))
            )
            input_box.clear()
            input_box.send_keys(query + Keys.RETURN)
            time.sleep(2)  # Allow time for the bot to respond
        except Exception as e:
            print(f"Error sending query: {e}")

    def get_response(self):
        try:
            response_boxes = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'chatbot-response'))
            )
            responses = [box.text for box in response_boxes]
            return responses[-1] if responses else None
        except Exception as e:
            print(f"Error fetching response: {e}")
            return None

    def handle_multiple_queries(self, queries):
        responses = []
        for query in queries:
            self.send_query(query)
            responses.append(self.get_response())
        return responses

    def close_session(self):
        self.driver.quit()

# Example usage
if __name__ == "__main__":
    driver_path = "/path/to/chrome"
    chatbot_url = "https://example.com/chatbot"
    bot = ChatbotAutomation(driver_path, chatbot_url)

    bot.start_session()
    queries = ["Hello!", "What's the weather like today?", "Tell me a joke."]
    responses = bot.handle_multiple_queries(queries)
    for query, response in zip(queries, responses):
        print(f"Query: {query} -> Response: {response}")
    bot.close_session()

# Example usage
if __name__ == "__main__":
    driver_path = "chromedriver.exe"
    chatbot_url = "192.168.1.105/chatbot"
    bot = ChatbotAutomation(driver_path, chatbot_url)

    bot.start_session()
    queries = ["Hello!", "What's the weather like today?", "Tell me a joke."]
    responses = bot.handle_multiple_queries(queries)
    for query, response in zip(queries, responses):
        print(f"Query: {query} -> Response: {response}")
    bot.close_session()
