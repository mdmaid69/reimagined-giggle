import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)