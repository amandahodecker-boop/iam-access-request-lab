# Data Model

## Access Request

An Access Request represents a request made by a user to receive a specific level of access to a corporate system.

Initial fields for the MVP:

| Field | Purpose |
|---|---|
| Request ID | Unique identifier for the request |
| Requester | User requesting the access |
| System | Corporate system being requested |
| Requested Role | Access profile requested |
| Requested Functions | Activities or permissions the user needs |
| Organizational Scope | Business unit, branch, or scope the access should cover |
| Business Justification | Business reason for requesting the access |
| Reference User | Optional user used only as a reference for access analysis |
| Status | Current stage of the request |
| Created At | Date and time the request was created |
| Manager Approver | Manager responsible for business approval |
| Application Owner | Owner responsible for system-level approval |
| Provisioned By | IAM Analyst who granted the access |
| Provisioned At | Date and time the access was provisioned |
### MVP Rule

The Requested Role is mandatory when an access request is submitted.

The requester must select an existing role associated with the selected corporate system. Role descriptions will help users understand which access profile best matches their business need.
