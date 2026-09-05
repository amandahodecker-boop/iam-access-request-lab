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
## Self-approval restriction

A user cannot approve their own access request.

If the requester is also the person who would normally act as their manager approver, an alternate approver must be used.

The alternate approver must be a previously defined authority with enough responsibility to validate the request independently.

This rule prevents self-approval and reduces conflicts of interest in the access request process.
## Exception flow

Example:

1. Laura Martins requests access to NovaERP.
2. Laura cannot approve her own request.
3. Camila Torres acts as the alternate approver.
4. Rafael Nunes, as NovaERP Application Owner, performs the system-level approval.
5. Diego Freitas, as IAM Analyst, provisions the approved access.
