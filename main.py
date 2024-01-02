import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")