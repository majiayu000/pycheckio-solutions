#!/usr/bin/env checkio --domain=py run stressful-subject

# 
# END_DESC

import re
def is_stressful(subj):
    """
        recognize stressful subject
    """
   
    stress = subj.isupper() or subj[-3:] == '!!!'
    subj = subj.lower()
    for i in ['help', 'asap', 'urgent']:
        if i in subj:
            stress = True        
    if not stress:
        subj = subj.split(' ')
        for i in subj:
            letters = set()
            for letter in i:
                if letter.isalpha():
                    letters.add(letter)
            if letters in [{'h', 'e', 'l', 'p'}, {'a', 's', 'p'}, {'u', 'r', 'g', 'e', 'n', 't'}]:
                stress = True
    return stress




if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')