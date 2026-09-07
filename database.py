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