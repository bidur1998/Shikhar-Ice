import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 0.75
PLAYER_SPEED = 5
JUMP_HEIGHT = 15
ENEMY_SPEED = 3
PROJECTILE_SPEED = 8

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Assignment 3 game")

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT // 2)
        self.vel_y = 0
        self.health = 100
        self.lives = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_SPACE] and self.rect.bottom >= SCREEN_HEIGHT:
            self.vel_y = -JUMP_HEIGHT

        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel_x = PROJECTILE_SPEED

    def update(self):
        self.rect.x += self.vel_x

class Enemy(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 200)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - 30)
        self.vel_x = -ENEMY_SPEED

    def update(self):
        self.rect.x += self.vel_x

class Collectible(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 200)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - 20)

# Functions
def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def show_game_over_screen():
    screen.fill(BLACK)
    draw_text(screen, "GAME OVER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(screen, "Press R to Restart", 22, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False

# Game variables
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
collectibles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Initialize level variables
level = 1
num_enemies = 5
num_collectibles = 5

# Function to generate enemies and collectibles for the current level
def generate_level(level):
    for _ in range(num_enemies + level * 2):  # Increase number of enemies with each level
        enemy = Enemy(random.choice([GREEN, BLUE]))  # Different colored enemies
        all_sprites.add(enemy)
        enemies.add(enemy)
    
    for _ in range(num_collectibles + level * 2):  # Increase number of collectibles with each level
        collectible = Collectible(WHITE)
        all_sprites.add(collectible)
        collectibles.add(collectible)

generate_level(level)

clock = pygame.time.Clock()
running = True
game_over = False

# Game loop
while running:
    clock.tick(60)
    screen.fill(BLACK)

    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    projectile = Projectile(player.rect.right, player.rect.centery)
                    all_sprites.add(projectile)
                    projectiles.add(projectile)

        # Update
        all_sprites.update()

        # Check collisions
        hits = pygame.sprite.spritecollide(player, enemies, True)
        if hits:
            player.health -= 10

        hits = pygame.sprite.groupcollide(enemies, projectiles, True, True)
        for hit in hits:
            enemy = Enemy(random.choice([GREEN, BLUE]))  # Respawn enemies with different color
            all_sprites.add(enemy)
            enemies.add(enemy)

        hits = pygame.sprite.spritecollide(player, collectibles, True)
        for hit in hits:
            player.health += 10

        # Check game over
        if player.health <= 0:
            player.lives -= 1
            if player.lives <= 0:
                game_over = True
            else:
                player.health = 100

        # Check if player reached the end of the level
        if len(enemies) == 0 and len(collectibles) == 0:
            level += 1
            generate_level(level)

        # Draw
        all_sprites.draw(screen)
        draw_text(screen, f"Level: {level}", 18, 100, 10)
        draw_text(screen, f"Health: {player.health}", 18, 100, 30)
        draw_text(screen, f"Lives: {player.lives}", 18, 100, 50)

    else:
        show_game_over_screen()
        game_over = False
        player.health = 100
        player.lives = 3
        all_sprites.empty()
        enemies.empty()
        projectiles.empty()
        collectibles.empty()
        generate_level(level)  # Restart the game with level 1
        all_sprites.add(player)

    pygame.display.flip()

pygame.quit()
