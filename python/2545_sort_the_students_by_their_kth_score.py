class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score = sorted(score, key=lambda test:0-test[k])
        return score
