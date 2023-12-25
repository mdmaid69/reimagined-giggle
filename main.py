import random
def generate_random_choice(choices):
        return random.choice(choices)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)