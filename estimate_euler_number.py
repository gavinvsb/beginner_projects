"""
Estimate the Euler Number, e.
"""

import math

def euler(n):
    t_sum = 0
    for i in range(n):
        term = 1/math.factorial(i)
        t_sum = t_sum + term
    
    return t_sum

# Reading number of terms to be considered in series
terms = int(input("Enter number of terms: "))

# Function call
e = euler(terms)

# Displaying result
print(f"e = {e}")
