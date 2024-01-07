numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)