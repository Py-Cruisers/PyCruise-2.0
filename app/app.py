import rumps
import subprocess, os, sys
from subprocess import CompletedProcess

def openOne(sender):

    print(f"Starting function: {sender.title}")

    subprocess.run(["/usr/bin/open", "-a", "Spotify"])  # waits until calendar exit
    CompletedProcess(args=['/usr/bin/open', '-a', 'Spotify'], returncode=0)
    subprocess.Popen(["/usr/bin/open", "-a", "Spotify"]) # returns immediately


def openTwo(sender):

    print(f"Starting function: {sender.title}")

    subprocess.run(["/usr/bin/open", "-a", "Slack"])  # waits until (SPECIFIC APP) exit
    CompletedProcess(args=['/usr/bin/open', '-a', 'Slack'], returncode=0)
    subprocess.Popen(["/usr/bin/open", "-a", "Slack"]) # returns immediately

app = rumps.App('🚀')
app.menu = [
rumps.MenuItem('Open Spotify', callback=openOne),
rumps.MenuItem('Open Slack', callback=openTwo),
]

app.run()