import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1000, 600 # Widened the screen for those long-range moves!
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Luffy: High-Action Row")
clock = pygame.time.Clock()

# 1. Load Sheet
try:
    sheet = pygame.image.load("luffy_sheet.png").convert_alpha()
    sheet.set_colorkey((0, 0, 0)) 
except:
    print("Error: check filename!")
    pygame.quit()
    sys.exit()

# 2. DATA FROM YOUR NEW MEASUREMENTS
# Your provided X-coordinates
CUTS = [0, 34, 75, 120, 177, 236, 307, 418, 496, 565, 601, 640]
Y_START = 825
Y_END = 894
FRAME_H = Y_END - Y_START

# Build the frame data list
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

    # Get the precise rectangle for this specific action frame
    x, y, w, h = FRAME_DATA[current_frame]
    crop_rect = (x, y, w, h)
    
    try:
        luffy_sprite = sheet.subsurface(crop_rect)
        luffy_big = pygame.transform.scale(luffy_sprite, (w * SCALE, h * SCALE))
        
        # Center him—this is extra important here since widths vary so much
        screen.blit(luffy_big, (WIDTH // 2 - (w * SCALE // 2), 250))
    except Exception as e:
        print(f"Error at frame {current_frame}: {e}")
        current_frame = 0

    # Logic: Cycle through the 11 frames
    current_frame = (current_frame + 1) % len(FRAME_DATA)

    pygame.display.flip()
    # Speed: 8-10 is usually good for these longer action sequences
    clock.tick(8)