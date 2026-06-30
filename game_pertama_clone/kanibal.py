import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock() # Buat ngatur FPS

# Posisi awal si Kotak (Pemain)
player_x = 300
player_y = 200
player_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- LOGIKA INPUT KEYBOARD ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # --- GAMBAR DI LAYAR ---
    screen.fill((20, 30, 60)) # Background Biru Gelap

    # Gambar Kotak Merah (Pemain)
    # pygame.draw.rect(tujuan, warna, [x, y, lebar, tinggi])
    pygame.draw.rect(screen, (255, 0, 0), [player_x, player_y, 50, 50])

    pygame.display.flip()
    
    # Limit FPS ke 60 biar gak kecepetan
    clock.tick(60)

pygame.quit()