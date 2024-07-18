import random

class Simulation:
    def __init__(self, doornum):
        self.numdoors = doornum
        
    def set_random_doors(self):
        doors = ['zonk'] * self.numdoors
        index = random.randint(0, self.numdoors - 1)
        doors[index] = 'car'
        return doors
    
    def choose_doors(self):
        doors = self.set_random_doors()
        contestant_choice = random.choice(doors)
        doors.remove(contestant_choice)
        doors.remove('zonk')
        alt_door = random.choice(doors)
        return contestant_choice, alt_door
    
    
    def play_game(self, switch=False, iterations=1):
        if iterations < 1:
            raise ValueError("Iterations must be a positive integer.")
        wins = 0
        for i in range(iterations):
            contestant_door, alternate_door = self.choose_doors()
            if (contestant_door == 'car' and not switch) or (alternate_door == "car" and switch): 
                wins = wins +1
        try:
            win_percentage = wins / iterations
        except ZeroDivisionError:
            win_percentage = 0
        return win_percentage   

if __name__ == "main": 
    simulate = Simulation(doornum = 3)
    win_percent = simulate.play_game(switch = True, iterations = 1000)
    print(f"Win percentage : {win_percent}")
        