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
## Approval

An Approval represents an individual decision made as part of an access request workflow.

Initial fields for the MVP:

| Field | Purpose |
|---|---|
| Approval ID | Unique identifier for the approval record |
| Request ID | Access Request associated with this approval |
| Approval Type | Responsibility under which the decision was made, such as Manager or Application Owner |
| Approver | User who made the decision |
| Decision | APPROVED or REJECTED |
| Decision Comment | Optional explanation for the decision |
| Decided At | Date and time the decision was made |
## Audit Log

The Audit Log records important events that occur during the lifecycle of an access request.

It provides a chronological history of actions without replacing the detailed records stored in other entities such as Approval.

Initial fields for the MVP:

| Field | Purpose |
|---|---|
| Log ID | Unique identifier for the audit event |
| Request ID | Access Request associated with the event |
| Event Type | Type of event that occurred |
| Performed By | User who performed the action |
| Event Details | Additional context about the event |
| Created At | Date and time the event occurred |
### Audit rule

Audit events must preserve the historical sequence of actions performed in the system.

Existing audit records should not be silently overwritten when a new action occurs. New events should be added to the history instead.
