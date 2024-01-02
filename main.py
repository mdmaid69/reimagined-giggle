import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)