import time
def measure_execution_time(func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)