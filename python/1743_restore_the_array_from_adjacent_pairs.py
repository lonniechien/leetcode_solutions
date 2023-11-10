class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neighbors = dict()
        for pair in adjacentPairs:
            neighbors[pair[0]] = list()
            neighbors[pair[1]] = list()
        ends = {num:0 for num in neighbors}
        for pair in adjacentPairs:
            for i in [0,1]:
                neighbors[pair[i]].append(pair[i-1])
                ends[pair[i]] += 1
                if ends[pair[i]] > 1:
                    ends.pop(pair[i])
        ends = iter(ends)
        val = next(ends)
        curr = neighbors[val][0]
        result = [val,curr]
        end = next(ends)
        while curr is not end:
            pair = neighbors[curr]
            if pair[0] == val:
                result.append(pair[1])
            else:
                result.append(pair[0])
            val = curr
            curr = result[-1]
        return result
