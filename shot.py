import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        direction = self.velocity.normalize()
        shot_length = 30
        end_position = self.position + (direction * shot_length)

        pygame.draw.line(surface, "white", self.position, end_position, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt