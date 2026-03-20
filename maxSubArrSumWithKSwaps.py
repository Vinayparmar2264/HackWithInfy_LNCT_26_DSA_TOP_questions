def max_subarray_sum(arr):
    max_sum = float('-inf')
    current  = 0

    for x in arr:
        current = max(x,current+x)
        max_sum = max(max_sum,current)
    return max_sum

def solve(n,k,arr):
    arr.sort()

    for i in range(min(k,n//2)):
        if arr[i] < arr[n-1-i]:
            arr[i],arr[n-1-i] = arr[n-1-i],arr[i]
    return max_subarray_sum(arr)
    

print(solve(3,1,[1,1,-5]))
