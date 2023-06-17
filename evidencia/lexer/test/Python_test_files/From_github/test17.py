# Loop to print numbers from 1 to 10
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# Loop to calculate the sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print("Sum of numbers from 1 to 100:", total)

# Loop to print the multiplication table of a number
num = 5
print("Multiplication table of", num, ":")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Loop to print even numbers from 1 to 20
print("Even numbers from 1 to 20:")
for i in range(2, 21, 2):
    print(i)

# Loop to find the factorial of a number
num = 6
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, ":", factorial)

# Loop to check if a number is prime
num = 17
is_prime = True
for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        is_prime = False
        break
print(num, "is prime:", is_prime)

# Loop to generate a Fibonacci sequence
num_terms = 10
fibonacci_seq = [0, 1]
for i in range(2, num_terms):
    next_term = fibonacci_seq[i - 1] + fibonacci_seq[i - 2]
    fibonacci_seq.append(next_term)
print("Fibonacci sequence:", fibonacci_seq)

# Loop to iterate over a list and perform operations
numbers = [2, 4, 6, 8, 10]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)
print("Squared numbers:", squared_numbers)

# Loop to iterate over a string and count the occurrences of a character
word = "banana"
char = "a"
count = 0
for c in word:
    if c == char:
        count += 1
print("Occurrences of", char, "in", word, ":", count)

# Loop to iterate over a dictionary and print key-value pairs
student_grades = {"John": 85, "Emma": 92, "Michael": 78, "Sophia": 90}
print("Student Grades:")
for student, grade in student_grades.items():
    print(student, ":", grade)

# Loop to iterate over a range in reverse order
print("Countdown from 10 to 1:")
for i in range(10, 0, -1):
    print(i)

# Loop to iterate over multiple lists simultaneously
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9]
print("Sum of corresponding elements in three lists:")
for n1, n2, n3 in zip(numbers1, numbers2, numbers3):
    print(n1 + n2 + n3)

# Loop to iterate over a list and skip certain elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Numbers skipping multiples of 3:")
for num in numbers:
    if num % 3 == 0:
        continue
    print(num)

# Loop to iterate over a list and break at a certain condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Numbers until reaching 5:")
for num in numbers:
    print(num)
    if num == 5:
        break
