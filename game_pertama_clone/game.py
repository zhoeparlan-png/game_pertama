import pygame

# 1. Inisialisasi Pygame
pygame.init()

# 2. Setup layar (Lebar, Tinggi)
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Tes Pygame Bro!")

running = True
while running:
    # 3. Cek event (biar window bisa di-close)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 4. Kasih warna background (RGB: Biru dongker)
    screen.fill((20, 30, 60))

    # 5. Update tampilan
    pygame.display.flip()

pygame.quit()