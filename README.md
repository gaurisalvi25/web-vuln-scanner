# Web Application Vulnerability Scanner

## Overview
This project is a Python-based Web Application Vulnerability Scanner that detects common security flaws such as:
- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)

It uses Python libraries like `requests` and `BeautifulSoup` to crawl web forms, submit payloads, and analyze responses for potential vulnerabilities.

---

## Features
- Scan target websites for SQL Injection and XSS vulnerabilities  
- Extract and analyze HTML forms automatically  
- Send crafted payloads and check for security weaknesses  
- Built with pure Python (easy to run, no heavy dependencies)  

---

## Tech Stack
- Language: Python 3  
- Libraries:  
  - `requests` → for sending HTTP requests  
  - `beautifulsoup4` → for parsing HTML content  
  - `urllib.parse` → for handling form actions and URLs  

---

## Project Structure
web-vuln-scanner/
│── scanner.py # Main script for scanning vulnerabilities
│── README.md # Project documentation

---

## Installation & Usage

### 1. Clone the repository

git clone https://github.com/your-username/web-vuln-scanner.git

cd web-vuln-scanner


### 2. Install dependencies

pip install requests beautifulsoup4


### 3. Run the scanner
Edit the TARGET_URL in scanner.py to your desired website, then run:

python scanner.py


Example
Scanning the test site:

TARGET_URL = "http://testphp.vulnweb.com/"

Output (example):

[+] Testing XSS on http://testphp.vulnweb.com/search.php

[!] XSS vulnerability detected in form!

[+] Testing SQL Injection on http://testphp.vulnweb.com/search.php

[!] SQL Injection vulnerability detected in form!


### Disclaimer
This tool is created strictly for educational purposes and for scanning legally owned applications (such as test sites or applications you have explicit permission to test).
Unauthorized scanning of websites may be illegal and is not encouraged.

### Author
Developed by gaurisalvi25

