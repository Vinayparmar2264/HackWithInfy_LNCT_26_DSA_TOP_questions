class Solution:
    def trap(self, height: List[int]) -> int:
        left_max  = []
        l_max = height[0]
        for i in range(len(height)):
            left_max.append(l_max)
            if height[i]>l_max:
                l_max = height[i]
        
        right_max = []
        r_max = height[-1]
        for i in range(len(height)-1,-1,-1):
            right_max.append(r_max)
            if height[i]>r_max:
                r_max = height[i]

        j= len(right_max)-1
        total_water_trapped = 0
        for i in range(len(height)):
            temp =  min(left_max[i],right_max[j])-height[i]
            if temp>0:
                total_water_trapped += temp
            j-=1
        return total_water_trapped
