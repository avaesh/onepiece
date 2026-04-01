import os
import time
import random

# Gatling frames with "multiple" fists to show speed
frames = [
    "Luffy:  ( o_o)  =👊",
    "Luffy:  ( o_o)  ==👊",
    "Luffy:  ( o_o)  ===👊",
    "Luffy:  ( o_o)  👊= =👊",
    "Luffy:  ( o_o)  =👊 =👊=",
    "Luffy:  ( o_o)  👊===👊",
    "Luffy:  ( o_o)  ==👊==👊",
    "Luffy:  ( o_o)  👊=👊=👊"
]

print("GOMU GOMU NO...!!!!")
time.sleep(1)

try:
    while True:
        # Pick a random frame to make it look chaotic and fast
        frame = random.choice(frames)
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n\n")
        print(frame)
        
        # Super fast speed (0.03 seconds)
        time.sleep(0.03) 
except KeyboardInterrupt:
    print("\n\nAttack finished! Luffy is hungry. 🍖")