import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def calculate_speed(distance, time):
        return distance / time