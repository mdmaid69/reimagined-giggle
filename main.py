  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))