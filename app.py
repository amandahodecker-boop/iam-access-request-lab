from flask import Flask, redirect, render_template, request

from approval_rules import (
    get_request_status_from_approvals,
    get_required_approvers
)

from database import (
    create_access_request,
    create_approval,
    decide_approval,
    get_access_request,
    list_access_requests,
    list_request_approvals,
    update_access_request_status
)

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

        manager, application_owner = get_required_approvers(
            scope,
            system
        )

        if not manager or not application_owner:
            return render_template(
                "index.html",
                error_message="Área ou sistema inválido para o fluxo de aprovação.",
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

        create_approval(
            request_id=request_id,
            approver_type="manager",
            approver_name=manager
        )

        create_approval(
            request_id=request_id,
            approver_type="application_owner",
            approver_name=application_owner
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


@app.route("/requests/<int:request_id>")
def request_details(request_id):
    access_request = get_access_request(request_id)

    if access_request is None:
        return "Solicitação não encontrada.", 404

    approvals = list_request_approvals(request_id)

    return render_template(
        "request_details.html",
        access_request=access_request,
        approvals=approvals
    )


@app.route(
    "/approvals/<int:approval_id>/<decision>",
    methods=["POST"]
)
def approval_decision(approval_id, decision):
    try:
        request_id = decide_approval(
            approval_id,
            decision
        )
    except ValueError:
        return "Decisão de aprovação inválida.", 400

    if request_id is None:
        return "Aprovação não encontrada.", 404

    approvals = list_request_approvals(request_id)

    approval_statuses = [
        approval["status"]
        for approval in approvals
    ]

    new_status = get_request_status_from_approvals(
        approval_statuses
    )

    update_access_request_status(
        request_id,
        new_status
    )

    return redirect(
        f"/requests/{request_id}"
    )