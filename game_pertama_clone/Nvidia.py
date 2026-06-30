import pygame
import random
import math

# --- 1. SETTING PARTIKEL LEDAKAN ---
class Partikel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        sudut = random.uniform(0, 2 * math.pi)
        kecepatan = random.uniform(5, 15) 
        self.vx = math.cos(sudut) * kecepatan
        self.vy = math.sin(sudut) * kecepatan
        
        # Umur diperpanjang dikit biar efek slow-mo nya puas dilihat
        self.umur = random.randint(60, 120)
        self.warna = (255, random.randint(100, 255), random.randint(0, 50))

    def update(self):
        # --- VARIABEL CINEMATIC ---
        # 1.0 = Normal, 0.2 = Slow Motion Mantap
        slow_mo = 0.2 
        
        self.x += self.vx * slow_mo
        self.y += self.vy * slow_mo
        
        # Gesekan udara juga melambat (0.99 biar awet di layar)
        self.vx *= 0.99
        self.vy *= 0.99
        
        # Umur berkurang lebih lambat (0.4 biar durasi ledakan lama)
        self.umur -= 0.4

    def draw(self, screen):
        if self.umur > 0:
            pygame.draw.rect(screen, self.warna, (int(self.x), int(self.y), 2, 2))

# --- 2. SETUP ---
pygame.init()
lebar, tinggi = 800, 600
screen = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("Supernova Cinematic 3000 - Lab Fariz")
clock = pygame.time.Clock()

partikel_list = []
bintang_x, bintang_y = 400, 300
bintang_umur = 300
meledak = False
running = True

# --- 3. MAIN LOOP ---
while running:
    # Warna background biru angkasa gelap biar cinematic
    screen.fill((5, 0, 15)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not meledak:
        # LOGIKA PULSING (Makin tua makin deg-degan)
        speed = 0.01 + (1 - bintang_umur/300) * 0.15
        denyut = math.sin(pygame.time.get_ticks() * speed) * 5
        
        radius = 7 + denyut
        p = bintang_umur / 300
        warna = (255, int(255 * p), int(255 * p))
        
        pygame.draw.circle(screen, warna, (bintang_x, bintang_y), int(radius))
        
        bintang_umur -= 1
        if bintang_umur <= 0:
            meledak = True
            # TETAP 3000 BIAR LANCAR JAYA
            for i in range(3000):
                partikel_list.append(Partikel(bintang_x, bintang_y))
    
    else:
        # Update & Gambar Partikel
        for p in partikel_list[:]:
            p.update()
            if p.umur <= 0:
                partikel_list.remove(p)
            else:
                p.draw(screen)
        
        # Restart otomatis kalau ledakan sudah habis
        if len(partikel_list) == 0:
            meledak = False
            bintang_umur = 300

    pygame.display.flip()
    clock.tick(60) # Lock 60 FPS biar i7-4770K stabil

pygame.quit()