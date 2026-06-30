import pygame
from sys import exit

#game variables
GAME_WIDTH = 512
GAME_HEIGHT = 512

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Amogus 😂")
clock = pygame.time.Clock()

# left (x), top (y), width, height
player = pygame.Rect(150, 150, 50, 50)

def draw():
    window.fill("blue")
    pygame.draw.rect(window, (2, 239, 238), player)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # --- INI RAHASIANYA (DI LUAR FOR EVENT) ---
    keys = pygame.key.get_pressed() # Cek semua tombol yang lagi diteken
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= 5  # Geser kiri
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += 5  # Geser kanan
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= 5  # Geser atas
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += 5  # Geser bawah
    # ------------------------------------------

    draw()
    pygame.display.update()
    clock.tick(60) # Biar i7 lu gak kepanasan jalanin 1000 FPS!