import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))