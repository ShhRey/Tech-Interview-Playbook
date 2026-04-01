# Question: Design an algorithm to encode a list of strings to a string. 
# The encoded string is then sent over the network and is decoded back to the original list of strings.


from typing import List

def encode(strs: List[str]):
    # Des. Output is a str
    res = ""
    # Iterate through the List checking each str
    for s in strs:
        # Encoding with a Delimeter
        res += str(len(s)) + "#" + s
    # Returning str
    return res


def decode(s: str):
    res = []
    # Ptr to maintain pos
    i = 0
    # Until i in-bound
    while i < len(s):
        # Ptr to find delimeter
        j = i
        # Inc until we find delimeter
        while str[j] != "#":
            j += 1
        # Calc str len and convert to int
        length = int(s[i:j])
        # Iterate till str len and add to res
        res.append(s[j+1 : j+1+length])
        # Setting i for nxt str
        i = j+1+length
    # Return List
    return res



#  Sample Test Cases
q1 = encode()
q2 = decode()