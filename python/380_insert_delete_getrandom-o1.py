class RandomizedSet:

    def __init__(self):
        self.vals = dict()
        self.randoms = list()
        self.curr = 0

    def insert(self, val: int) -> bool:
        if val in self.vals:
            return False
        else:
            self.vals[val] = self.curr
            self.randoms.append(val)
            self.curr += 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.vals:
            i = self.vals[val]
            self.vals[self.randoms[-1]] = i
            self.randoms[i], self.randoms[-1] = self.randoms[-1], self.randoms[i]
            self.vals.pop(val)
            self.randoms.pop(-1)
            self.curr -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.randoms)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
