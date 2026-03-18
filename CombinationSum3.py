class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def solve(last,total,subset):
            if total == n and len(subset) == k :
                result.append(subset.copy())
            if total>n or len(subset)>k:
                return
            for i in range(last,10):
                sum = total + i
                subset.append(i)
                solve(i+1,sum,subset)
                sum = total
                subset.pop()
            
        result = []
        solve(1,0,[])
        return result
