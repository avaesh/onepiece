import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 1. LOAD THE SHEET
try:
    # Use .convert() for solid background sheets
    sheet = pygame.image.load("boa_sheet.png").convert()
    
    # --- AUTO-DETECT GREEN ---
    # We grab the color of the very first pixel (0,0) 
    # as that is almost always the background color.
    bg_color = sheet.get_at((0, 0))
    sheet.set_colorkey(bg_color) 
    
    print(f"Detected Background Color: {bg_color}")
except Exception as e:
    print(f"Load Error: {e}")
    pygame.quit()
    sys.exit()

# 2. COORDINATES (Your Row 824px)
CUTS = [51, 132, 191, 281, 355, 417, 501, 568, 618, 666]
Y_START, Y_END = 824, 923
FRAME_H = Y_END - Y_START

current_frame = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dark background to check for transparency leaks
    screen.fill((30, 30, 30)) 

    try:
        x = CUTS[current_frame]
        w = CUTS[current_frame + 1] - x
        
        # Grab the frame
        boa_sprite = sheet.subsurface((x, Y_START, w, FRAME_H))
        
        # --- THE ANTI-HALO FIX ---
        # If green edges still exist, this line forces a 'hard' 
        # transparency on the current surface.
        boa_sprite.set_colorkey(bg_color)

        boa_big = pygame.transform.scale(boa_sprite, (w * 4, FRAME_H * 4))
        screen.blit(boa_big, (WIDTH // 2 - (w * 2), 200))
        
    except Exception as e:
        current_frame = 0

    current_frame = (current_frame + 1) % (len(CUTS) - 1)
    pygame.display.flip()
    clock.tick(10)