import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
text = "Hello, world!"
print("Words:", len(text.split()))