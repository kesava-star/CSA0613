# Recursive Financial Summation Engine
# Time Complexity: O(n)

def financial_sum(n):
    if n <= 1:
        return 1
    return financial_sum(n // 2) + n

n = int(input("Enter the value of n: "))

result = financial_sum(n)

print("Result =", result)
print("Time Complexity = Θ(n)")