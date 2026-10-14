# CENTINELL — The Forgotten Session

**Hack The Box Sherlock candidate** · **Difficulty:** Easy · **Category:** Digital Forensics / Authentication Logs

## Scenario
On 9 October 2026, the SOC at **Northvale Enterprises** (a completely fictional training organization) reviewed unusual activity involving an identity retired the previous month. A small set of Windows-like event records spans several workstations and includes legitimate activity, failed logons, and more than one session for the retired identity. Investigators must determine exactly what the data establishes.

## Investigation objective
Correlate account status and authentication events; isolate the relevant host/session; establish a defensible timeline and session duration. Distinguish suspicious authentication from evidence of an actual intrusion.

## Files
- `evidence/account_status.csv`: synthetic account-lifecycle inventory.
- `evidence/windows_security_events.csv`: original seven-row baseline dataset with annotated descriptions for orientation.
- `evidence/authentication_correlation.csv`: **extended 22-record challenge dataset** with competing sessions and record IDs.
- `STUDENT_GUIDE.md`: analysis instructions.
- `INVESTIGATION_TASKS.md`: 10 graded questions and reporting criteria.
- `SHA256SUMS.txt`: hashes of the **two original** CSV files only. The supplemental extended file is not covered by this older manifest.
- `tools/verify_evidence.py`: baseline-hash checker; not a verifier of supplemental data.

## Start
Read `STUDENT_GUIDE.md` and answer the questions in `INVESTIGATION_TASKS.md`. Work with UTC timestamps exactly as represented. The baseline logs show the case context and may reveal part of the investigative trail; the extended file is the canonical source for questions involving multi-host correlation and record IDs.

## Educational integrity and safety
All accounts, infrastructure, addresses and events are simulated. These are **synthetic CSV data**, not forensic images or original Windows EVTX captures. No real organization is implicated. The dataset does not establish who used the credentials, malware activity or exfiltration. No live targets or hacking actions are required.

## Author submission caution
The public repository intentionally omits answer keys. A separately supplied instructor-only writeup, exact answer key, evidence checks and current platform submission requirements are needed before the package should be called submission-ready.
