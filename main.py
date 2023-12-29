import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)