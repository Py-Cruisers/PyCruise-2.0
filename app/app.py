import rumps
import subprocess

def hello(sender):
    print(f"The button has been pressed: {sender.title}")

app = rumps.App('🚀')

app.menu = [rumps.MenuItem("Open",callback=hello)]

app.run()

# subprocess.run(["/usr/bin/open", "-a", "calendar"])  # waits until calendar exit
# CompletedProcess(args=['/usr/bin/open', '-a', 'calendar'], returncode=0)
# subprocess.Popen(["/usr/bin/open", "-a", "calendar"]) # returns immediately
