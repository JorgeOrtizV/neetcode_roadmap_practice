""" 
Description:

ou are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

Example:

Input: s = "[]"

Output: true

Input: s = "([{}])"

Output: true

Input: s = "[(])"

Output: false


"""

def isValid(s: str) -> bool:
    # implementing Stack as a list
    stack = list()
    #opening = set('(', '{', '[')
    closing = set([')', '}', ']'])
    for c in s:
        if c not in closing:
            stack.append(c)
        else:
            if len(stack) == 0: return False # We wont be able to close the stack
            o = stack.pop()
            if o == '(' and c == ')' or  o == '{' and c == '}' or  o == '[' and c == ']':
                continue
            else:
                return False
    if len(stack) > 0:
        return False
    return True




if __name__ == "__main__":
    s = input()
    result = isValid(s)
    print(result)