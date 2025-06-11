def fibonacci(n):
    """Return a list containing the Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
    print(f"Fibonacci sequence ({num_terms} terms):", fibonacci(num_terms))
