import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)