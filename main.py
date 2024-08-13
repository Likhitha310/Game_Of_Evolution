import pygame
from bact1 import Bacteria1
from bact2 import Bacteria2
from bact3 import Bacteria3
from utils.helper_functions import wrap_around_screen, detect_collision

# Initialize the game
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game of Evolution")

# Create instances of bacteria
bacteria1 = Bacteria1([100, 100])
bacteria2 = Bacteria2([200, 200])
bacteria3 = Bacteria3([300, 300])

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))  # White background

    # Update and move bacteria
    bacteria1.position = wrap_around_screen(bacteria1.position, screen.get_width(), screen.get_height())
    bacteria2.move()
    bacteria2.position = wrap_around_screen(bacteria2.position, screen.get_width(), screen.get_height())
    bacteria3.move()
    bacteria3.position = wrap_around_screen(bacteria3.position, screen.get_width(), screen.get_height())

    # Detect collisions (optional example usage)
    if detect_collision(pygame.Rect(bacteria1.position, (20, 20)), pygame.Rect(bacteria2.position, (20, 20))):
        print("Collision detected between Bacteria1 and Bacteria2")

    # Draw bacteria
    bacteria1.draw(screen)
    bacteria2.draw(screen)
    bacteria3.draw(screen)

    # Update the display
    pygame.display.flip()

pygame.quit()
