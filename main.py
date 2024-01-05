import sys
def exit_program():
        sys.exit()
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)