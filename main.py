import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def calculate_volume(length, width, height):
        return length * width * height