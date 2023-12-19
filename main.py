import shutil
def delete_directory(path):
        shutil.rmtree(path)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))