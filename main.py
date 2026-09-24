# Python 3.11
from typing import Generator

def fibonacci(n: int) -> Generator[int, None, None]:
    """Yield the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# Run
fibs = list(fibonacci(12))
print(f"Fibonacci (12 terms): {fibs}")
print(f"Sum: {sum(fibs)}")

primes = [n for n in range(2, 50) if is_prime(n)]
print(f"Primes < 50: {primes}")
