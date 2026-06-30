import pygame

# 1. Inisialisasi Mesin Game
pygame.init()
layar = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tantangan Balap Ayah")

# 2. Setup Mobil (Warna Merah kayak Proton)
mobil_x = 375
mobil_y = 500
kecepatan = 5

jalan = True
while jalan:
    pygame.time.delay(10) # Biar nggak terlalu cepet kyk cahaya
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalan = False

    # 3. Kontrol Input (Logika Gerak)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and mobil_x > 0:
        mobil_x -= kecepatan
    if keys[pygame.K_RIGHT] and mobil_x < 750:
        mobil_x += kecepatan

    # 4. Gambar ke Layar
    layar.fill((30, 30, 30)) # Aspal item
    pygame.draw.rect(layar, (255, 0, 0), (mobil_x, mobil_y, 50, 80)) # Mobil kita
    
    pygame.display.update()

pygame.quit()