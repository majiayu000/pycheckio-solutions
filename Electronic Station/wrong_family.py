#!/usr/bin/env checkio --domain=py run wrong-family

# Michael always knew that there was something wrong with his family. Many strangers were introduced to him as part of it.
# 
# Michael should figure this out. He's spent almost a month parsing the family archives. He has all father-son connections of his entire family collected in one place.
# 
# With all that data Michael can easily understand who the strangers are. Or maybe the only stranger in this family is Michael? Let's see.
# 
# You have a list of family ties between father and son. Each element on this list has two elements. The first is the father's name, the second is the son's name. All names in the family are unique. Check if the family tree is correct. There are no strangers in the family tree. All connections in the family are natural.
# 
# Input:list of lists. Each element has two strings. The list has at least one element
# 
# Output:bool. Is the family tree correct.
# 
# 
# 
# 
# Precondition:1<= len(tree)<100
# 
# 
# END_DESC

def is_family(tree):
    a = tree
    a0 = []
    a1 = []
    c = []
    r = True
    for i in a:
        a0.append(i[0])
        a1.append(i[1])
        if len(a) > 1:
    		for j in a:
    			if j[1] == i[0] and j[0] == i[1]:
    				r = False
    b0 = list(set(a0))
    b1 = list(set(a1))
    if len(b1) != len(a1): #有人重复当了两个人的儿子
    	r = False    
    for i in b0:
    	if i not in b1:
    		c.append(i)   #找出来数的顶端
    if len(c) != 1:      #如果树的顶端不只一个，是不对的
    	r = False
    elif c[0] in b1:    #如果数的顶端又在数的分支是不对的
    	r = False
    return r

       
    for x in s:
        if s.count(x[1]) > 1:
            return False
    return True


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father to your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father to your brother?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    print("Looks like you know everything. It is time for 'Check'!")