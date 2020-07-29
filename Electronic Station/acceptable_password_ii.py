#!/usr/bin/env checkio --domain=py run acceptable-password-ii

# In this mission you need to create a password verification function.
# 
# Those are the verification conditions:
# 
# the length should be bigger than 6;should contain at least one digit.Input:A string.
# 
# Output:A bool.
# 
# 
# END_DESC

# Taken from mission Acceptable Password I
def is_acceptable_password(password: str) -> bool:
    # your code here
    c = []
    c = list(password)
    if len(c) > 6:
        for i in range(len(c)):
            if c[i] >= u'\u0030' and c[i] <= u'\u0039':
                return True
    return False
    


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")