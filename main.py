import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)