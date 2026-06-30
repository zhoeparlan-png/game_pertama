import pygame
import math
import sys

# 🎨 Inisialisasi Pygame (Aman, Gak Bikin CPU Meledak!)
pygame.init()

# 🖥️ Pengaturan Layar (Mulus di i7-4770K)
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌈 Suparlan Rainbow Generator v1.0 🌈")

# ⏱️ Pengaturan Waktu (Anti-Shuttering kayak Labkom!)
clock = pygame.time.Clock()
FPS = 60

# 🧠 Variabel untuk Efek Pelangi (Bukan Transistor Kuantum!)
hue = 0.0
speed = 0.1  # Kecepatan gerak pelangi (0.1 - 2.0)

# 🔄 Loop Utama Program
running = True
while running:
    # 🛑 Cek Event (Biar Bisa Keluar Pake Tombol 'X')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # 🌈 Hitung Warna Pelangi (HSV to RGB)
    h = hue
    s = 1.0  # Saturation Maksimal (Biar Gonjreng!)
    v = 1.0  # Value Maksimal (Biar Terang!)
    
    # Rumus Konversi HSV ke RGB (Aman, Rumus Matematika!)
    hp = h * 6.0
    i = int(hp)
    f = hp - i
    p = v * (1.0 - s)
    q = v * (1.0 - f * s)
    t = v * (1.0 - (1.0 - f) * s)
    
    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    else:
        r, g, b = v, p, q
    
    color = (int(r * 255), int(g * 255), int(b * 255))

    # 🖌️ Gambar Background Warna Pelangi
    screen.fill(color)

    # 🆙 Update Hue (Biar Warnanya Gerak!)
    hue += speed / 360.0
    if hue > 1.0:
        hue = 0.0

    # 🔄 Update Layar (Mulus 60 FPS!)
    pygame.display.flip()
    
    # 💤 Jaga FPS Biar Gak Boros Listrik!
    clock.tick(FPS)

# ✅ Keluar dari Pygame (Aman, Gak Ninggalin Jejak!)
pygame.quit()
sys.exit()