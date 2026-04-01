import os
import time

# The "frames" of our animation (Luffy's stretching arm)
frames = [
    "Luffy: ( o_o)=--",
    "Luffy: ( o_o)===---",
    "Luffy: ( o_o)=====-----",
    "Luffy: ( o_o)=======-------",
    "Luffy: ( o_o)=====-----",
    "Luffy: ( o_o)===---"
]

while True:
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear') # Clears the screen
        print("\n\n\n")
        print(frame)
        time.sleep(0.1) # Controls the speed