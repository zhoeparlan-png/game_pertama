import pygame
import random

# Inisialisasi
pygame.init()
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lab Nuklir Tetris - 100FPS")


pygame.mixer.init()
# Ganti 'musik_drift.mp3' sama nama file musik lu ya!
pygame.mixer.music.load('v1.mp3') 
pygame.mixer.music.set_volume(0.5) # Volume 50% biar gak pecah
pygame.mixer.music.play(-1) # Angka -1 artinya muter terus (loop)
# ---------------------------------


# Warna (Vibe IPS Glow)
BLACK = (5, 5, 10)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)    # I-Block
YELLOW = (255, 255, 0)  # O-Block
ORANGE = (255, 165, 0)  # L-Block

# Definisi Bentuk Blok (Koordinat Relatif)
SHAPES = {
    'I': [[1, 5, 9, 13]], # Lurus memanjang
    'O': [[1, 2, 5, 6]],  # Kotak
    'L': [[1, 5, 9, 10]]  # Huruf L
}

class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.type = shape
        self.color = CYAN if shape == 'I' else YELLOW if shape == 'O' else ORANGE
        self.rotation = 0

    def get_image(self):
        return SHAPES[self.type][self.rotation]

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))

def main():
    clock = pygame.time.Clock()
    game_over = False
    
    # Pilih blok acak pertama
    current_piece = Piece(3, 0, random.choice(['I', 'O', 'L']))
    fall_time = 0
    
    while not game_over:
        screen.fill(BLACK)
        draw_grid()
        
        fall_speed = 500 # Kecepatan jatuh (ms)
        fall_time += clock.get_rawtime()
        clock.tick(100) # Tetap di 100 FPS biar smooth

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1

        # Logika Jatuh Otomatis
        if fall_time >= fall_speed:
            current_piece.y += 1
            fall_time = 0
            # Reset kalau mentok bawah (Simpel dulu)
            if current_piece.y > 15:
                current_piece = Piece(3, 0, random.choice(['I', 'O', 'L']))

        # Gambar Blok
        shape_data = current_piece.get_image()
        for i in shape_data:
            row = i // 4
            col = i % 4
            pygame.draw.rect(screen, current_piece.color, 
                             ((current_piece.x + col) * GRID_SIZE, 
                              (current_piece.y + row) * GRID_SIZE, 
                              GRID_SIZE - 2, GRID_SIZE - 2))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()