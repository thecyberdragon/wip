from datetime import datetime
import matplotlib.pyplot as plt

# Add in option to display the lap time each lap, as well as lap time difference

def stamp():
    return datetime.now()

class CyberTimer():
    def __init__(self, name = None, verbose = False):
        self.name = name        
        self.lap_times = []
        self.checkpoints = {}     
        self.end = None   
        self.verbose = verbose
    
    def start(self):
        self.start = stamp()
        self.lap_times = [self.start]    
        if self.verbose == True:
            print(f"Timer started: {self.start}")
                                     
    def stop(self):
        now = stamp()
        self.end = now 
        self.span = self.end - self.start  
        
        if self.verbose == True:
            print(f"Timer stopped: {now}")
            
    def mark_lap(self):
        if self.end is not None:
            print("Cannot mark a checkpoint when the timer is completed.")
            return
        now = stamp()
        self.lap_times.append(now)  
        
        if self.verbose == True:
            print(f"Mark lap {len(self.lap_times) - 1}, {now}")
        
    def mark_checkpoint(self, name = None):
        if self.end is not None:
            print("Cannot mark a checkpoint when the timer is completed.")
            return

        current_lap = self.lap_times[-1]
        now = stamp()
        
        if current_lap not in self.checkpoints:
            self.checkpoints[current_lap] = {now:name}
        else:
            self.checkpoints[current_lap][now] = name
        
        if self.verbose == True:
            print(f"Mark checkpoint: {len(self.checkpoints[current_lap])}, {now}, Name: {name}")
        
    def print_timer(self, laps = True, checkpoints = True):
        
        if self.end is None:
            print("Timer has not been completed yet.")
            return
        
        print(f"Timer name: {self.name}")
        print(f"Start: {self.start}")
        print(f"End: {self.end}")
        print(f"Time span (seconds): {self.span.total_seconds()}")
        
        if laps == True:
            if checkpoints == True:
                print("Printing laps and checkpoints")
            else:
                print("Printing laps")
            for idx, dtime in enumerate(self.lap_times):
                if idx == 0:
                    print(f"Start: {dtime}")
                else:                   
                    print(f"Lap: {dtime}")
                if checkpoints == True:
                    for checkpoint, checkpoint_name in self.checkpoints[dtime].items():
                        print(f"   Checkpoint name: {checkpoint_name} -> {checkpoint}")
            
    def return_laps(self):                  
        return self.lap_times                 
        
    def return_laps_incremental(self):
        incremental_times = []
        for time in self.lap_times:                
            seconds = (time - self.start).total_seconds()
            incremental_times.append(seconds)
        return incremental_times                        
                        
    def return_lap_changes(self):
        if len(self.lap_times) > 2:            
            
            lap_list = []
            
            for index in range(len(self.lap_times)-1):
                next_index = index + 1
                seconds = (self.lap_times[index] - self.lap_times[next_index]).total_seconds()
                lap_list.append(seconds)
                
            lap_changes = [0]
            for index, time in enumerate(lap_list):
                if index == 0:
                    continue
                lap_changes.append(time - lap_list[index - 1])
                
            return lap_changes                                   
            
        else:
            print("Not enough laps to calculate lap changes")
        
    def return_checkpoint_changes_over_laps(self):
        if len(self.checkpoints) < 2:
            print("Must have at least one checkpoint over two laps to calculate changes")
            return
        
        checkpoint_lengths = None
        for checkpoint_values in self.checkpoints.values():
            length = len(checkpoint_values)
            if checkpoint_lengths is None:
                checkpoint_lengths = length
            else:
                if checkpoint_lengths != length:
                    print("Cannot calculate checkpoint variation when checkpoint dictionaries are not the same length")
                    return 
                               
        index = 0        
        while index != checkpoint_lengths:
            values = []
            for checkpoint_dict in self.checkpoints.values():
                checkpoint_list = list(checkpoint_dict.values())
                values.append(checkpoint_list[index])
            # here
        
        
def gen_graph_indexes(number:int):
    return list(range(1, number + 1))
    
def visualise_data(x:list, y:list, title:str, xlabel:str, ylabel:str):
    plt.scatter(x=x, y=y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
        

        