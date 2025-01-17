"""
Interview question

Write a function according to the specifications below.
1. Function: generate_combos(intList, target)
2. intList: a list of distinct integers of any length and will contain only positive and/or negative integers
3. target: a single integer
4. Output: A list of strings containing all the combinations of intList that can yield "target" while only using addition, subtraction, 
multiplication, or division – do NOT use parenthesis () when printing the output.
5. Operators may be used more than once, but numbers in intList may not be used more than once.

For example, if L1 = [2,3,4,5] and T = 6, output should be:
2*3
2+4
5+3-2
3*4/2
2*5-4
5+4-3, etc.

"""

# Using Python
from itertools import permutations, combinations_with_replacement

def generate_combos(l1: list, t: int):
    """Returns a list of all the combinations of L1 that can yield T only using plus [+], minus [-],
       multiply [*], divide [/]. Do NOT use parenthesis ()."""
    l1 = list(set([str(i) for i in l1])) # confirm unique list
    operators = ["+","-","*","/"]
    seen_values = set()
    for num in range(1, len(l1) + 1):
        for values in permutations(l1, num):
            for operCombo in combinations_with_replacement(operators, num - 1):
                for oper in permutations(operCombo, num - 1):
                    formula = "".join(o + v for o, v in zip([""] + list(oper), values))
                    if formula not in seen_values and eval(formula) == t:
                        print(formula)
                        seen_values.add(formula)

generate_combos([2,3,4,5], 6)
