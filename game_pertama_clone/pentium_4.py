import pygame
import sys

# 1. SETUP AWAL
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EKSPERIMEN PENTIUM 4 - 5GHz")
clock = pygame.time.Clock()

# 2. SETUP FONT & TEKS
# Pake SysFont biar aman baca simbol derajat
font_besar = pygame.font.SysFont("arial", 50, bold=True)
font_kecil = pygame.font.SysFont("arial", 24)

suhu_val = -111.5
status_teks = "OVERCLOCKING STABLE"

# 3. LOOP UTAMA (The Heart of the Game)
running = True
while running:
    # A. Cek Event (Biar window bisa di-close/X)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # B. LOGIKA (Misal: bikin suhunya gerak-gerak dikit biar real)
    variasi = (pygame.time.get_ticks() % 10) / 10.0
    suhu_display = suhu_val + variasi

    # C. GAMBAR KE LAYAR
    screen.fill((10, 10, 30)) # Warna background gelap (Vibe Lab)

    # Render Teks Suhu (Pake Unicode derajat \u00b0)
    teks_suhu = font_besar.render(f"TEMP: {suhu_display:.1f}\u00b0C", True, (0, 255, 255))
    teks_ghz = font_besar.render("FREQ: 5.02 GHz", True, (255, 200, 0))
    teks_info = font_kecil.render(status_teks, True, (0, 255, 0))

    # Tempel ke layar (blit)
    screen.blit(teks_suhu, (150, 130))
    screen.blit(teks_ghz, (150, 190))
    screen.blit(teks_info, (210, 260))

    # D. UPDATE LAYAR
    pygame.display.flip()
    
    # E. LOCK FPS (Sesuai monitor 100Hz lu!)
    clock.tick(100)

# Keluar dari program kalau loop selesai
pygame.quit()
sys.exit()