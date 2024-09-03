"""
Description:

Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
"""

def encode(strs):
    s = ''
    for x in strs:
        s += x + "#end"
    return s

def decode(s):
    return s.split("#end")[:-1]

if __name__ == "__main__":
    strs = input()
    strs = strs.split(',')
    encoded = encode(strs)
    decoded = decode(encoded)
    print(decoded)
