from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        requester = request.form.get("requester")
        system = request.form.get("system")
        role = request.form.get("role")
        functions = request.form.get("functions")
        scope = request.form.get("scope")
        justification = request.form.get("justification")
        reference_user = request.form.get("reference_user")

        return (
            f"Solicitante: {requester} | "
            f"Sistema: {system} | "
            f"Perfil: {role} | "
            f"Funções: {functions} | "
            f"Escopo: {scope} | "
            f"Justificativa: {justification} | "
            f"Usuário de referência: {reference_user}"
        )

    return render_template("index.html")