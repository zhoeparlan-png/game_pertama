import pygame
import math
import random

# 1. Setup Dasar & Monitor Gede
pygame.init()
WIDTH, HEIGHT = 750, 750 # Resolusi gede biar Bohr-nya megah
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MODEL BOHR: POLONIUM-210 (PO-210) - LAB NUKLIR FARIZ")
clock = pygame.time.Clock()

# Warna-warna partikel (Model Klasik)
BLACK = (10, 10, 15)
NEON_BLUE = (100, 200, 255) # Buat Teks
RED = (255, 60, 60)         # Proton
BLUE = (60, 60, 255)        # Neutron
YELLOW = (255, 255, 0)      # Elektron Bohr (Klasik)
ORBIT_COLOR = (80, 80, 80)  # Garis Orbit Rapi

angle = 0
# 2. Konfigurasi Elektron Bohr Po (84e-)
# Kulit: K, L, M, N, O, P
# Jumlah: 2, 8, 18, 32, 18, 6
electron_config = [2, 8, 18, 32, 18, 6]
# Jarak radius tiap orbit (Rapi bertingkat)
orbit_radii = [80, 130, 180, 230, 280, 330]

def draw_nucleus():
    # Inti Atom Padat & Rapi (84P + 126N)
    # Kita gambar gumpalan padat di tengah
    # Kita simulasiin aja proton/neutron-nya ngumpul rapi
    core_radius = 45
    num_protons = 84
    num_neutrons = 126
    total_particles = num_protons + num_neutrons
    
    for _ in range(total_particles):
        # Gunakan distribusi polar biar ngumpul di tengah
        # r = core_radius * math.sqrt(random.random())
        # angle_n = random.random() * 2 * math.pi
        # nx = WIDTH//2 + int(r * math.cos(angle_n))
        # ny = HEIGHT//2 + int(r * math.sin(angle_n))
        
        # Pake random uniform aja biar padat
        rx = random.uniform(-core_radius+5, core_radius-5)
        ry = random.uniform(-core_radius+5, core_radius-5)
        
        color = RED if random.random() < (num_protons/total_particles) else BLUE
        pygame.draw.circle(screen, color, (WIDTH//2 + int(rx), HEIGHT//2 + int(ry)), 7)

running = True
while running:
    screen.fill(BLACK) # Luar angkasa gelap
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. Gambar Inti padat di tengah (Lapis pertama biar ditumpuk orbit)
    draw_nucleus()

    angle += 0.01 # Kecepatan muter elektron (Semua sama biar seragam)
    
    # 4. Gambar Model Bohr: Orbit & Elektron Konsentris
    for i, (count, radius) in enumerate(zip(electron_config, orbit_radii)):
        # Gambar Garis Orbit Sempurna
        pygame.draw.circle(screen, ORBIT_COLOR, (WIDTH//2, HEIGHT//2), radius, 1)
        
        # Gambar Elektron di tiap Orbit (Konsentris)
        for j in range(count):
            # Rumus penempatan elektron Bohr:
            # Sudut e = (angle + j * (2π / count))
            e_angle = angle + j * (2 * math.pi / count)
            ex = WIDTH//2 + int(radius * math.cos(e_angle))
            ey = HEIGHT//2 + int(radius * math.sin(e_angle))
            
            # Elektron Kunit Bohr
            pygame.draw.circle(screen, YELLOW, (ex, ey), 8)
            # Kasih efek glow tipis di elektron biar keren di monitor 100Hz
            glow_surf = pygame.Surface((20, 20), pygame.SRCALPHA)
            pygame.draw.circle(glow_surf, (255, 255, 100, 80), (10, 10), 10)
            screen.blit(glow_surf, (ex-10, ey-10))

    # Teks Info Megah
    font_lg = pygame.font.Font(None, 48)
    font_sm = pygame.font.Font(None, 32)
    
    info1 = font_lg.render("MODEL BOHR: POLONIUM-210 (Po-210)", True, NEON_BLUE)
    info2 = font_sm.render(f"Konfigurasi Elektron: {electron_config}", True, YELLOW)
    info3 = font_sm.render(f"Status: SANGAT TIDAK STABIL (WARNING)", True, RED)
    
    screen.blit(info1, (20, 20))
    screen.blit(info2, (20, 70))
    screen.blit(info3, (20, 100))

    pygame.display.flip()
    clock.tick(100) # Biar monitor 100Hz lu makin adem

pygame.quit()