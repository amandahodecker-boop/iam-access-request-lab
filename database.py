import sqlite3

DATABASE = "iam_lab.db"


def init_db():
    connection = sqlite3.connect(DATABASE)

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS access_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            requester TEXT NOT NULL,
            system TEXT NOT NULL,
            role TEXT NOT NULL,
            functions TEXT NOT NULL,
            scope TEXT NOT NULL,
            justification TEXT NOT NULL,
            reference_user TEXT,
            status TEXT NOT NULL DEFAULT 'pending_approval',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    connection.execute(
    """
        CREATE TABLE IF NOT EXISTS approvals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            request_id INTEGER NOT NULL,
            approver_type TEXT NOT NULL,
            approver_name TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending',
            decided_at TIMESTAMP,
            FOREIGN KEY (request_id) REFERENCES access_requests(id)
        )
        """
)
    connection.commit()
    connection.close()


def create_access_request(
    requester,
    system,
    role,
    functions,
    scope,
    justification,
    reference_user
):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.execute(
        """
        INSERT INTO access_requests (
            requester,
            system,
            role,
            functions,
            scope,
            justification,
            reference_user
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            requester,
            system,
            role,
            functions,
            scope,
            justification,
            reference_user
        )
    )

    connection.commit()

    request_id = cursor.lastrowid

    connection.close()

    return request_id
def list_access_requests():
    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    requests = connection.execute(
        """
        SELECT
            id,
            requester,
            system,
            role,
            scope,
            status,
            created_at
        FROM access_requests
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return requests
def create_approval(request_id, approver_type, approver_name):
    connection = sqlite3.connect(DATABASE)

    connection.execute(
        """
        INSERT INTO approvals (
            request_id,
            approver_type,
            approver_name
        )
        VALUES (?, ?, ?)
        """,
        (
            request_id,
            approver_type,
            approver_name
        )
    )

    connection.commit()
    connection.close()

def list_request_approvals(request_id):
    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    approvals = connection.execute(
        """
        SELECT
            id,
            request_id,
            approver_type,
            approver_name,
            status,
            decided_at
        FROM approvals
        WHERE request_id = ?
        ORDER BY id
        """,
        (request_id,)
    ).fetchall()

    connection.close()

    return approvals 
def get_access_request(request_id):
    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    access_request = connection.execute(
        """
        SELECT
            id,
            requester,
            system,
            role,
            functions,
            scope,
            justification,
            reference_user,
            status,
            created_at
        FROM access_requests
        WHERE id = ?
        """,
        (request_id,)
    ).fetchone()

    connection.close()

    return access_request
def decide_approval(approval_id, decision):
    allowed_decisions = ("approved", "rejected")

    if decision not in allowed_decisions:
        raise ValueError("Decisão de aprovação inválida.")

    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    approval = connection.execute(
        """
        SELECT request_id
        FROM approvals
        WHERE id = ?
        """,
        (approval_id,)
    ).fetchone()

    if approval is None:
        connection.close()
        return None

    connection.execute(
        """
        UPDATE approvals
        SET
            status = ?,
            decided_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (
            decision,
            approval_id
        )
    )

    connection.commit()

    request_id = approval["request_id"]

    connection.close()

    return request_id
def update_access_request_status(request_id, status):
    connection = sqlite3.connect(DATABASE)

    connection.execute(
        """
        UPDATE access_requests
        SET status = ?
        WHERE id = ?
        """,
        (
            status,
            request_id
        )
    )

    connection.commit()
    connection.close()