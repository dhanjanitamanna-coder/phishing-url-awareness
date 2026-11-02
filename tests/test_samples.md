# Test Results

**Project:** Phishing URL Awareness Checker  
**Date:** 02 November 2026  
**Operating System:** Windows  
**Python Version:** python 3.15

| Test | Expected Result | Actual Result | Status |
|---|---|---|---|
| 1 | No listed warning signs | No listed warning signs | PASS |
| 2 | IP address + HTTP warnings | IP address + HTTP warnings | PASS |
| 3 | @ symbol + HTTP warnings | @ symbol + HTTP warnings | PASS |
| 4 | 5 or more hostname segments warning | Hostname segments warning | PASS |
| 5 | Punycode warning | Punycode warning | PASS |


## Notes
- All five workbook sample URLs were tested.
- The program does not open or visit any URL.
- No warning signs do not guarantee that a URL is safe.
