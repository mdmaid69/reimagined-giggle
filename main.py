sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)