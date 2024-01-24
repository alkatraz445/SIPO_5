from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def display_info():
    name = "Jakub Kraus"
    index_number = "344120"
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return f"{name}\n{index_number}\n{current_datetime}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7777)
