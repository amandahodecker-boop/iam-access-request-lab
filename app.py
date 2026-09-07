from flask import Flask, render_template, request

from database import create_access_request, list_access_requests

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
            missing_fields.append("Área")

        if not justification or not justification.strip():
            missing_fields.append("Justificativa de negócio")

        if missing_fields:
            error_message = (
                "Preencha os campos obrigatórios: "
                + ", ".join(missing_fields)
            )

            return render_template(
                "index.html",
                error_message=error_message,
                form_data=request.form
            ), 400

        request_id = create_access_request(
            requester=requester,
            system=system,
            role=role,
            functions=functions,
            scope=scope,
            justification=justification,
            reference_user=reference_user
        )

        return (
            f"Solicitação #{request_id} criada com sucesso. "
            "Status: aguardando aprovação."
        )

    return render_template("index.html")


@app.route("/requests")
def requests_list():
    access_requests = list_access_requests()

    return render_template(
        "requests.html",
        access_requests=access_requests
    )