def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)