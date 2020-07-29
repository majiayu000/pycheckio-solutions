#!/usr/bin/env checkio --domain=py run end-zeros

# Try to find out how many zeros a given number has at the end.
# 
# Input:A positive Int
# 
# Output:An Int.
# 
# 
# END_DESC

def end_zeros(num: int) -> int:
    # your code here
    c=str(num)
    h=tuple(c)
    l=len(c)
    if l == 1 :
        if h[0] == '0':
            return 1
        else:
            return 0
    else:
      if h[-1] != '0':
        sum = 0
      else :
        sum = 1
       
        for i  in range(2,l):
            if h[-i] == '0':
                sum = sum +1
            else:
                break
            
    return sum


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(100))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")