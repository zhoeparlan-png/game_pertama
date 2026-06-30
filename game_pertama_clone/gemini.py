import pygame
import os
from PIL import Image, ImageSequence # Baris baru dari screenshot lu!

# 1. SETUP AWAL (Struktur Tetap)
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# ... (kode import lu yang tadi)

def load_gif_with_pillow(filename):
    pil_image = Image.open(filename)
    frames = []
    
    # Ambil ukuran window lu (biar pas beneran)
    window_size = (800, 600) 
    
    for frame in ImageSequence.Iterator(pil_image):
        frame = frame.convert('RGBA')
        data = frame.tobytes()
        size = frame.size
        mode = frame.mode
        pygame_surface = pygame.image.fromstring(data, size, mode)
        
        # --- INI KUNCINYA RIZ! ---
        # Kita paksa frame-nya seukuran window (800x600)
        scaled_surface = pygame.transform.scale(pygame_surface, window_size)
        frames.append(scaled_surface)
        
    return frames

# ... (sisa kode main loop lu)

# Load logo Gemini atau GIF TADC lu
# Pastikan filenya ada di folder yang sama ya!
frames = load_gif_with_pillow("wow.gif") 
current_frame = 0

# 3. MAIN LOOP (Struktur Tetap)
running = True
while running:
    screen.fill((18, 18, 18)) # Background Gelap
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Fitur Kinger 98
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_9: # Tekan 9 buat simulasi error 98
                print("Caine Deleted by Kinger! 💀")

    # 4. UPDATE ANIMASI (Pake frame dari Pillow)
    current_frame = (current_frame + 1) % len(frames)
    rect = frames[current_frame].get_rect(center=(400, 300))
    screen.blit(frames[current_frame], rect)

    pygame.display.flip()
    clock.tick(30) # Speed animasi (20 FPS biar smooth di i7 lu)

pygame.quit()