from flask import Flask
app = Flask(__name__)

@app.route('/health')
def health():
    return "Got some rare things on sale, stranger!"
