# Student investigation guide — The Forgotten Session

## Scenario and scope
You are a junior SOC analyst reviewing a small exported collection of Windows-style security events for a fictional company. The account-status register is your independent source for employee status; the security export is your source for authentication activity. Both are **synthetic educational data**, not native Windows EVTX.

**Estimated time:** 15–25 minutes. **Difficulty:** Easy.

## Recommended tools
Use a spreadsheet application, a CSV viewer, or Python's built-in `csv` module. No privileged access, malware samples or network connectivity are needed.

## Investigation procedure
1. Verify the two evidence files using the hashes in `SHA256SUMS.txt` (or `python tools/verify_evidence.py`).
2. Read the account register and identify statuses that merit follow-up.
3. Filter security events to the account(s) discovered in step 2.
4. Compare logon outcomes: 4625 (failure) is not 4624 (success).
5. Confirm the event's workstation and source IP.
6. Preserve the recorded timestamp with its UTC marker (`Z`).
7. Cross-check the logon ID against any matching logoff. Avoid assuming a logoff means the account was legitimate.

## Investigation questions (answer exactly)
1. Which **retired user account** successfully logged on?
2. Which **workstation hostname** recorded that successful logon?
3. Which **source IPv4 address** was associated with it?
4. At what **exact UTC timestamp** did it occur? Use `YYYY-MM-DDTHH:MM:SSZ`.
5. Which **Windows Security Event ID** represents the successful logon?

## Reporting worksheet
Create a short finding for each question stating the value, the evidence file, and the row or field used. Do not include guessed answers.

## Analyst note
The logs alone cannot prove the person behind the credentials, and a retired identity successfully authenticating does not by itself prove data theft. Explain the observed authentication event, not unsupported consequences.
