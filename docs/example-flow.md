# Example Access Request Flow

This document demonstrates a complete access request lifecycle using the fictional users and systems defined in the IAM Access Request Lab.

## Scenario

João Ribeiro is an Operations Assistant at NovaCore Technologies.

He needs read-only access to ServiceFlow to consult the status and history of operational requests related to his work.

### Access request

- Request ID: AR-0001
- Requester: João Ribeiro
- System: ServiceFlow
- Requested Role: Viewer
- Requested Functions:
  - View operational requests
  - View request history
- Business Justification: Required to monitor operational requests related to daily activities.
- Manager Approver: Marina Lopes
- Application Owner: Marcelo Azevedo
- Status: PENDING_APPROVAL
- ## Approval steps

### Manager approval

Marina Lopes reviews the request and approves it based on João's business need.

- Approval Type: Manager
- Approver: Marina Lopes
- Decision: APPROVED
- Request Status: PENDING_APPROVAL

The request remains pending because the Application Owner approval is still required.

### Application Owner approval

Marcelo Azevedo reviews whether the requested ServiceFlow Viewer role is appropriate for João's stated activities.

- Approval Type: Application Owner
- Approver: Marcelo Azevedo
- Decision: APPROVED
- Request Status: APPROVED
## Provisioning

After all required approvals are completed, the request becomes eligible for provisioning.

Diego Freitas, acting as IAM Analyst, grants the approved ServiceFlow Viewer access to João Ribeiro.

- Provisioned By: Diego Freitas
- Provisioned Access: ServiceFlow Viewer
- Request Status: PROVISIONED

## Audit trail

The request history records the main events that occurred during the lifecycle of AR-0001:

```text
10:00 - REQUEST_CREATED
Performed by: João Ribeiro

10:20 - APPROVAL_COMPLETED
Performed by: Marina Lopes
Decision: APPROVED

10:40 - APPROVAL_COMPLETED
Performed by: Marcelo Azevedo
Decision: APPROVED

10:40 - STATUS_CHANGED
From: PENDING_APPROVAL
To: APPROVED

11:15 - ACCESS_PROVISIONED
Performed by: Diego Freitas
Access: ServiceFlow Viewer

11:15 - STATUS_CHANGED
From: APPROVED
To: PROVISIONED
  
