q = input("Enter numbers: ")

# Convert the input string to a tuple of integers
n = tuple(map(int, q.split(',')))

def find_second_largest(numbers):
    u = set(numbers)
    u.remove(max(u))
    return max(u)

second_largest = find_second_largest(n)

print("The second largest number is:", second_largest)
