import pygame
import random

# Pygame initialization
pygame.init()

# Game window dimensions
WIDTH, HEIGHT = 600, 500

# Colors
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
PINK = (252, 3, 152)
PURPLE = (252, 170, 28)

# Font
font = pygame.font.Font(None, 34)

# Game objects
class Brick(pygame.Rect):
    def __init__(self, x, y, brick_type):
        super().__init__(x, y, 98, 38)
        self.brick_type = brick_type
        self.health = 1

    def update(self):
        if self.health > 0:
            self.draw()

    def draw(self):
        if self.brick_type == "green":
            color = GREEN
        elif self.brick_type == "pink":
            color = PINK
        else:
            color = PURPLE

        pygame.draw.rect(screen, color, self)

    def collision(self, ball):
        if pygame.rect.colliderect(self, ball):
            self.health -= 1
            return True
        return False

class Ball:
    def __init__(self, x, y):
        super().__init__(x, y, 10, 10)
        self.speed = 10
        self.direction = "DOWN"

    def update(self):
        if self.direction == "DOWN":
            self.y += self.speed
        elif self.direction == "UP":
            self.y -= self.speed
        if self.direction == "LEFT":
            self.x -= self.speed
        elif self.direction == "RIGHT":
            self.x += self.speed

        if self.x > 590 or self.x < 0:
            self.direction = "LEFT" if self.direction == "RIGHT" else "RIGHT"
        if self.y > 590 or self.y < 0:
            self.direction = "UP" if self.direction == "DOWN" else "DOWN"

        self.collision()

    def collision(self):
        for brick in bricks:
            if self.collision(brick):
                brick.health -= 1
                if brick.health == 0:
                    bricks.remove(brick)
                    self.speed += 5
                    if self.speed > 20:
                        self.speed = 20

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Brick Breaker Game")

    clock = pygame.time.Clock()
    FPS = 30

    # Define game objects
    ball = Ball(50, 250, 10, 10)
    bricks = [
        Brick(1 + i * 100, 60, "green"),
        Brick(1 + i * 100, 100, "pink"),
        Brick(1 + i * 100, 140, "purple")
        for i in range(6)
    ]

    score = 0
    lives = 3

    while continue_game:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continue_game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    ball.direction = "UP"
                if event.key == pygame.K_s:
                    ball.direction = "DOWN"
                if event.key == pygame.K_a:
                    ball.direction = "LEFT"
                if event.key == pygame.K_d:
                    ball.direction = "RIGHT"

        screen.fill(WHITE)

        for brick in bricks:
            brick.update()
            brick.draw(screen)

        ball.update()
        ball.draw(screen)

        score_text = font.render("SCORE: " + str(score), 1, WHITE)
        screen.blit(score_text, (10, 20))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()