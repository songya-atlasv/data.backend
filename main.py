from flask import Flask, app


app = Flask(__name__)


@app.route('/')
def home():
    return "first app!!!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)