class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = list()
        n = target[-1] + 1
        for i in range(1, n):
            if i == target[0]:
                result.append("Push")
                target.pop(0)
            else:
                result.append("Push")
                result.append("Pop")
        return(result)
