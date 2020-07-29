#!/usr/bin/env checkio --domain=py run acceptable-password-vi

# In this mission you need to create a password verification function.
# 
# Those are the verification conditions:
# 
# the length should be bigger than 6;should contain at least one digit, but it cannot consist of just digits;having numbers or containing just numbers does not apply to the password longer than 9.a string should not contain the word "password" in any case;should contain 3 different letters (or digits) even if it is longer than 10Input:A string.
# 
# Output:A bool.
# 
# 
# END_DESC

# Taken from mission Acceptable Password V

# Taken from mission Acceptable Password IV

# Taken from mission Acceptable Password III

# Taken from mission Acceptable Password II

# Taken from mission Acceptable Password I
def is_acceptable_password(password: str) -> bool:
    # your code here
    c = []
    c = list(password)
    flag = 0
    s = set(password)
    if len(s) <3:
        return False
    if "password" in password:
        return False
    if "PASSWORD" in password:
        return False
    if len(c) > 9:
        return True
    if len(c) > 6:
        for i in range(len(c)):
            if c[i] >= u'\u0030' and c[i] <= u'\u0039':
                flag += 1
                break
        for i in range(len(c)):
            if (c[i] >= u'\u0041' and c[i] <= u'\u005a') or (c[i] >= u'\u0061' and c[i] <= u'\u007a'):
                flag += 1
                break
    
    return flag == 2
    


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