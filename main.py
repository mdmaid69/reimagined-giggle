import logging
def log_message(message):
        logging.info(message)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)