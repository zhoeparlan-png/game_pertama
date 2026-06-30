import pygame
import random
import math

# --- 1. PARTIKEL DEBU ANGKASA (Opsional biar rame) ---
class Partikel:
    def __init__(self, x, y, warna):
        self.x, self.y = x, y
        sudut = random.uniform(0, 2 * math.pi)
        self.vx = math.cos(sudut) * random.uniform(2, 5)
        self.vy = math.sin(sudut) * random.uniform(2, 5)
        self.umur = random.randint(50, 100)
        self.warna = warna

    def update(self):
        slow_mo = 0.2
        self.x += self.vx * slow_mo
        self.y += self.vy * slow_mo
        self.umur -= 0.5

    def draw(self, screen):
        if self.umur > 0:
            pygame.draw.rect(screen, self.warna, (int(self.x), int(self.y), 2, 2))

# --- 2. SETUP ---
pygame.init()
lebar, tinggi = 800, 600
screen = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("pulsar object 💀")
clock = pygame.time.Clock()

pusat_x, pusat_y = 400, 300
sudut_rotasi = 0
partikel_list = []
running = True

# --- 3. MAIN LOOP ---
while running:
    screen.fill((5, 0, 10)) # Ungu tua gelap banget

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # A. EFEK PULSING INTI (Bintang Kerdil)
    # Slow-mo pulsing
    denyut = math.sin(pygame.time.get_ticks() * 0.005) * 3
    radius_inti = 10 + denyut
    pygame.draw.circle(screen, (200, 230, 255), (pusat_x, pusat_y), int(radius_inti)) # Inti Biru Putih
    pygame.draw.circle(screen, (255, 255, 255), (pusat_x, pusat_y), int(radius_inti - 3)) # Cahaya Putih tengah

    # B. LOGIKA LASER JET (Dua Arah)
    # Kecepatan rotasi dibuat lambat (Slow-mo)
    slow_mo_rotasi = 0.01
    sudut_rotasi += slow_mo_rotasi
    
    # Kita gambar laser pake banyak titik biar efeknya halus
    for i in range(10, 400, 5): 
        # Sinar Atas
        jx1 = pusat_x + math.sin(sudut_rotasi) * i
        jy1 = pusat_y + math.cos(sudut_rotasi) * i
        # Sinar Bawah
        jx2 = pusat_x - math.sin(sudut_rotasi) * i
        jy2 = pusat_y - math.cos(sudut_rotasi) * i
        
        # Gambar titik-titik laser biru elektrik
        warna_laser = (100, 150, 255)
        pygame.draw.circle(screen, warna_laser, (int(jx1), int(jy1)), 2)
        pygame.draw.circle(screen, warna_laser, (int(jx2), int(jy2)), 2)
        
        # Tambahin partikel debu yang keluar dari laser (biar cinematic)
        if random.random() > 0.98:
            partikel_list.append(Partikel(jx1, jy1, warna_laser))
            partikel_list.append(Partikel(jx2, jy2, warna_laser))

    # C. UPDATE & DRAW PARTIKEL DEBU
    for p in partikel_list[:]:
        p.update()
        if p.umur <= 0:
            partikel_list.remove(p)
        else:
            p.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()