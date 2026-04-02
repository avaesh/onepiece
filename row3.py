import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Luffy Row 3: Final Form")
clock = pygame.time.Clock()

# 1. Load Sheet
try:
    sheet = pygame.image.load("luffy_sheet.png").convert_alpha()
    sheet.set_colorkey((0, 0, 0)) 
except:
    print("Error: check filename!")
    pygame.quit()
    sys.exit()

# 2. DATA FROM YOUR MEASUREMENTS
# We use your list to calculate (X, Y, WIDTH, HEIGHT) for every frame
CUTS = [0, 38, 71, 110, 152, 193, 232, 275, 320, 365, 408, 452]
Y_START = 112
Y_END = 178
FRAME_H = Y_END - Y_START

# This list comprehension does the math for us!
# It takes (Current Cut) and (Next Cut - Current Cut) to get the width
FRAME_DATA = []
for i in range(len(CUTS) - 1):
    x = CUTS[i]
    w = CUTS[i+1] - x
    FRAME_DATA.append((x, Y_START, w, FRAME_H))

SCALE = 4
current_frame = 0

# 3. Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30)) 

    # Get the precise rectangle for this frame
    x, y, w, h = FRAME_DATA[current_frame]
    crop_rect = (x, y, w, h)
    
    try:
        luffy_sprite = sheet.subsurface(crop_rect)
        luffy_big = pygame.transform.scale(luffy_sprite, (w * SCALE, h * SCALE))
        
        # We center him based on his individual width (w)
        screen.blit(luffy_big, (WIDTH // 2 - (w * SCALE // 2), 250))
    except Exception as e:
        print(f"Error at frame {current_frame}: {e}")
        current_frame = 0

    # Logic: Cycle through the 11 frames
    current_frame = (current_frame + 1) % len(FRAME_DATA)

    pygame.display.flip()
    clock.tick(10) # 10 FPS looks great for GBA sprites