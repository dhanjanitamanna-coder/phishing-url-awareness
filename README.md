# Phishing URL Awareness Checker

## Overview
This is a beginner-friendly Python command-line project that checks URLs for common phishing warning signs.

## Features
- Checks for @ symbol.
- Checks URL length.
- Detects IP address hostnames.
- Checks for 5 or more hostname segments.
- Detects punycode marker (xn--).
- Checks HTTP scheme.
- Allows repeated URL checking and quit option.
- Handles invalid URL input.

## Technologies Used
- Python 3
- urllib.parse
- ipaddress

## Requirements
Python 3.10 or above.
No external packages are required.

## How to Run
1. Open the project folder in VS Code.
2. Open the terminal.
3. Run: python phishing_checker.py
4. Enter a sample URL.
5. Type quit to exit.

## Example Output
Enter URL (or type 'quit' to exit): https://www.example.com/login

--- URL CHECK RESULT --- 

No listed warning signs found.    

This does NOT guarantee that the URL is safe.


## Testing
Five sample URLs from the project workbook were tested.
See tests/test_samples.md for test results.

## Screenshots
Screenshots are available in the screenshots folder.

## Improvements
- Added a loop to check multiple URLs.
- Added a quit option.
- Added invalid URL handling.
- Added warning messages and review-carefully result.

## Limitations
This is educational tool. It is  checks only six warning signs. It does not confirm whether a website is safe or malicious and does not open or scan websites.

## Ethical Use
Use only the sample URLs provided in the project workbook. Do not use this tool to scan real suspicious websites.

## Author
SINDHI TAMANNA BHARATBHAI