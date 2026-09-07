class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - position[i]) / speed[i] for i in range(len(position))]
        pairs = sorted(zip(position, time), key = lambda x: x[0])
        # a car joins another's fleet if it gets there time and position are lower
        fleets = [pairs[0][1]]
        for i in range(1, len(position)):
            limit = pairs[i][1]
            while fleets and limit >= fleets[-1]:
                fleets.pop()
            fleets.append(limit)
        return len(fleets)
                