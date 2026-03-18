class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        brackets = [""]*(2*n)
        result = []
        def solve(idx,total,brackets):
            if idx>=len(brackets):
                if total == 0 :
                    result.append("".join(brackets))
                return 
            if total>len(brackets)//2:
                return 
            elif total<0:
                return 
            brackets[idx] = "("
            sum = total+1
            solve(idx+1,sum,brackets)
            brackets[idx]=")"
            sum = total - 1
            solve(idx+1,sum,brackets)
        solve(0,0,brackets)
        return result
