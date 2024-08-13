import pygame
import math

class BacteriaSecondType:
    def __init__(self, x, y, color, r):
        self.x = x
        self.y = y
        self.color = color
        self.radius = r

    def attract2(self, other_bacteria):
        distance = math.sqrt((self.x - other_bacteria.x)**2 + (self.y - other_bacteria.y)**2)
        if distance == 0:  # Avoid division by zero
            return

        force = distance  # Attraction force
        force_repulsion = -distance  # Repulsion force

        alpha = math.atan2(other_bacteria.y - self.y, other_bacteria.x - self.x)

        # Update positions based on attraction
        self.x += force * math.cos(alpha)
        self.y += force * math.sin(alpha)
        other_bacteria.x -= force * math.cos(alpha)
        other_bacteria.y -= force * math.sin(alpha)

        # Check for collision
        if distance < self.radius + other_bacteria.radius:
            self.x += force_repulsion * math.cos(alpha)
            self.y += force_repulsion * math.sin(alpha)
            other_bacteria.x -= force_repulsion * math.cos(alpha)
            other_bacteria.y -= force_repulsion * math.sin(alpha)

    def draw2(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
