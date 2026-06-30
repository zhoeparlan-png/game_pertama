import pygame
import random

# Inisialisasi
pygame.init()

# Resolusi Mobile (Portrait)
WIDTH, HEIGHT = 450, 800
GRID_SIZE = 30
COLUMNS = 10
ROWS = 18 # Dikurangin biar ada space buat tombol di bawah

OFFSET_X = (WIDTH - (COLUMNS * GRID_SIZE)) // 2
OFFSET_Y = 50 # Kasih jarak dari atas

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris Mobile Lab Nuklir | 100FPS")

# Warna
BLACK = (5, 5, 10)
GRAY = (50, 50, 55)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# SHAPES
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

def clear_rows(grid, locked):
    new_locked = {}
    lines_cleared = 0
    for i in range(len(grid)-1, -1, -1):
        if BLACK in grid[i]:
            for j in range(COLUMNS):
                if (j, i) in locked:
                    new_locked[(j, i + lines_cleared)] = locked[(j, i)]
        else:
            lines_cleared += 1
    return new_locked

def draw_buttons():
    # Gambar Tombol Navigasi (Simulasi Touchscreen)
    btn_size = 60
    # Tombol Kiri, Bawah, Kanan
    pygame.draw.rect(screen, GRAY, (50, 650, btn_size, btn_size), 0, 10) # Left
    pygame.draw.rect(screen, GRAY, (130, 650, btn_size, btn_size), 0, 10) # Down
    pygame.draw.rect(screen, GRAY, (210, 650, btn_size, btn_size), 0, 10) # Right
    # Tombol Rotate (Gede di kanan)
    pygame.draw.circle(screen, (0, 150, 255), (360, 680), 45) # Rotate
    
    # Label Sederhana
    font = pygame.font.SysFont('Arial', 20, bold=True)
    screen.blit(font.render("<", True, WHITE), (70, 665))
    screen.blit(font.render("V", True, WHITE), (150, 665))
    screen.blit(font.render(">", True, WHITE), (230, 665))
    screen.blit(font.render("ROT", True, WHITE), (340, 670))

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
        clock.tick(100)

        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                for pos in current_piece.get_coords():
                    locked_positions[(pos[0], pos[1])] = current_piece.color
                locked_positions = clear_rows(create_grid(locked_positions), locked_positions)
                current_piece = Piece(4, 0, random.choice(['I', 'O', 'L']))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # Deteksi Klik Mouse (Simulasi Tap Layar)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                # Tombol Kiri
                if 50 < mx < 110 and 650 < my < 710:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid): current_piece.x += 1
                # Tombol Kanan
                if 210 < mx < 270 and 650 < my < 710:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid): current_piece.x -= 1
                # Tombol Bawah
                if 130 < mx < 190 and 650 < my < 710:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid): current_piece.y -= 1
                # Tombol Rotate (Lingkaran)
                if ((mx - 360)**2 + (my - 680)**2)**0.5 < 45:
                    current_piece.rotation += 1
                    if not valid_space(current_piece, grid): current_piece.rotation -= 1

        screen.fill(BLACK)
        # Draw Play Area
        pygame.draw.rect(screen, (60, 60, 70), (OFFSET_X-4, OFFSET_Y-4, COLUMNS*GRID_SIZE+8, ROWS*GRID_SIZE+8), 4)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(screen, grid[i][j], (OFFSET_X + j*GRID_SIZE, OFFSET_Y + i*GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
                pygame.draw.rect(screen, (30,30,35), (OFFSET_X + j*GRID_SIZE, OFFSET_Y + i*GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

        for x, y in current_piece.get_coords():
            if y > -1:
                pygame.draw.rect(screen, current_piece.color, (OFFSET_X + x*GRID_SIZE, OFFSET_Y + y*GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

        draw_buttons()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()