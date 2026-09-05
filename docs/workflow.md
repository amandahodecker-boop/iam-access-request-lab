# Access Request Workflow

## Standard approval flow

A standard access request requires approval from both the requester's manager and the Application Owner.

The manager validates the business need for the requested access.

The Application Owner validates whether the requested system access and permissions are appropriate.

After both approvals, the request can be provisioned by an IAM Analyst.

## Request status

The MVP uses the following request statuses:

- `PENDING_APPROVAL` - The request was submitted and is waiting for approval.
- `APPROVED` - All required approvals were completed, but the access has not yet been provisioned.
- `REJECTED` - The request was rejected by one of the required approvers.
- `PROVISIONED` - The approved access was successfully granted.
