class Solution:
    # s.c. = O(2n)
    # def candy(self, ratings: List[int]) -> int:
    #     n = len(ratings)
    #     l2r = [1]*n
    #     r2l = [1]*n

    #     for i in range(1,n):
    #         if ratings[i]>ratings[i-1]:
    #             l2r[i]= max(l2r[i],l2r[i-1]+1)

    #     for i in range(n-2,-1,-1):
    #         if ratings[i]>ratings[i+1]:
    #             r2l[i]= max(r2l[i],r2l[i+1]+1)
                
    #     result = 0
    #     for i in range(n):
    #         result += max(l2r[i],r2l[i])
    #     return result


# s.c. = O(n)
    def candy(self, ratings: List[int]) -> int:
            n = len(ratings)
            count = [1]*n

            for i in range(1,n):
                if ratings[i]>ratings[i-1]:
                    count[i]= max(count[i],count[i-1]+1)

            for i in range(n-2,-1,-1):
                if ratings[i]>ratings[i+1]:
                    count[i]= max(count[i],count[i+1]+1)
                    
            result = 0
            for i in range(n):
                result += count[i]
            return result
