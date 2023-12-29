import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import logging
def log_message(message):
        logging.info(message)