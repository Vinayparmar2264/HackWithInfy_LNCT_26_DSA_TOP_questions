class Solution:
    def checkValidString(self, s: str) -> bool:
        stack  =  []
        l_forgive = 0
        r_forgive = 0
        forgive =0
        for i in range(len(s)):
            if s[i] == "*" and stack:
                r_forgive += 2
                stack.pop()

            elif not stack and s[i] == "*":
                l_forgive+=1

            elif s[i] == "(":
                stack.append(s[i])

            elif s[i] == ")" :
                if not stack and r_forgive<=0 and l_forgive<=0:
                    return False
                elif stack:
                    stack.pop()
                elif r_forgive>0:
                    r_forgive-=1
                elif l_forgive>0:
                    l_forgive-=1
        
        
        if not stack:
            return True
        return False

        
