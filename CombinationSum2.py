
# method 1 brute force approach
class Solution:
    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #     candidates.sort()
    #     result = set()
    #     def solve(idx,target,subset,total):
    #         if target == total:
    #             # subset.sort()
    #             result.add(tuple(subset[:]))
    #             return
    #         if idx >= len(candidates):
    #             return
    #         if target < total:
    #             return 
    #         sum = total + candidates[idx]
    #         subset.append(candidates[idx])
    #         solve(idx+1,target,subset,sum)

    #         sum = total
    #         subset.pop()
    #         solve(idx+1,target,subset,sum)
        
    #     solve(0,target,[],0)  
    #     result = list(result)
    #     result = [list(i) for i in result]
    #     return result



    # optimal approach 
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        result = []
        def solve(idx,subset,total):
            if  total == 0:
                # subset.sort()
                result.append(subset.copy())
                return

            if total < 0 :
                return 
            
            for i in range(idx,n):
                if i>idx and candidates[i] == candidates[i-1] : 
                    continue

                sum = total - candidates[i]
                subset.append(candidates[i])
                solve(i+1,subset,sum)
                subset.pop()

        total = target
        solve(0,[],total)  
        
        return result
