import math, random

class ReverseThreshold:
    def __init__(self, threshold):
        self.hunted = 0
        self.slacked = 0
        self.threshold = threshold

    def hunt_choices(self, round_number, current_food, current_reputation, m,
                     player_reputations):
        if len(player_reputations) == 1:
            return ['s']
        hunt_decisions = []
        if (round_number < 10):
            hunt_decisions = ['h' for player in player_reputations]
        n = len(player_reputations)
        timesToHunt = min(int(math.ceil(self.threshold * (self.hunted + self.slacked + n) - self.hunted)), n)
        for i in range(timesToHunt):
            hunt_decisions.append('h')
            self.hunted += 1
        for i in range(n - timesToHunt):
            hunt_decisions.append('s')
            self.slacked += 1
        hunt_decisions = self.shuffle(hunt_decisions)
        return hunt_decisions

    def hunt_outcomes(self, food_earnings):
        pass

    def round_end(self, award, m, number_hunters):
        pass

    def shuffle(self, hunt_decisions):
        n = len(hunt_decisions)
        for i in range(n):
            j = random.randint(i, n - 1)
            tmp = hunt_decisions[j]
            hunt_decisions[j] = hunt_decisions[i]
            hunt_decisions[i] = tmp
        return hunt_decisions

    def printInfo(self):
        print "ReverseThreshold with threshold " + str(self.threshold)
        
        
