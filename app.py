from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        requester = request.form.get("requester")

        return f"Solicitação recebida para: {requester}"

    return render_template("index.html")

