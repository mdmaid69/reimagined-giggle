  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)