#!/bin/python3
#method 1
import math
import os
import random
import re
import sys

#
# Complete the 'virusIndices' function below.
#
# The function accepts following parameters:
#  1. STRING p
#  2. STRING v
#

def z_function(s):
    n = len(s)
    z = [0]*n
    l = r = 0
    
    for i in range(1,n):
        if i <= r:
            z[i] = min(r-i+1, z[i-l])
        
        while i+z[i] < n and s[z[i]] == s[i+z[i]]:
            z[i] += 1
        
        if i+z[i]-1 > r:
            l = i
            r = i+z[i]-1
    
    return z


def virusIndices(p, v):

    n = len(p)
    m = len(v)

    # prefix matches
    s1 = v + "#" + p
    z1 = z_function(s1)

    prefix = [0]*n
    for i in range(n):
        prefix[i] = min(z1[m+1+i], m)

    # suffix matches
    rp = p[::-1]
    rv = v[::-1]

    s2 = rv + "#" + rp
    z2 = z_function(s2)

    suffix = [0]*n
    for i in range(n):
        suffix[n-1-i] = min(z2[m+1+i], m)

    ans = []

    for i in range(n-m+1):

        if prefix[i] + suffix[i+m-1] >= m-1:
            ans.append(i)

    if not ans:
        print("No Match!")
    else:
        print(*ans)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        p = first_multiple_input[0]

        v = first_multiple_input[1]
        virusIndices(p, v)





# method 2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'virusIndices' function below.
#
# The function accepts following parameters:
#  1. STRING p
#  2. STRING v
#
def small_match(w1,w2):
    counter = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            counter+=1
            if counter>1:
                return 0
    return 1

def match(w1,w2):
    length = len(w1)
    if length<10:
        return small_match(w1,w2)
    w11 = w1[:length//2]
    w12 = w1[length//2:]
    w21 = w2[:length//2]
    w22 = w2[length//2:]

    section1 = (w11==w21)
    section2 = (w12 == w22)
    
    if section1 and section2:
        return 1
    elif section1 and not section2:
        return match(w12,w22)
    elif not section1 and section2:
        return match(w11,w21)
    else:
        return 0
        
def virusIndices(p, v):
    res = "" 
    if len(v) > len(p):
        return "No Match!"
    else:
        for i in range(len(p)-len(v)+1):
            temp = p[i:i+len(v)]
            flag = match(temp,v)
            if flag:
                res += str(i) + " "
        if len(res)==0:
            return "No Match!"
        else:
            return res.strip()
            

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        p = first_multiple_input[0]

        v = first_multiple_input[1]

        print(virusIndices(p, v))
