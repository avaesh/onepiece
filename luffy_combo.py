import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Luffy: Animation Combo Sequence")
clock = pygame.time.Clock()

# 1. Load Sheet
try:
    sheet = pygame.image.load("luffy_sheet.png").convert_alpha()
    sheet.set_colorkey((0, 0, 0))
except:
    print("Error: check filename!")
    pygame.quit()
    sys.exit()

# 2. SEQUENCE DATA
# We put your moves in a list so we can loop through them in order
SEQUENCE = [
    {
        "name": "PUNCH",
        "y": 112,
        "h": 66,
        "cuts": [0, 38, 71, 110, 152, 193, 232, 275, 320, 365, 408, 452]
    },
    {
        "name": "SPECIAL",
        "y": 825,
        "h": 69,
        "cuts": [0, 34, 75, 120, 177, 236, 307, 418, 496, 565, 601, 640]
    }
]

current_move_idx = 0
current_frame_idx = 0
SCALE = 4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))

    # --- GET CURRENT ANIMATION DATA ---
    move = SEQUENCE[current_move_idx]
    cuts = move["cuts"]
    
    # Calculate crop area
    x_src = cuts[current_frame_idx]
    w_src = cuts[current_frame_idx + 1] - x_src
    y_src = move["y"]
    h_src = move["h"]

    # Extract, Scale, and Draw
    luffy_sprite = sheet.subsurface((x_src, y_src, w_src, h_src))
    luffy_big = pygame.transform.scale(luffy_sprite, (w_src * SCALE, h_src * SCALE))
    
    # Always draw in the center of the screen
    screen.blit(luffy_big, (WIDTH // 2 - (w_src * SCALE // 2), 200))

    # --- THE COMBO LOGIC ---
    current_frame_idx += 1
    
    # If we reach the end of the current move's cuts...
    if current_frame_idx >= len(cuts) - 1:
        current_frame_idx = 0 # Reset frame to start
        current_move_idx += 1 # Move to the next animation in the sequence
        
        # If we finished the last move in the SEQUENCE list, loop back to the first move
        if current_move_idx >= len(SEQUENCE):
            current_move_idx = 0

    pygame.display.flip()
    clock.tick(10) # Adjust speed of the combo here