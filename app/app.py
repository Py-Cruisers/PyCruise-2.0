import rumps
import subprocess, os, sys
from subprocess import CompletedProcess

def openOne(sender):
    print(f”Starting function: {sender.title}“)
    subprocess.run([“/usr/bin/open”, “-a”, “Spotify”])  # waits until calendar exit
    CompletedProcess(args=[‘/usr/bin/open’, ‘-a’, ‘Spotify’], returncode=0)
    subprocess.Popen([“/usr/bin/open”, “-a”, “Spotify”]) # returns immediately

def openTwo(sender):
    print(f”Starting function: {sender.title}“)
    subprocess.run([“/user/bin/open”, “-a”, “Slack”])  # waits until (SPECIFIC APP) exit
    CompletedProcess(args=[‘/user/bin/open’, ‘-a’, ‘Slack’], returncode=0)
    subprocess.Popen([“/user/bin/open”, “-a”, “Slack”]) # returns immediately

def openThree(sender):
        print(f”Starting function: {sender.title}“)
        subprocess.run([“Open app/pyqt/main.py”])
        CompletedProcess(args=[“Open main.py”], returncode=0)
        subprocess.Popen([“Open /app/pyqt/main.py”])

app = rumps.App(‘:rocket:’)
app.menu = [
rumps.MenuItem(‘Open Spotify’, callback=openOne),
rumps.MenuItem(‘Open Slack’, callback=openTwo),
rumps.MenuItem(‘Settings’, callback=openThree),
]

app.run()