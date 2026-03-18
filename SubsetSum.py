class Solution:
	def subsetSums(self, arr):
		# code here
		def solve(idx,total):
		    if idx>=len(arr):
		        result.append(total)
		        return 
		    
		    sum = total + arr[idx]
		    solve(idx+1,sum)
		    sum = total
		    solve(idx+1,sum)
		    
		result = []
        solve(0,0)
        # result = set(result)
		return result  
