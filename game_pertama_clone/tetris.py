import pygame
import random

# --- KONFIGURASI ---
LEBAR_LAYAR = 300
TINGGI_LAYAR = 600
UKURAN_KOTAK = 30
KOLOM = LEBAR_LAYAR // UKURAN_KOTAK
BARIS = TINGGI_LAYAR // UKURAN_KOTAK

# Warna
HITAM = (0, 0, 0)
PUTIH = (255, 255, 255)
MERAH = (255, 0, 0)
BIRU = (0, 0, 255)

pygame.init()
layar = pygame.display.set_mode((LEBAR_LAYAR, TINGGI_LAYAR))
pygame.display.set_caption("Tetris Challenge Ayah")

# 1. Inisialisasi Grid (Papan)
grid = [[HITAM for _ in range(KOLOM)] for _ in range(BARIS)]

# 2. Fungsi Hapus Baris (BINTANG UTAMANYA ✨)
def hapus_baris(grid):
    baris_baru = [baris for baris in grid if any(sel == HITAM for sel in baris)]
    jumlah_hapus = BARIS - len(baris_baru)
    # Tambah baris kosong baru di atas
    for _ in range(jumlah_hapus):
        baris_baru.insert(0, [HITAM for _ in range(KOLOM)])
    return baris_baru, jumlah_hapus

# 3. Setup Balok Sederhana (Cuma kotak 1x1 buat simulasi gampang)
balok_x, balok_y = 5, 0
skor = 0
clock = pygame.time.Clock()

jalan = True
while jalan:
    layar.fill(HITAM)
    
    # Kecepatan jatuh
    balok_y += 0.1 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalan = False
        # Kontrol Kanan Kiri
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and balok_x > 0: balok_x -= 1
            if event.key == pygame.K_RIGHT and balok_x < KOLOM-1: balok_x += 1
            if event.key == pygame.K_DOWN: balok_y += 1

    # Logika kalau balok nyentuh dasar atau tumpukan
    if int(balok_y) >= BARIS or grid[int(balok_y)][int(balok_x)] != HITAM:
        grid[int(balok_y)-1][int(balok_x)] = MERAH
        balok_x, balok_y = 5, 0 # Reset balok baru
        # CEK HAPUS BARIS!
        grid, n = hapus_baris(grid)
        skor += n * 100

    # Gambar Grid yang sudah terisi
    for y in range(BARIS):
        for x in range(KOLOM):
            pygame.draw.rect(layar, grid[y][x], (x*UKURAN_KOTAK, y*UKURAN_KOTAK, UKURAN_KOTAK-1, UKURAN_KOTAK-1))

    # Gambar Balok yang lagi jatuh
    pygame.draw.rect(layar, BIRU, (int(balok_x)*UKURAN_KOTAK, int(balok_y)*UKURAN_KOTAK, UKURAN_KOTAK-1, UKURAN_KOTAK-1))

    pygame.display.update()
    clock.tick(30)

pygame.quit()