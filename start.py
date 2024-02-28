import subprocess

subprocess.call(['netsh', 'wlan', 'show', 'profiles'])
profile = input("Wifi name: ")
subprocess.call(['netsh', 'wlan', 'show', 'profiles', profile, "key=clear"])