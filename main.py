import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)