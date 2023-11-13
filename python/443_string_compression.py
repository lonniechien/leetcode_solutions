class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return n
        prev = chars[0]
        count = 1
        j = 0
        chars.append(None)
        for i in range(1,n+1):
            if chars[i] == prev:
                count += 1
            if chars[i] != prev:
                chars[j] = prev
                prev = chars[i]
                j += 1
                print(count,j)
                if count > 1:
                    count = str(count)
                    for num in count:
                        chars[j] = num
                        j += 1
                    count = 1
        return j 
