# Student Guide — CENTINELL: The Forgotten Session

## Role
You are a junior DFIR investigator working with synthetic normalized Windows-style security data from a fictional organization. Do not treat these CSVs as native EVTX evidence.

## Goals
- Understand 4624 (successful logon), 4625 (failure), and 4634 (logoff).
- Join an account status inventory to authentication activity.
- Distinguish different hosts, IP addresses and logon IDs.
- Calculate a session duration using UTC timestamps.
- Explain evidence limits and avoid unsupported attacker attribution.

## Procedure
1. Run `python tools/verify_evidence.py` to verify the two **original** CSVs listed in `SHA256SUMS.txt`. Note the supplemental CSV is outside that manifest.
2. Read `evidence/account_status.csv` to establish which identity was retired and when.
3. Open `evidence/authentication_correlation.csv` and filter by that identity.
4. Count successful 4624 events across all computers. Note the earlier and later occurrences are distinct sessions.
5. On `NVE-WS14`, inspect a preceding 4625, the 4624, and the matching 4634 using account, computer and logon_id.
6. Answer all ten questions in `INVESTIGATION_TASKS.md` and supply a short evidence-based justification per answer.

## Recommended tools
CSV viewer, spreadsheet, or Python 3 standard library. No privileged permissions, network connectivity, malware or VM are required.

## Evidence limitations
The baseline data includes descriptive hints useful in onboarding. The challenge questions require the extended dataset. Windows Event ID 4634 reflects a logoff record, but no human attribution or data theft can be inferred from it.

## Success criteria
Every answer is exact and reproducible; you document row IDs, timestamps in UTC and the calculation for session duration.
