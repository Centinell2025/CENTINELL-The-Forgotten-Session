# CENTINELL — The Forgotten Session | Investigation tasks

## Mission
A retired identity appears in synthetic authentication records at fictional Northvale Enterprises. Determine what was observed, distinguish two separate sessions for the identity, and avoid claiming attribution or data theft without proof.

**Difficulty:** Easy | **Category:** Digital Forensics | **Expected duration:** 30–45 minutes

## Evidence order
1. Validate integrity of the baseline CSV artifacts with `python tools/verify_evidence.py`.
2. Read `evidence/account_status.csv` to identify retired identities.
3. Independently query `evidence/authentication_correlation.csv`. This new file is a teaching-friendly normalized supplementary dataset, not a native EVTX export; its baseline record values overlap the original CSV.
4. Correlate by **computer + target_user + logon_id**, not by username alone. A different source or computer may represent a different session.
5. Record the exact row ID and source field for each answer.

## Questions (student-facing; no answers)
1. Which account was marked Retired before the incident day?
2. What is the exact UTC timestamp when that account was marked Retired?
3. How many successful Event ID 4624 records belong to that identity **across all computers** in the correlation dataset?
4. Which two hostnames recorded those successful authentications? Return alphabetical order, comma-separated.
5. What is the source IPv4 address of the retired identity's **earlier** successful authentication?
6. On NVE-WS14, what is the UTC timestamp of the retired identity's failed logon immediately preceding its successful logon?
7. On NVE-WS14, which record_id documents the successful authentication of the retired identity?
8. What is the logon_id (including `0x`) for that NVE-WS14 successful session?
9. What is the timestamp of the matching NVE-WS14 logoff, matching by computer, account and logon_id?
10. What is the session duration in seconds, from successful NVE-WS14 logon to its matching logoff?

## Reporting requirement
For each answer, cite the file, `record_id` where applicable, the precise CSV field, and a concise justification. For Q10 show the timestamp subtraction. Do not infer the human actor, intent, malware execution, lateral movement or data theft from this evidence.

## Validation rubric
Each question should have one exact, dataset-derived answer. Treat a mere retired-account authentication as a potentially unauthorized access indicator requiring triage, not confirmed compromise.
