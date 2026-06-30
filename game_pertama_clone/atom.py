import pygame
import random
import math

# Inisialisasi
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Atom Electron Cloud Simulation - Python 3.14")

# Warna
BLACK = (10, 10, 15)
NUCLEUS_COLOR = (255, 50, 50)  # Merah (Proton)
ELECTRON_COLOR = (50, 150, 255) # Biru Muda

def draw_cloud(center, num_dots, radius_spread):
    for _ in range(num_dots):
        # Pakai Distribusi Gauss biar numpuk di tengah (kayak awan asli)
        angle = random.uniform(0, 2 * math.pi)
        
        # Semakin ke tengah semakin padat
        distance = abs(random.gauss(0, radius_spread))
        
        x = center[0] + math.cos(angle) * distance
        y = center[1] + math.sin(angle) * distance
        
        # Gambar elektron kecil dengan transparansi (opsional)
        size = random.randint(1, 2)
        pygame.draw.circle(screen, ELECTRON_COLOR, (int(x), int(y)), size)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # 1. Gambar Inti Atom (Nucleus)
    pygame.draw.circle(screen, NUCLEUS_COLOR, (WIDTH//2, HEIGHT//2), 10)

    # 2. Gambar Awan Elektron (Update setiap frame biar "bergetar")
    # 500 titik, spread radius 100
    draw_cloud((WIDTH//2, HEIGHT//2), 500, 100)

    pygame.display.flip()
    clock.tick(30) # 30 FPS biar efek flicker-nya dapet

pygame.quit()