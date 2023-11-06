class SeatManager:

    def __init__(self, n: int):
        self.unreserved = set()
        self.nextSeat = 0

    def reserve(self) -> int:
        if self.unreserved:
            smallest = min(self.unreserved)
            self.unreserved.remove(smallest)
            return smallest
        else:
            self.nextSeat += 1
            return self.nextSeat

    def unreserve(self, seatNumber: int) -> None:
        self.unreserved.add(seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
