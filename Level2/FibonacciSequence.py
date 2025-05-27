"""Write a Python function that generates the
Fibonacci sequence up to a given number of
terms. The function should take an integer
input from the user and display the
Fibonacci sequence up to that number of
terms."""

def fibonacci_sequence(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_value)
    
    return fib_sequence

def main():
    try:
        terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
        result = fibonacci_sequence(terms)
        print(f"Fibonacci sequence up to {terms} terms: {result}")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        
if __name__ == "__main__":
    main()