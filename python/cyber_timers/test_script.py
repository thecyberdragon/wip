import cyber_timers
import time
import random

def random_wait():
    time.sleep(random.randint(1,5))

laps = 6
checkpoints = 5

timer = cyber_timers.CyberTimer("Test timer", True)
timer.start()

random_wait()
for checkpoint in range(checkpoints):
        random_wait()
        timer.mark_checkpoint()

random_wait()
for lap in range(laps):
    random_wait()
    timer.mark_lap()
    for checkpoint in range(checkpoints):
        random_wait()
        timer.mark_checkpoint()
        
random_wait()

timer.stop()

print("\n")

timer.print_timer()

x = timer.return_lap_changes()
y = cyber_timers.gen_graph_indexes(6)
cyber_timers.visualise_data(y, x , "test", "iteration", "difference")

print("Lap changes: ")
print(timer.return_lap_changes())

print("Laps as is")
print(timer.return_laps())
print("")

print("Laps incremental")
print(timer.return_laps_incremental())
print("")



