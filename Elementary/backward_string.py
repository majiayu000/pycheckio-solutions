#!/usr/bin/env checkio --domain=py run backward-string

# You should return a given string in reverse order.
# 
# Input:A string.
# 
# Output:A string.
# 
# 
# END_DESC

def backward_string(val: str) -> str:
    # your code here
    c = list(val)
    for i in range(len(c)//2):
        tmp = c[i]
        c[i] = c[-i-1]
        c[-i-1] = tmp
    return "".join(c)


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")