# CENTINELL — The Forgotten Session

**Difficulty:** Easy | **Category:** Digital Forensics / Authentication Logs

## Case briefing
On October 9, 2026, Northvale Enterprises (entirely fictional) reviewed authentication activity on workstation `NVE-WS14`. A retired account may have been used after its scheduled departure. Investigate the attached evidence and reconstruct the relevant logon. Do not assume every failed logon is malicious.

## Learning objectives
- Interpret Windows Security Event IDs 4624 (successful logon), 4625 (failed logon), and 4634 (logoff) in exported records.
- Distinguish source IP, target username, and logon ID.
- Correlate the account inventory with authentication events.
- Extract exact UTC-formatted answers from the evidence.

## Evidence
- `evidence/windows_security_events.csv` — **synthetic lab-generated** Windows-like event exports (not an original EVTX capture).
- `evidence/account_status.csv` — fictional HR / account status inventory.
- `SHA256SUMS.txt` — SHA-256 hashes of the evidence files.

All names, hosts, addresses, events and timestamps are part of this fictional training exercise. IP addresses are private RFC1918 examples. No external Internet access is required.

## Workflow
1. Inspect `account_status.csv` and identify accounts that are no longer active.
2. Find that account in `windows_security_events.csv`.
3. Identify its successful authentication record (`event_id=4624`).
4. Compare that record with the earlier failed logon and subsequent logoff using `logon_id` where available.
5. Submit the exact answers as recorded (UTC timestamps use `YYYY-MM-DDTHH:MM:SSZ`).

## Investigation questions
1. Which retired user account successfully logged on to the workstation?
2. What is the workstation hostname involved in that successful logon?
3. What is the source IP address for that successful logon?
4. At what exact UTC time was the successful logon recorded?
5. Which Windows Security Event ID identifies that successful logon?

## Student safety
This exercise is passive log analysis only; no attacks or live targets are involved.
