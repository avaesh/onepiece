import pygame
import sys

# 1. Setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Luffy: GBA Edition")
clock = pygame.time.Clock()

# 2. Load the Sprite Sheet
try:
    sheet = pygame.image.load("luffy_sheet.png").convert_alpha()
    # If the background is black, make it transparent
    sheet.set_colorkey((0, 0, 0)) 
except:
    print("Error: 'luffy_sheet.png' not found!")
    pygame.quit()
    sys.exit()

# 3. YOUR FINAL DIMENSIONS
FRAME_W = 40  # Width
FRAME_H = 50  # Length (Height)
TOTAL_FRAMES = 6  # Number of Luffys in the row
SCALE = 4         # Size on screen

# 4. State
current_frame = 0
luffy_x = -50
luffy_y = 300 # Vertical position

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- MOVE ---
    luffy_x += 6 # Speed of movement
    if luffy_x > WIDTH:
        luffy_x = -FRAME_W * SCALE

    # --- ANIMATE ---
    current_frame = (current_frame + 1) % TOTAL_FRAMES

    # --- DRAW ---
    screen.fill((30, 30, 30)) 

    # CROP RECTANGLE: (x_start, y_start, width, height)
    # We use 50 here to match your new Length!
    crop_rect = (current_frame * FRAME_W, 0, FRAME_W, FRAME_H)
    
    try:
        luffy_sprite = sheet.subsurface(crop_rect)
        luffy_big = pygame.transform.scale(luffy_sprite, (FRAME_W * SCALE, FRAME_H * SCALE))
        screen.blit(luffy_big, (luffy_x, luffy_y))
    except:
        # If the math is slightly off at the end of the row, this stops a crash
        current_frame = 0 

    pygame.display.flip()
    clock.tick(12) # Classic handheld game speed