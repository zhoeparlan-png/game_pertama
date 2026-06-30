import pygame
import math

# Inisialisasi
pygame.init()
WIDTH, HEIGHT = 900, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Uranium-92 Bohr Model - Nuclear Mode ☢️")

# Warna
SPACE = (5, 5, 15)
NUCLEUS_COLOR = (255, 50, 50)   # Proton (Merah)
NEUTRON_COLOR = (100, 100, 100) # Neutron (Abu-abu)
ELECTRON_COLOR = (0, 255, 100)  # Elektron (Neon Green biar keren)
ORBIT_COLOR = (50, 50, 80)

# Konfigurasi Kulit Uranium (Total 92 elektron)
# Kulit: K, L, M, N, O, P, Q
URANIUM_SHELLS = [2, 8, 18, 32, 21, 9, 2]
angles = [0.0] * 92  # Posisi sudut awal buat semua elektron

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SPACE)
    center = (WIDTH // 2, HEIGHT // 2)

    # 1. Gambar Inti Atom (Nucleus) - Bikin agak gede karena Uranium berat
    pygame.draw.circle(screen, NUCLEUS_COLOR, center, 15)
    pygame.draw.circle(screen, (200, 0, 0), center, 18, 2) # Outer glow proton

    # 2. Gambar Orbit dan Elektron
    electron_idx = 0
    for shell_num, electron_count in enumerate(URANIUM_SHELLS):
        radius = 50 + (shell_num * 50) # Jarak antar kulit
        
        # Gambar garis orbit
        pygame.draw.circle(screen, ORBIT_COLOR, center, radius, 1)
        
        # Kecepatan putar: Kulit dalam lebih cepet daripada kulit luar
        speed = 0.05 / (shell_num + 1)
        
        for i in range(electron_count):
            # Update sudut biar muter
            angles[electron_idx] += speed
            
            # Hitung posisi X, Y berdasarkan sin/cos
            angle_offset = (2 * math.pi / electron_count) * i
            current_angle = angles[electron_idx] + angle_offset
            
            x = center[0] + radius * math.cos(current_angle)
            y = center[1] + radius * math.sin(current_angle)
            
            # Gambar Elektron
            pygame.draw.circle(screen, ELECTRON_COLOR, (int(x), int(y)), 4)
            # Tambah efek cahaya dikit di elektron
            pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 1)
            
            electron_idx += 1

    # Text Info
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("Uranium (U) - 92 Electrons", True, (255, 255, 255))
    screen.blit(text, (20, 20))

    pygame.display.flip()
    clock.tick(60) # 60 FPS biar smooth parah

pygame.quit()