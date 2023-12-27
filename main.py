import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"