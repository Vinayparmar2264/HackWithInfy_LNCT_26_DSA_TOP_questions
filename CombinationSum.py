class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        comb = []
        result = []
        def solve(idx,target,comb):
            # if idx>=len(candidates):
            if  target == 0 : 
                    result.append(comb.copy())
                    return 
            if idx>=len(candidates):
                return
            if target < 0:
                return 

            comb.append(candidates[idx])
            target -= candidates[idx]
            solve(idx,target,comb)

            comb.pop()
            target += candidates[idx]
            solve(idx+1,target,comb)
        
        solve(0,target,comb)
        return result
