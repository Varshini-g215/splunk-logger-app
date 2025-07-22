from flask import Flask, request, jsonify
from splunk_logger import get_logger

app = Flask(__name__)
logger = get_logger()

@app.route('/')
def home():
    logger.info('Home route accessed')
    return "Welcome to the Splunk Logging Demo!"

@app.route('/log', methods=['POST'])
def log():
    data = request.get_json()
    message = data.get('message', 'No message provided')
    level = data.get('level', 'info').lower()

    if level == 'debug':
        logger.debug(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'error':
        logger.error(message)
    else:
        logger.info(message)

    return jsonify({"status": "logged", "level": level, "message": message})

if __name__ == '__main__':
    app.run(debug=True)
