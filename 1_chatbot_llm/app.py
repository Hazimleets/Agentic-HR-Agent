from flask import Flask
from routes import generate_bp
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.register_blueprint(generate_bp)

@app.route("/", methods=["GET"])
def index():
    return "✅ Flask server is running! Send POST requests to /generate"


if __name__ == "__main__":
    app.run(debug=True)
