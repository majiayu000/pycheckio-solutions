#!/usr/bin/env checkio --domain=py run sort-by-extension

# You are given a list of files. You need to sort this list by the file extension.     The files with the same extension should be sorted by name.
# 
# Some possible cases:
# 
# Filename cannot be an empty string;Files without the extension should go before the files with one;Filename ".config" has an empty extension and a name ".config";Filename "config." has an empty extension and a name "config.";Filename "table.imp.xls" has an extension "xls" and a name "table.imp";Filename ".imp.xls" has an extension "xls" and a name ".imp".Input:A list of filenames.
# 
# Output:A list of filenames.
# 
# 
# END_DESC

from typing import List

def sort_by_ext(files: List[str]) -> List[str]:
    # your code here
    l=[]
    s=[]
    c=[]
    f=[]
    q=[]
    for i in range(len(files)):
        l.append(files[i].split(".")) 
    for x in l:
        if x[-1] == "" and len(x) <=2 :
            s.append(x)
    s.sort()
    for x in l:
        if len(x) > 2:
            continue
        if x[0] == "" and x[0] != "config":
            q.append(x)
    q.sort()
    for x in l:
        if x[1] != "" and x[0] != "" or (x[0]  == "" and len(x) > 2) :
            c.append(x)
    for m in range(len(c)-1):
         for i in range(len(c)-1):
              if c[i][-1] > c[i+1][-1]:
                 c[i],c[i+1] = c[i+1],c[i]
              if c[i][-1] == c[i+1][-1]:
                  if c[i][0] > c[i+1][0]:
                      c[i],c[i+1] = c[i+1],c[i]
    
            
        
    
    for x in s:
        f.append(".".join(x))
    for x in q:
        f.append(".".join(x))
    for x in c:
        f.append(".".join(x))
    return f


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")