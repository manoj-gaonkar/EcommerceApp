from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<center><p>Hello world!</p></center>"

if __name__ == "__main__":
    app.run()

