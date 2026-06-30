import pygame
import random
import math

# Inisialisasi
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Atom Orbital Cloud - Python 3.11 Mode")

# Palet Warna (Biar mirip screenshot kamu)
BLACK = (5, 5, 10)
CORE_BRIGHT = (255, 255, 255)  # Inti putih terang
PURPLE = (160, 32, 240)        # Ungu luar
ORANGE = (255, 69, 0)          # Oranye tengah

def draw_orbital_cloud(center, num_dots):
    for _ in range(num_dots):
        # Milih area (Lobe Atas, Lobe Bawah, atau Inti)
        seed = random.random()
        
        angle = random.uniform(0, 2 * math.pi)
        
        if seed < 0.4: # Lobe Atas
            dist_x = random.gauss(0, 60)
            dist_y = -abs(random.gauss(100, 50)) # Pakai minus biar ke atas
            color = PURPLE
        elif seed < 0.8: # Lobe Bawah
            dist_x = random.gauss(0, 60)
            dist_y = abs(random.gauss(100, 50))  # Pakai plus biar ke bawah
            color = PURPLE
        else: # Area Inti yang padat
            dist_x = random.gauss(0, 30)
            dist_y = random.gauss(0, 30)
            color = ORANGE

        x = center[0] + dist_x
        y = center[1] + dist_y
        
        # Gambar titik-titik elektronnya
        size = random.randint(1, 2)
        pygame.draw.circle(screen, color, (int(x), int(y)), size)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # 1. Gambar Inti Atom (Nucleus) - Putih Berpijar
    pygame.draw.circle(screen, CORE_BRIGHT, (WIDTH//2, HEIGHT//2), 10)
    
    # 2. Gambar Orbital Cloud (Setiap frame titiknya diacak ulang biar 'getar')
    # Kita pakai 1200 titik supaya dapet kesan 'kabut' yang padat
    draw_orbital_cloud((WIDTH//2, HEIGHT//2), 1200)

    pygame.display.flip()
    clock.tick(24) # FPS agak rendah biar flicker-nya kerasa kayak kamera jadul

pygame.quit()