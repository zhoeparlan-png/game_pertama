import pygame
import math
import random

# Inisialisasi
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# --- DATA BINTANG ---
# 1. Bintang Latar (statis)
bg_stars = [[random.randint(0, WIDTH), random.randint(0, HEIGHT)] for _ in range(500)]

# 2. Bintang Galaksi (Spiral dengan 2 lengan)
stars = []
for _ in range(2500):
    r = random.uniform(50, 280)
    # Gunakan choice([0, pi]) untuk memaksa bentuk 2 lengan
    angle = random.choice([0, math.pi]) + random.uniform(-0.3, 0.3)
    # Tambahin sedikit random noise ke radius tiap bintang
    # Ini bikin lengkukan lengannya kelihatan lebih "tebal" dan natural
    r_noise = r + random.uniform(-10, 10) 
    stars.append([r_noise, angle])

# --- VARIABEL LOOP ---
running = True
rotation = 0

# --- LOOP UTAMA ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0, 0, 0)) # Background hitam
    
    # Update rotasi pelan-pelan
    rotation += 0.001
    
    # 1. Gambar Bintang Latar (Layer Belakang)
    for bs in bg_stars:
        pygame.draw.circle(screen, (50, 50, 80), bs, 1)
        
    # 2. Gambar Galaksi (Layer Depan)
    for r, angle in stars:
        # Rumus spiral arm: nambahin offset r ke sudut
        spiral_effect = r * 0.06
        current_angle = angle + rotation + spiral_effect
        
        x = 400 + r * math.cos(current_angle)
        y = 300 + r * math.sin(current_angle)
        
        # Gambar bintang galaksi
        pygame.draw.circle(screen, (100, 200, 255), (int(x), int(y)), 1)
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()