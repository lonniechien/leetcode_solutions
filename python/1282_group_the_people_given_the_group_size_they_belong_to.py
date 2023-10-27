class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        groups = {size:list() for size in groupSizes}
        ans = list()
        for i,size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                ans.append(groups[size])
                groups[size] = list()
        return ans
