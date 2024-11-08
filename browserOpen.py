#! python3
# This format is more complicated than what was in the textbook because I'm using WSL Ubuntu, which has trouble accessing
# the default windows browser.  Extra steps are needed to make the code accessible to other OSs.
import webbrowser
import subprocess
import sys
import os

def is_wsl():
    """Check if running inside WSL"""
    try:
        with open('/proc/sys/kernel/osrelease', 'r') as f:
            os_release = f.read().strip()
            if 'Microsoft' in os_release:  # WSL2 will include 'Microsoft' in the kernel release string
                return True
    except FileNotFoundError:
        pass
    return False

def open_url(url):
    try:
        # Check if running in WSL by inspecting /proc/sys/kernel/osrelease
        if is_wsl():
            print("Detected WSL. Using cmd.exe to open URL.")
            subprocess.run(["cmd.exe", "/c", "start", url])
        else:
            print("Not in WSL. Using webbrowser.open() for non-WSL system.")
            webbrowser.open(url)

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
open_url("https://inventwithpython.com/")
