import pygame
import random
import math

# --- 1. PARTIKEL JET GAMMA ---
class PartikelGamma:
    def __init__(self, x, y, arah_y):
        self.x = x
        self.y = y
        # Jet super tipis (sumbu X cuma geser dikit)
        self.vx = random.uniform(-0.4, 0.4) 
        # Kecepatan Y tinggi (arah_y: -1 atas, 1 bawah)
        self.vy = random.uniform(18, 28) * arah_y 
        self.umur = random.randint(40, 70)
        # Warna Ungu/Neon (Energi Tinggi)
        self.warna = (200, 0, 255)

    def update(self):
        slow_mo = 0.15 # Efek Cinematic Slow Motion
        self.x += self.vx * slow_mo
        self.y += self.vy * slow_mo
        self.umur -= 0.4

    def draw(self, screen):
        if self.umur > 0:
            pygame.draw.rect(screen, self.warna, (int(self.x), int(self.y), 2, 2))

# --- 2. SETUP ---
pygame.init()
lebar, tinggi = 800, 600
screen = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("CINEMATIC GAMMA RAY BURST 💀")
clock = pygame.time.Clock()

pusat_x, pusat_y = 400, 300
partikel_list = []
bintang_radius = 25
fase = 1 # 1: Kolaps, 2: Flash, 3: Burst
durasi_burst = 0
flash_alpha = 0 # Buat efek silau

running = True

# --- 3. MAIN LOOP ---
while running:
    screen.fill((5, 0, 15)) # Background luar angkasa gelap

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # FASE 1: BINTANG KOLAPS (Hypernova)
    if fase == 1:
        bintang_radius -= 0.1 # Mengecil pelan
        # Warna berubah dari Biru -> Putih -> Oranye -> Hitam
        p = bintang_radius / 25
        warna = (255, int(200 * p), int(255 * p))
        pygame.draw.circle(screen, warna, (pusat_x, pusat_y), int(max(1, bintang_radius)))
        
        if bintang_radius <= 1:
            fase = 2 # Pindah ke kilatan cahaya
            flash_alpha = 255 # Full putih silau

    # FASE 2 & 3: FLASH & BURST JET
    elif fase >= 2:
        # Gambar Black Hole kecil di tengah
        pygame.draw.circle(screen, (0, 0, 0), (pusat_x, pusat_y), 5)
        
        # Munculin Jet (Fase 3)
        if fase == 2:
            durasi_burst = 100
            fase = 3 # Langsung lanjut ke burst
            
        if durasi_burst > 0:
            for i in range(80): # Tambah jumlah partikel (3000-an total)
                partikel_list.append(PartikelGamma(pusat_x, pusat_y, -1))
                partikel_list.append(PartikelGamma(pusat_x, pusat_y, 1))
            durasi_burst -= 1

        # Update & Draw Partikel
        for p in partikel_list[:]:
            p.update()
            if p.umur <= 0 or p.y < -50 or p.y > tinggi + 50:
                partikel_list.remove(p)
            else:
                p.draw(screen)

        # EFEK SCREEN FLASH (Kilatan cahaya pas meledak)
        if flash_alpha > 0:
            s = pygame.Surface((lebar, tinggi))
            s.set_alpha(flash_alpha)
            s.fill((255, 255, 255)) # Kilatan putih
            screen.blit(s, (0, 0))
            flash_alpha -= 10 # Menghilang pelan-pelan

        # Reset kalau sudah selesai biar looping
        if len(partikel_list) == 0 and durasi_burst <= 0:
            fase = 1
            bintang_radius = 25

    pygame.display.flip()
    clock.tick(60)

pygame.quit()