#! python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.

import subprocess, webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = '+'.join(sys.argv[1:])
    print(address)
else:
    # Get address from command line.
    address = pyperclip.paste()
url = 'https://www.google.com/maps/place/' + address
print(url)

subprocess.run(["cmd.exe", "/c", "start", url])
