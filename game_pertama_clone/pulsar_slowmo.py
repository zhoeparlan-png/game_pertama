import pygame
import math
import random

# --- 1. SETUP SLOWMO ---
pygame.init()
lebar, tinggi = 900, 700
screen = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("Pulsar Slowmo - 15 FPS")
clock = pygame.time.Clock()
tengah = (lebar // 2, tinggi // 2)

# --- 2. DATA PULSAR ---
sudut = 0
radius_jet = 400
bintang = []
for _ in range(200): # Bikin 200 bintang background
    bintang.append([random.randint(0, lebar), random.randint(0, tinggi), random.randint(1, 3)])

# --- 3. LOOP UTAMA SLOWMO ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((5, 5, 15)) # Background biru gelap ruang angkasa

    # GAMBAR BINTANG
    for b in bintang:
        pygame.draw.circle(screen, (255, 255, 255), (b[0], b[1]), b[2])

    # GAMBAR PULSAR DI TENGAH
    pygame.draw.circle(screen, (200, 200, 255), tengah, 15) # Inti bintang
    pygame.draw.circle(screen, (255, 255, 255), tengah, 25, 2) # Aura

    # GAMBAR JET PULSAR Muter Slowmo
    x1 = tengah[0] + math.cos(sudut) * radius_jet
    y1 = tengah[1] + math.sin(sudut) * radius_jet
    x2 = tengah[0] + math.cos(sudut + math.pi) * radius_jet # Lawanan
    y2 = tengah[1] + math.sin(sudut + math.pi) * radius_jet

    pygame.draw.line(screen, (0, 200, 255), tengah, (x1, y1), 3) # Jet 1
    pygame.draw.line(screen, (0, 200, 255), tengah, (x2, y2), 3) # Jet 2

    # UPDATE SUDUT SLOWMO BANGET
    sudut += 0.01 # <--- INI KUNCINYA. 0.01 = LAMBAT. Coba 0.05 kalo kecepetan

    pygame.display.flip()
    clock.tick(15) # <--- SLOWMO. 15 FPS doang. Default 60

pygame.quit()