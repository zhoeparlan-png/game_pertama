import pygame
import random

# --- 1. SETUP ---
pygame.init()
lebar, tinggi = 800, 600
screen = pygame.display.set_mode((lebar, tinggi), pygame.DOUBLEBUF)
pygame.display.set_caption("PC Tahun 1999, Energy Star")
clock = pygame.time.Clock()

f = pygame.font.SysFont("Courier New", 18, bold=True)

# --- 2. PRE-RENDERING (BIAR GAK NOT RESPONDING) ---
# Kita gambar scanlines SEKALI SAJA di awal
scanline_surf = pygame.Surface((lebar, tinggi), pygame.SRCALPHA)
for y in range(0, tinggi, 3):
    pygame.draw.line(scanline_surf, (0, 0, 0, 60), (0, y), (lebar, y), 1)

# Kita gambar Frame Monitor (Cembung) SEKALI SAJA
monitor_frame = pygame.Surface((lebar, tinggi), pygame.SRCALPHA)
for r in range(400, 280, -1):
    alpha = int((400 - r) * 1.5)
    pygame.draw.circle(monitor_frame, (0, 0, 0, alpha), (400, 300), r)

# --- 3. LOGIKA BOOTING ---
boot_text = [
    "Energy Star",
     "",
    "Award Modular BIOS v1.51PG, Am Energy Star Ally",
    "Copyright (C) 1984 - 1997, Award Software, inc.",
    "",
    "(aftb008) EVALUATION ROM - NOT FOR SALE!",
    "Intel Core(TM) Pentium 4 NetBurst @ 1.5 GHz",
    "",
    "Memory Test : 65536 KB OK",
    "",
    "Award Plug and Play BIOS Extention 1.0A",
    "Copyright (C) 1997, Award Software inc.",
    "",
    "",
    "Press DEL/F2 to enter startup",
    "Starting to boot windows 98.......",


]

memori = 0
baris_aktif = 0
running = True

# --- 4. MAIN LOOP ---
while running:
    screen.fill((10, 15, 10)) # Warna dasar fosfor hijau tua

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # A. GAMBAR MONITOR ITEM (BACKGROUND)
    pygame.draw.circle(screen, (0, 0, 0), (400, 300), 285)

    # B. LOGIKA TEKS BIOS
    y_pos = 120
    # Gambar baris teks yang sudah "terbuka"
    for i in range(baris_aktif + 1):
        if i < len(boot_text):
            konten = boot_text[i]
            # Khusus baris memori, kita kasih angka jalan
            if "Memory Test" in konten:
                konten = f"Memory Test: {int(memori)} KB OK"
                if memori < 65536: memori += 1024 # Simulasi RAM 64MB
            
            # Efek Flicker Teks (pake alpha acak)
            color = (200, 255, 200) if random.random() > 0.05 else (100, 150, 100)
            img = f.render(konten, True, color)
            screen.blit(img, (180, y_pos))
            y_pos += 25

    # Tambahin baris baru setiap sekian detik
    if random.random() > 0.97 and baris_aktif < len(boot_text) - 1:
        if "Memory Test" in boot_text[baris_aktif] and memori < 65536:
            pass # Nunggu RAM selesai tes dulu
        else:
            baris_aktif += 1

    # C. TEMPEL SCANLINES & FRAME (YANG SUDAH JADI)
    screen.blit(scanline_surf, (0, 0))
    screen.blit(monitor_frame, (0, 0))

    # D. GLOBAL FLICKER (Simulasi Listrik CRT)
    if random.random() > 0.98:
        s = pygame.Surface((lebar, tinggi))
        s.set_alpha(15)
        s.fill((255, 255, 255))
        screen.blit(s, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()