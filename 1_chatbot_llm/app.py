from flask import Flask
from routes import generate_bp
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.register_blueprint(generate_bp)

if __name__ == "__main__":
    app.run(debug=True)
