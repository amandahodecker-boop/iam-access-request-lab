# Entity Relationships

This document describes how the main entities of the IAM Access Request Lab relate to each other.

## User and Access Request

A User can create multiple Access Requests.

Each Access Request belongs to one requester.

## System and Role

A System can contain multiple Roles.

Each Role belongs to one System.

## Access Request and Role

Each Access Request requests one specific Role.

The requested Role determines the access profile being requested for the selected System.

## Access Request and Approval

An Access Request can have multiple Approval records.

Each Approval belongs to one Access Request.

For the MVP, a standard request normally requires:

- one Manager approval;
- one Application Owner approval.

## Access Request and Audit Log

An Access Request can have multiple Audit Log events.

Each Audit Log event belongs to one Access Request.
## Simplified relationship view

```text
User
  |
  | creates
  v
Access Request
  |
  | requests
  v
Role
  |
  | belongs to
  v
System


Access Request
  |
  +---- Approval
  |
  +---- Approval
  |
  +---- Audit Log
  |
  +---- Audit Log

## Identity-centered history

Each user is represented only once in the system and can be associated with multiple access requests over time.

Individual requests remain independent records, while the relationship with the User allows the system to reconstruct the access request history of a specific identity for governance and audit purposes.
