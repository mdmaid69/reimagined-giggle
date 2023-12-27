import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import array
def get_array_item_count(array, item):
        return array.count(item)