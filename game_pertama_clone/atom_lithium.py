import pygame
import math

# 1. Setup Dasar
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SIMULASI ATOM LITHIUM - LAB FARIZ")
clock = pygame.time.Clock()

# Warna-warna partikel
WHITE = (255, 255, 255)
RED = (255, 50, 50)      # Proton
BLUE = (50, 50, 255)     # Neutron
YELLOW = (255, 255, 0)   # Elektron
GRAY = (50, 50, 50)      # Orbit

angle = 0 # Sudut putaran elektron

def draw_nucleus():
    # Gambar Inti Atom (3 Proton + 4 Neutron ganti-gantian biar ngumpul)
    positions = [(0,0), (10,10), (-10,10), (10,-10), (-10,-10), (0, 15), (0, -15)]
    for i, pos in enumerate(positions):
        color = RED if i < 3 else BLUE
        pygame.draw.circle(screen, color, (WIDTH//2 + pos[0], HEIGHT//2 + pos[1]), 12)

running = True
while running:
    screen.fill((10, 10, 10)) # Luar angkasa gelap
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Gambar Orbit (Lintasan)
    pygame.draw.circle(screen, GRAY, (WIDTH//2, HEIGHT//2), 100, 1) # Kulit K
    pygame.draw.circle(screen, GRAY, (WIDTH//2, HEIGHT//2), 180, 1) # Kulit L

    # 3. Gambar Inti
    draw_nucleus()

    # 4. Logika & Gambar Elektron (Pake Matematika Trigonometri!)
    angle += 0.05
    
    # Elektron Kulit Dalam (2 biji)
    for i in range(2):
        # Rumus: x = Center + Radius * cos(Sudut), y = Center + Radius * sin(Sudut)
        ex = WIDTH//2 + 100 * math.cos(angle + i * math.pi)
        ey = HEIGHT//2 + 100 * math.sin(angle + i * math.pi)
        pygame.draw.circle(screen, YELLOW, (int(ex), int(ey)), 8)

    # Elektron Kulit Luar (1 biji - Valensi)
    ex = WIDTH//2 + 180 * math.cos(-angle * 0.5) # Putaran lebih lambat
    ey = HEIGHT//2 + 180 * math.sin(-angle * 0.5)
    pygame.draw.circle(screen, YELLOW, (int(ex), int(ey)), 8)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()