class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        k = min(k, len(arr))
        streak = 0
        winner = None
        while streak < k:
            i = 0
            j = 1
            if arr[i] > arr[j]:
                if arr[i] == winner:
                    streak += 1
                else:
                    streak = 1
                winner = arr[i]
                arr.append(arr[j])
                arr.pop(j)
            else:
                if arr[j] == winner:
                    streak += 1
                else:
                    streak = 1
                winner = arr[j]
                arr.append(arr[i])
                arr.pop(i)
        return winner
