import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def calculate_density(mass, volume):
        return mass / volume