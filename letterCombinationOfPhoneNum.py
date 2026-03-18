class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        subset = []
        result = []
        def solve(idx,subset):
            if idx >= len(digits):
                result.append("".join(subset))
                return
            for ch in char_map[digits[idx]]:
                subset.append(ch)
                solve(idx+1,subset)
                subset.pop()
        solve(0,[])
        return result
