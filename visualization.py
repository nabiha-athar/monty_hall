from monty_hall import Simulation
import pandas as pd
import seaborn as sb

class Plot:
    
    def __init__(self, doors = 3, iterations = 200):
        self.doors = doors
        self. iterations = iterations
        self.sequences = []
        
        for i in range(1, iterations + 1):
            if i % 2 == 0: 
                simulate = Simulation(doornum = self.doors)
                percent = simulate.play_game(switch = True, iterations = i)
                switch = "True"
            else: 
                simulate = Simulation(doornum = self.doors)
                percent + simulate.play_game(switch = False, iterations = i)
                self.sequences.append ({"iterations": i, "percentage": percent, "doors": self.doors, "switched": "False"})
                
        self.make_plot()
        
    def make_plot(self):
        df = pd.DataFrame(self.sequence)
        plot = sb.lmplot(x="iterations", y="percentage", data=df, hue="switched")
        plot.savefig(f"{self.doors}doors_{self.iterations}iterations.png")
        
        
if __name__ == "main":
    plot = Plot(doors = 5, iterations = 100)    