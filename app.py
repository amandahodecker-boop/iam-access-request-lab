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

        missing_fields = []

        if not requester or not requester.strip():
            missing_fields.append("Solicitante")

        if not system or not system.strip():
            missing_fields.append("Sistema")

        if not role or not role.strip():
            missing_fields.append("Perfil solicitado")

        if not functions or not functions.strip():
            missing_fields.append("Funções necessárias")

        if not scope or not scope.strip():
            missing_fields.append("Escopo organizacional")

        if not justification or not justification.strip():
            missing_fields.append("Justificativa de negócio")

        if missing_fields:
            return "Campos obrigatórios não preenchidos: " + ", ".join(missing_fields), 400

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