# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
# For example (Input -> Output):
# summation(2) -> 3 (1 + 2)
# summation(8) -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

def summation(n):
    if n <= 1:
        return n
    else:
        return n + summation(n-1)
    
print(summation(10))


def summation(n):
    sum = 0

    for i in range(1, n + 1):
        sum += n
    return sum
print(summation(10))