# Q19 and Q20 Combined

def financial_sum(n):
    if n <= 1:
        return 1
    return financial_sum(n // 2) + n

def authentication(n):
    if n <= 1:
        return 1
    return authentication(n // 2) + 1

n = int(input("Enter the value of n: "))

print("\n----- Q19 -----")
print("Financial Summation Result =", financial_sum(n))
print("Time Complexity = Θ(n)")

print("\n----- Q20 -----")
print("Authentication Levels =", authentication(n))
print("Time Complexity = Θ(log n)")