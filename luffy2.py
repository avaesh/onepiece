import os
import time
import random

# ASCII Art Frames
Luffy_Gatling = [
    """
    ( o_o)  👊===👊
     /|_|\\  ==👊==
    """,
    """
    ( o_o)  =👊==👊=
     /|_|\\  👊====👊
    """,
    """
    ( o_o)  👊👊👊👊
     /|_|\\  👊👊👊👊
    """
]

Finisher = """
      _____________
     /             \\
    /   GEAR THIRD  \\
   (      👊👊👊      )
    \\_____________/
         ||
       ( o_o)
        /|_|\\
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- THE ANIMATION ---
clear()
print("\n\n   Luffy: GOMU GOMU NO...")
time.sleep(1.5)

# 1. Gatling Phase (Fast and Chaotic)
for _ in range(30):
    clear()
    print(random.choice(Luffy_Gatling))
    time.sleep(0.05)

# 2. The Impact Frame (White Flash)
clear()
print("\n" * 5 + "      💥 IMPACT!! 💥" + "\n" * 5)
time.sleep(0.2)

# 3. The Finisher (Giant Fist)
clear()
print(Finisher)
print("\n   GIGANT PISTOL!!!")
time.sleep(2)

print("\n\n   K.O. 🍖")