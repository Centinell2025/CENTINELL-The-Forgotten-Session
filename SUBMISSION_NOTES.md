# Submission readiness — CENTINELL: The Forgotten Session

**Proposed difficulty:** Easy · **Proposed category:** Digital Forensics

## Student-facing content
README, STUDENT_GUIDE, INVESTIGATION_TASKS, account status CSV, baseline event CSV, supplemental 22-record correlation CSV, baseline integrity manifest and checking script.

## Author deliverables still required
- [ ] Instructor-only walkthrough and ten-answer grading key (do **not** commit publicly).
- [ ] Validate every question independently against supplemental records.
- [ ] Refresh integrity manifest to also cover `evidence/authentication_correlation.csv` and test checker.
- [ ] Produce versioned Sherlock evidence ZIP and, if requested by HTB, a reviewer download.
- [ ] Confirm current HTB requirements, supported formats and submission links.
- [ ] Consider obtaining native EVTX from a fully isolated synthetic Windows testbed if platform guidelines expect those artifacts.

## Known pedagogical limitation
The seven-record baseline CSV contains explicit analyst-context hints and reveals the retired account. The extended dataset increases correlation work, but this is still an introductory case, not a realistic full incident investigation. Avoid claiming that this lab proves adversary intrusion.
