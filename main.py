import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)