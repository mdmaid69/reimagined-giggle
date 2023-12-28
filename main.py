import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import sys
def exit_program():
        sys.exit()