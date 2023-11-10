class Solution:
    def countPoints(self, rings: str) -> int:
        rods = {str(i):[False,False,False] for i in range(10)}
        colors = {"R":0,"G":1,"B":2}
        goal = [True,True,True]
        completed = set()
        for i in range(0,len(rings),2):
            color = colors[rings[i]]
            rod = rings[i+1]
            rods[rod][color] = True
            if rods[rod] == goal:
                completed.add(rod)
        return len(completed)
