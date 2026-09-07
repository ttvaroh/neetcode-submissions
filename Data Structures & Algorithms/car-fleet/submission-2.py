class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - position[i]) / speed[i] for i in range(len(position))]
        pairs = sorted(zip(position, time), reverse=True)
        # a car joins another's fleet if it gets there time and position are lower
        fleets = []
        for p, t in pairs:
            if len(fleets) == 0 or t > fleets[-1]:
                fleets.append(t)
        return len(fleets)
