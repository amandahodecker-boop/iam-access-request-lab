AREA_MANAGERS = {
    "operations": "Marina Lopes",
    "finance": "Laura Martins",
    "hr": "Helena Duarte",
    "technology": "Marcelo Azevedo",
    "information_security": "Camila Torres"
}


APPLICATION_OWNERS = {
    "novaerp": "Rafael Nunes",
    "peoplehub": "Helena Duarte",
    "serviceflow": "Marcelo Azevedo"
}


def get_required_approvers(scope, system):
    manager = AREA_MANAGERS.get(scope)
    application_owner = APPLICATION_OWNERS.get(system)

    return manager, application_owner
def get_request_status_from_approvals(approval_statuses):
    if "rejected" in approval_statuses:
        return "rejected"

    if approval_statuses and all(
        status == "approved" for status in approval_statuses
    ):
        return "approved"

    return "pending_approval"