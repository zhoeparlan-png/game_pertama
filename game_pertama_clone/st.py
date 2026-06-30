import pygame
import math
import random

# --- 1. SETUP ---
pygame.init()
lebar, tinggi = 800, 600
screen = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("Stephenson 2-18 Clean Version - Lab Fariz")
clock = pygame.time.Clock()

pusat_x, pusat_y = 400, 300
radius_dasar = 230

# Kita simpan posisi plasma biar gak ganti-ganti tiap frame (biar gak muter cepet)
plasma_spots = []
for _ in range(50):
    s = random.uniform(0, 2 * math.pi)
    d = random.uniform(0, radius_dasar * 0.7)
    plasma_spots.append([s, d, random.randint(30, 70)]) # [sudut, jarak, ukuran]

running = True

# --- 2. MAIN LOOP ---
while running:
    screen.fill((2, 0, 5)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # A. SLOW-MO PULSING
    denyut = math.sin(pygame.time.get_ticks() * 0.0007) * 12
    radius_skrg = radius_dasar + denyut

    # B. GLOW LUAR (Cinematic)
    for r in range(12, 0, -1):
        alpha = 30 - (r * 2)
        s = pygame.Surface((lebar, tinggi), pygame.SRCALPHA)
        pygame.draw.circle(s, (220, 40, 0, alpha), (pusat_x, pusat_y), int(radius_skrg + r*8))
        screen.blit(s, (0,0))

    # C. BODY BINTANG
    pygame.draw.circle(screen, (160, 20, 0), (pusat_x, pusat_y), int(radius_skrg))

    # D. TEKSTUR PLASMA (DIEM & NYATU)
    for spot in plasma_spots:
        # Posisinya ikut pulsing tapi gak pindah-pindah tempat
        sudut, jarak_persen, size = spot
        actual_dist = (jarak_persen / radius_dasar) * radius_skrg
        px = pusat_x + math.cos(sudut) * actual_dist
        py = pusat_y + math.sin(sudut) * actual_dist
        
        # Gambar plasma dengan gradasi (biar halus)
        s_plasma = pygame.Surface((150, 150), pygame.SRCALPHA)
        pygame.draw.circle(s_plasma, (255, 80, 0, 40), (75, 75), size)
        screen.blit(s_plasma, (int(px-75), int(py-75)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()