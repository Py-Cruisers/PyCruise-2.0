import rumps
import subprocess
from subprocess import CompletedProcess

app = rumps.App('🚀')

def openFunction(sender):
    print(f"Starting function: {sender.title}")

    subprocess.run(["/usr/bin/open", "-a", "Slack"])  # waits until calendar exit
    CompletedProcess(args=['/usr/bin/open', '-a', 'Slack'], returncode=0)
    subprocess.Popen(["/usr/bin/open", "-a", "Slack"]) # returns immediately



app.menu = [rumps.MenuItem("Open",callback=openFunction)]

app.run()