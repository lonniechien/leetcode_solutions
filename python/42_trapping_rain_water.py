class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        global_max = 0
        for i in range(n):
            if height[i] >= global_max:
                global_max = height[i]
                global_max_index = i
        water = 0
        local_max = 0
        for i in range(global_max_index):
            if height[i] > local_max:
                local_max = height[i]
            else:
                water += (local_max - height[i])
        local_max = 0
        for i in range(n-1, global_max_index, -1):
            if height[i] > local_max:
                local_max = height[i]
            else:
                water += (local_max - height[i])
        return water
