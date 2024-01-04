import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)