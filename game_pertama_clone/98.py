import pygame
import random

# --- 1. SETUP ---
pygame.init()
lebar, tinggi = 800, 600
screen = pygame.display.set_mode((lebar, tinggi), pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption("PC Tahun 1999, Energy Star - Optimized")
clock = pygame.time.Clock()

f_bios = pygame.font.SysFont("Courier New", 18, bold=True)

# --- LOAD GAMBAR ---
try:
    img_win98 = pygame.image.load('windows 98.png').convert()
except FileNotFoundError:
    img_win98 = pygame.Surface((570, 430))
    img_win98.fill((0, 0, 139))

# --- PRE-RENDERING ---
scanline_surf = pygame.Surface((lebar, tinggi), pygame.SRCALPHA)
for y in range(0, tinggi, 3):
    pygame.draw.line(scanline_surf, (0, 0, 0, 50), (0, y), (lebar, y), 1)

monitor_frame = pygame.Surface((lebar, tinggi), pygame.SRCALPHA)
pygame.draw.circle(monitor_frame, (10, 15, 10, 255), (400, 300), 285)
for r in range(400, 285, -1):
    alpha = int((400 - r) * 2)
    pygame.draw.circle(monitor_frame, (0, 0, 0, alpha), (400, 300), r)

# --- DATA BIOS ---
boot_text = [
    "BIOS Version 1.0 - Lab Fariz",
    "CPU: Intel(R) Core(TM) Pentium 4 NetBurst @ 1.5 GHz",
    "Memory Test: 65536 KB OK",
    "",
    "Award Modular BIOS v1.51PG, Am Energy Star Ally",
    "Copyright (C) 1984 - 1997, Award Software, inc.",
    "(aftb008) EVALUATION ROM - NOT FOR SALE!",
    "",
    "Award Plug and Play BIOS Extention 1.0A",
    "Copyright (C) 1997, Award Software inc.",
    "",
    "Press DEL/F2 to enter startup",
    "Starting to boot windows 98......"
]

# --- VARIABEL FASE ---
baris_aktif = 0
fase = "BIOS" 
bar_progres_win98 = 0
running = True

# --- 3. MAIN LOOP ---
while running:
    screen.fill((5, 10, 5)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.USEREVENT + 1:
            fase = "WIN98_LOAD"
            pygame.time.set_timer(pygame.USEREVENT + 1, 0)

    # A. MONITOR FRAME
    screen.blit(monitor_frame, (0, 0))

    # B. LOGIKA FASE
    if fase == "BIOS":
        y_pos = 120
        for i in range(baris_aktif + 1):
            konten = boot_text[i]
            color = (200, 255, 200) if random.random() > 0.05 else (100, 150, 100)
            img_text = f_bios.render(konten, True, color)
            screen.blit(img_text, (180, y_pos))
            y_pos += 25

        if random.random() > 0.96 and baris_aktif < len(boot_text) - 1:
            baris_aktif += 1
            if baris_aktif == len(boot_text) - 1:
                pygame.time.set_timer(pygame.USEREVENT + 1, 3000)

    elif fase == "WIN98_LOAD":
        # --- SKALASI LOGO BIAR GAK GEPENG ---
        target_h = int(tinggi * 0.7)
        target_w = int(target_h * (570/430))
        img_scaled = pygame.transform.scale(img_win98, (target_w, target_h))
        
        s_win98 = pygame.Surface((lebar, tinggi), pygame.SRCALPHA)
        pos_x = (lebar - target_w) // 2
        pos_y = (tinggi - target_h) // 2
        s_win98.blit(img_scaled, (pos_x, pos_y))
        
        s_win98.set_alpha(200 + random.randint(-15, 15))
        screen.blit(s_win98, (0, 0))

        # --- PROGRESS BAR (DI-COMMENT BIAR BERSIH) ---
        # x, y, w, h = 250, 480, 300, 15
        # pygame.draw.rect(screen, (150, 150, 150), (x, y, w, h), 2)
        # num_boxes = int((bar_progres_win98 / 100) * (w // 10))
        # for i in range(num_boxes):
        #     pygame.draw.rect(screen, (0, 100, 255), (x + 5 + i*10, y + 4, 7, h - 8))
        
        # Logika Timer Tetap Jalan
        bar_progres_win98 += 0.5
        if bar_progres_win98 >= 100:
            bar_progres_win98 = 0 

    # C. EFEK JADUL
    screen.blit(scanline_surf, (0, 0))
    if random.random() > 0.98:
        s = pygame.Surface((lebar, tinggi), pygame.SRCALPHA)
        s.set_alpha(15)
        s.fill((255, 255, 255))
        screen.blit(s, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()