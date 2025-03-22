import pygame
import random
import math

WIDTH, HEIGHT = 500, 500
NUM_PARTICLES = 500
PARTICLE_RADIUS = 10
INTERACTION_DISTANCE = PARTICLE_RADIUS * 2

COLORS = [(255, 0, 0), # red scissors
          (0, 255, 0), # green rock
          (0, 0, 255)] # blue paper

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RSP Automata")
clock = pygame.time.Clock()

class Particle:
    def __init__(self):
        self.type = random.randint(0, 2)
        self.x = random.uniform(0 + PARTICLE_RADIUS, WIDTH - PARTICLE_RADIUS)
        self.y = random.uniform(0 + PARTICLE_RADIUS, HEIGHT - PARTICLE_RADIUS)
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-3, 3)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 + PARTICLE_RADIUS or self.x >= WIDTH - PARTICLE_RADIUS:
            self.vx *= -1
        if self.y <= 0 + PARTICLE_RADIUS or self.y >= HEIGHT- PARTICLE_RADIUS:
            self.vy *= -1

    def interact(self, others):
        for other in others:
            if other == self:
                continue
            dx = self.x - other.x
            dy = self.y - other.y
            dist = math.hypot(dx, dy)
            if dist < INTERACTION_DISTANCE:
                if (self.type - other.type) % 3 == 1:
                    other.type = self.type

    def draw(self, surface):
        pygame.draw.circle(surface, COLORS[self.type], (int(self.x), int(self.y)), PARTICLE_RADIUS)

particles = [Particle() for _ in range(NUM_PARTICLES)]

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for p in particles:
        p.move()
        p.interact(particles)
        p.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
