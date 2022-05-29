from pygame.math import Vector2  
from pygame.transform import rotozoom

from utils import load_sprite, wrap_position 

# gameObject Class
class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = position
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    
    def draw(self,surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self):
        self.position = self.position + self.velocity
    
    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius

    # Spaceship Class
UP = Vector2(0,-1)
class Spaceship(GameObject):
    def __init__(self, position):
        super().__init__(position, load_sprite("spaceship"), Vector2(0))
        # rotates the space ship - small rotates slower - large rotates faster
        MANEUVERABILITY = 3
        # Make a copy of the original UP vector
        self.direction = Vector2(UP)

        super().__init__(position, load_sprite("spaceship"), Vector2(0))

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)
        