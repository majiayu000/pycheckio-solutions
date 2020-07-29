#!/usr/bin/env checkio --domain=py run split-pairs

# Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').
# 
# Input:A string.
# 
# Output:An iterable of strings.
# 
# Precondition:0<=len(str)<=100
# 
# 
# END_DESC

def split_pairs(a):
    # your code here
        # your code here
    l = tuple(a)
    s = len(l)
    c = []
    if len(l) == 0:
        return l
    if len(l) % 2 == 0:
        for i in range(int(len(l) / 2)):
            d =  l[2*i] + l[i * 2  + 1]
            c.append(d)


    else:
         for i in range((len(l) // 2) + 1):
             if i < len(l) // 2:
                 d = l[2*i] + l[2*i + 1]
                 c.append(d)
             if i == len(l) // 2 :
                 d = l[2*i ] + "_"
                 c.append(d)

    return c


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")