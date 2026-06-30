import pygame
import math

# Inisialisasi
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hydrogen (H) - Bohr Model")

# Warna
SPACE_BLACK = (5, 5, 10)
PROTON_RED = (255, 60, 60)
ELECTRON_BLUE = (0, 200, 255)
ORBIT_LINE = (60, 60, 80)

# Variabel Animasi
angle = 0.0
orbit_radius = 150
electron_speed = 0.08  # Hidrogen itu gesit!

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SPACE_BLACK)
    center = (WIDTH // 2, HEIGHT // 2)

    # 1. Gambar Inti (1 Proton)
    # Tambah efek glow dikit biar keren
    pygame.draw.circle(screen, (100, 0, 0), center, 15) # Shadow
    pygame.draw.circle(screen, PROTON_RED, center, 10)  # Core

    # 2. Gambar Lintasan Orbit (Cuma 1 karena Hidrogen)
    pygame.draw.circle(screen, ORBIT_LINE, center, orbit_radius, 1)

    # 3. Hitung Posisi Elektron tunggal
    angle += electron_speed
    x = center[0] + orbit_radius * math.cos(angle)
    y = center[1] + orbit_radius * math.sin(angle)

    # 4. Gambar si Elektron Jomblo
    pygame.draw.circle(screen, ELECTRON_BLUE, (int(x), int(y)), 6)
    # Efek kilau di elektron
    pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 2)

    # Info Teks
    font = pygame.font.SysFont("Consolas", 20)
    label = font.render("Atom: Hydrogen (H)", True, (200, 200, 200))
    desc = font.render("1 Proton | 1 Electron", True, (150, 150, 150))
    screen.blit(label, (20, 20))
    screen.blit(desc, (20, 45))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()