# Function to generate Fibonacci series using recursion
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        # Recursively build the list
        fib_list = fibonacci_recursive(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

# Input: Number of terms
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))

# Generating and printing the series
fibonacci_series = fibonacci_recursive(num_terms)
print(f"Fibonacci series with {num_terms} terms: {fibonacci_series}")
