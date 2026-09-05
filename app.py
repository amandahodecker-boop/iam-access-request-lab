from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "IAM Access Request Lab"
