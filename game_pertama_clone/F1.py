import pygame
import random
import sys

# --- 1. SETUP AWAL (BOOTING SISTEM) ---
pygame.init()

# Spek Monitor (Biar kenceng kyk i7!)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("🏁 F1 Rush Bekasi - Riz White Hat Dev 🏁")
clock = pygame.time.Clock()

# Warna-warna Dasar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100) # Warna Aspal
RED = (220, 20, 60) # Warna Mobil Musuh
BLUE = (0, 0, 200) # Warna Mobil Riz

# --- 2. CLASS MOBIL (LOGIKA GAME) ---
# --- 2. CLASS MOBIL (LOGIKA GAME) ---
class Car:
    def __init__(self, color, is_player=False):
        self.width = 40
        self.height = 80
        self.color = color
        self.is_player = is_player
        
        # Posisi Awal
        if is_player:
            self.x = (SCREEN_WIDTH / 2) - (self.width / 2)
            self.y = SCREEN_HEIGHT - self.height - 20
            self.vel = 7 
        else:
            self.lane = random.randint(0, 2)
            self.x = (self.lane * (SCREEN_WIDTH // 3)) + ((SCREEN_WIDTH // 3) / 2) - (self.width / 2)
            self.y = -self.height - random.randint(0, 300)
            self.vel = random.randint(3, 6)

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    # NAH, BAGIAN INI HARUS MENJOROK KE DALAM SEJAJAR SAMA DRAW!
    def move(self):
        if self.is_player:
            # --- JALUR PLAYER (WASD/Panah) ---
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > 0:
                self.x -= 5
            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < SCREEN_WIDTH - self.width:
                self.x += 5
            if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.y > 0:
                self.y -= 5
            if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.y < SCREEN_HEIGHT - self.width:
                self.y += 5

        else:
            self.lane = random.randint(0, 2)
            self.x = (self.lane * (SCREEN_WIDTH // 3)) + ((SCREEN_WIDTH // 3) / 2) - (self.width / 2)
            
            # Kita pendekin dikit biar cepet nongol, tapi tetep beda-beda jaraknya
            # Jaraknya: -300, -200, atau -100
            self.y = -self.height - random.randint(100, 400) 
            
            # Kalo ngerasa lambat, naikin speed minimalnya
            self.vel = random.randint(10, 20)

# --- 3. LOGIKA GAME UTAMA ---
player_car = Car(BLUE, is_player=True)
enemies = [Car(RED) for _ in range(3)] # Munculin 3 mobil musuh
game_state = "RUNNING" # Status game: RUNNING atau GAME_OVER

while game_state == "RUNNING":
    # Manajemen FPS (Biar gak thermal throttling!)
    clock.tick(60) # 60 FPS kenceng kyk SSD!

    # A. Cek Event (Tombol Silang, dll)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = "EXIT"

    # B. Update Logika Game
    player_car.move()
    for enemy in enemies:
        enemy.move()
        # Cek Tabrakan (Hacker Mode: Defensive)
        if (player_car.x < enemy.x + enemy.width and
            player_car.x + player_car.width > enemy.x and
            player_car.y < enemy.y + enemy.height and
            player_car.y + player_car.height > enemy.y):
            print("❌ WADUH RIZ! Tabrakan! Bengek Mode: Game Over! 💀💥")
            game_state = "GAME_OVER"

    # C. Gambar ke Layar (Rendering)
    screen.fill(GRAY) # Latar belakang aspal

    # Gambar Garis Jalan (Scrolling Effect)
    for i in range(10):
        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH/2 - 5, i*60 + (pygame.time.get_ticks()//10 % 60), 10, 30))

    player_car.draw()
    for enemy in enemies:
        enemy.draw()

    pygame.display.update()

# --- 4. GAME OVER SCREEN & SHUTDOWN ---
if game_state == "GAME_OVER":
    screen.fill(BLACK)
    font = pygame.font.SysFont('Arial', 32)
    text_surface = font.render('❌ BENGEK! GAME OVER 💀', True, RED)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(text_surface, text_rect)
    pygame.display.update()
    pygame.time.wait(3000) # Tunggu 3 detik sebelum mati

pygame.quit()
sys.exit()
