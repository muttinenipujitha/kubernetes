from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    return "hello world"

@app.route('/login')
def login():
    return "login into the user"



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
