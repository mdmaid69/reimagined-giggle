import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread