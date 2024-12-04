# brutebreaker

[![Python2.7](https://img.shields.io/badge/Python-2.7-green.svg?style=flat-square)](https://www.python.org/downloads/release/python-2714/)
![OS](https://img.shields.io/badge/Tested%20On-Linux%20|%20OSX%20|%20Windows%20|%20Android-yellowgreen.svg?style=flat-square) 
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](https://github.com/sujeet0x01/brutebreaker/blob/main/LICENSE)

## Description for BruteBreaker

BruteBreaker is a powerful and efficient brute-force tool designed for ethical hacking and penetration testing. It automates the process of identifying and testing login fields to help security professionals assess the robustness of authentication systems. With a colorful and interactive interface, BruteBreaker combines usability with functionality, ensuring an optimal experience for users.

## Key Features

- Automatic Detection: Identifies username, password, and token fields in web forms.
- Token Support: Handles CSRF tokens automatically for secure requests.
- Progress Indicators: Includes a spinner, progress bar, and colorful banners for a polished UI.
- Customizable: Supports user-defined username and password files for testing.
- Responsibility Focused: Designed for ethical purposes only, promoting secure practices.

# Installation

## For Android
Download [Termux](https://f-droid.org/en/packages/com.termux/)

``` bash
pkg update
pkg upgrade
pkg install git
pkg install python
pip install requests beautifulsoup4
git clone https://github.com/sujeet0x01/brutebreaker
cd BruteBreaker
python BruteBreaker.py
```
## Installation [Linux](https://wikipedia.org/wiki/Linux) [![alt tag](http://icons.iconarchive.com/icons/dakirby309/simply-styled/32/OS-Linux-icon.png)](https://fr.wikipedia.org/wiki/Linux)

``` bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y
pip3 install requests beautifulsoup4
git clone https://github.com/sujeet0x01/brutebreaker
cd BruteBreaker
chmod +x BruteBreaker.py
python3 BruteBreaker.py
```
