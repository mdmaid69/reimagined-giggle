import random
def roll_die():
        return random.randint(1, 6)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)