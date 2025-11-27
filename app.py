from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Lesego! Your app is LIVE on the cloud!"

if __name__ == "__main__":
    app.run()
