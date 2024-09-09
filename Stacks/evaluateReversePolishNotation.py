"""
Description:

You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

    The operands may be integers or the results of other operations.
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward zero.


Example

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5

"""

import math

def evalPRN(tokens: list[str]) -> int:
    if len(tokens) == 1: return int(tokens[0])
    s = list()
    operands = set(['+', '-', '*', '/'])
    for i in tokens:
        if i not in operands:
            s.append(i)
        else:
            rhs = int(s.pop())
            lhs = int(s.pop())
            if i == '-':
                res = lhs - rhs
            elif i == '+':
                res = lhs + rhs
            elif i == '*':
                res = lhs * rhs
            else:
                res = math.trunc(lhs / rhs)
            s.append(str(res))
    return int(s.pop())

if __name__ == "__main__":
    tokens = input()
    tokens = list(tokens)
    print(tokens)
    result = evalPRN(tokens)
    print(result)