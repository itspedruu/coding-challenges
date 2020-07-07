from random import random

def estimate_pi(n):
    inside = 0
    total = 0

    for _ in range(n):
        x = random()
        y = random()
        distance = x**2 + y**2

        if distance <= 1:
            inside += 1

        total += 1

    return 4 * inside / n

print(estimate_pi(1000000))