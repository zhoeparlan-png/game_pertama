import pygame
import random

# Inisialisasi
pygame.init()

# Resolusi 1024x768
WIDTH, HEIGHT = 1024, 768
GRID_SIZE = 30
COLUMNS = 10
ROWS = 20

OFFSET_X = (WIDTH - (COLUMNS * GRID_SIZE)) // 2
OFFSET_Y = (HEIGHT - (ROWS * GRID_SIZE)) // 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris Lab Nuklir - Line Clear Edition | 100FPS")

pygame.mixer.init()
# Ganti 'musik_drift.mp3' sama nama file musik lu ya!
pygame.mixer.music.load('v1.mp3') 
pygame.mixer.music.set_volume(0.5) # Volume 50% biar gak pecah
pygame.mixer.music.play(-1) # Angka -1 artinya muter terus (loop)
# ---------------------------------

# Warna
BLACK = (5, 5, 10)
LINE_COLOR = (40, 40, 45)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# SHAPES dengan data rotasi
SHAPES = {
    'I': [[1, 5, 9, 13], [4, 5, 6, 7]], 
    'O': [[1, 2, 5, 6]],  
    'L': [[1, 5, 9, 10], [1, 2, 3, 5], [0, 1, 5, 9], [2, 4, 5, 6]]
}

class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = CYAN if shape == 'I' else YELLOW if shape == 'O' else ORANGE
        self.rotation = 0

    def get_coords(self):
        coords = []
        shape_format = SHAPES[self.shape][self.rotation % len(SHAPES[self.shape])]
        for i in shape_format:
            row = i // 4
            col = i % 4
            coords.append((self.x + col, self.y + row))
        return coords

def create_grid(locked_pos={}):
    grid = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]
    for (x, y), color in locked_pos.items():
        if y >= 0:
            grid[y][x] = color
    return grid

def valid_space(piece, grid):
    accepted_pos = [[(j, i) for j in range(COLUMNS) if grid[i][j] == BLACK] for i in range(ROWS)]
    accepted_pos = [item for sub in accepted_pos for item in sub]
    formatted = piece.get_coords()

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True

# FUNGSI BARU: HAPUS BARIS YANG PENUH
def clear_rows(grid, locked):
    inc = 0
    # Cek dari baris paling bawah ke atas
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        # Jika tidak ada warna BLACK di baris ini, berarti baris penuh
        if BLACK not in row:
            inc += 1
            # Hapus baris yang terkunci
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    
    if inc > 0:
        # Turunkan semua blok yang ada di atas baris yang dihapus
        # Kita urutkan kunci berdasarkan koordinat Y agar turunnya bener
        for key in sorted(list(locked.keys()), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < i: # Kondisi ini perlu diperbaiki agar semua yang di atas turun
                pass 
        
        # Logika turun yang lebih solid:
        new_locked = {}
        for key in sorted(list(locked.keys()), key=lambda x: x[1])[::-1]:
            x, y = key
            count = 0
            for r in range(len(grid)-1, -1, -1):
                if BLACK not in grid[r] and y < r:
                    count += 1
            new_locked[(x, y + count)] = locked[(x, y)]
        return new_locked
    return locked

def draw_window(grid):
    screen.fill(BLACK)
    pygame.draw.rect(screen, (60, 60, 70), (OFFSET_X-4, OFFSET_Y-4, COLUMNS*GRID_SIZE+8, ROWS*GRID_SIZE+8), 4)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(screen, grid[i][j], (OFFSET_X + j*GRID_SIZE, OFFSET_Y + i*GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
            pygame.draw.rect(screen, LINE_COLOR, (OFFSET_X + j*GRID_SIZE, OFFSET_Y + i*GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

def main():
    locked_positions = {}
    run = True
    current_piece = Piece(4, 0, random.choice(['I', 'O', 'L']))
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.3

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick(100) # Full power 100 FPS

        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                for pos in current_piece.get_coords():
                    locked_positions[(pos[0], pos[1])] = current_piece.color
                
                # CEK LINE CLEAR SETIAP KALI BLOK MENDARAT
                grid = create_grid(locked_positions)
                locked_positions = clear_rows(grid, locked_positions)
                
                current_piece = Piece(4, 0, random.choice(['I', 'O', 'L']))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid): current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid): current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid): current_piece.y -= 1
                if event.key == pygame.K_SPACE:
                    current_piece.rotation += 1
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1

        for x, y in current_piece.get_coords():
            if y > -1:
                grid[y][x] = current_piece.color

        draw_window(grid)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()