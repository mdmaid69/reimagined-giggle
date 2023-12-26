import array
def convert_array_to_unicode(array):
        return array.tounicode()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)