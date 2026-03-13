class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
       
        area =0
        width = [1]*len(heights)
        
        def width_arr():
            next_small_left=[-1]*len(heights)
            stack = []
            for i in range(len(heights)):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    next_small_left[i]=stack[-1]
                stack.append(i)
            

            next_small_right=[len(heights)]*len(heights)
            stack = []
            for i in range(len(heights)-1,-1,-1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack:
                    next_small_right[i]=stack[-1]
                stack.append(i)
                    
            for i in range(len(width)):
                width[i]=(next_small_right[i]-next_small_left[i]-1)

        width_arr()
        for i in range(len(heights)):
            area = max(area, heights[i]*width[i])
        return area
