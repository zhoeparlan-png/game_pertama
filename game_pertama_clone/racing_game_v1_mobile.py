import pygame
import random

# 1. Inisialisasi & Setup Layar Gede
pygame.init()
# Kita pake mode FULLSCREEN atau resolusi tinggi biar gak "melar"
WIDTH, HEIGHT = 455, 800 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JEBAKAN BATMAN MOBILE - FARIZ")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

# 2. Variabel Game
car = pygame.Rect(WIDTH//2 - 20, HEIGHT - 150, 40, 70)
obstacles = []
score = 0
game_over = False
speed = 7

# 3. Setup Tombol Mobile (Biar Gak Butuh Keyboard)
# Kita taruh di bawah layar biar jempol enak nekennya
btn_left = pygame.Rect(50, HEIGHT - 100, 80, 80)
btn_right = pygame.Rect(WIDTH - 130, HEIGHT - 100, 80, 80)
btn_reset = pygame.Rect(WIDTH//2 - 55, HEIGHT//2 + 50, 100, 55)

def reset_game():
    global car, obstacles, score, game_over, speed
    car.x = WIDTH//2 - 20
    car.y = HEIGHT - 150
    obstacles.clear()
    score = 0
    speed = 7
    game_over = False

while True:
    screen.fill((25, 25, 25)) # Aspal gelap
    
    # --- LOGIKA INPUT (TOUCH & MOUSE) ---
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # Logika Klik Reset pas Game Over
        if game_over and event.type == pygame.MOUSEBUTTONDOWN:
            if btn_reset.collidepoint(event.pos):
                reset_game()

    if not game_over:
        # Kontrol Mobile (Tekan tombol di layar)
        if mouse_click[0]: # Kalau layar ditekan
            if btn_left.collidepoint(mouse_pos) and car.left > 0:
                car.x -= 10
            if btn_right.collidepoint(mouse_pos) and car.right < WIDTH:
                car.x += 10

        # Logika Rintangan
        if random.randint(1, 25) == 1:
            obs_w = random.randint(50, 100)
            obs = pygame.Rect(random.randint(0, WIDTH-obs_w), -100, obs_w, 40)
            obstacles.append(obs)

        for obs in obstacles[:]:
            obs.y += speed
            if obs.top > HEIGHT:
                obstacles.remove(obs)
                score += 1
                if score % 5 == 0: speed += 0.5 # Makin lama makin ngebut!
            
            if car.colliderect(obs):
                game_over = True

        # --- GAMBAR SEMUANYA ---
        # Gambar Mobil
        pygame.draw.rect(screen, (0, 255, 150), car, border_radius=5)
        
        # Gambar Musuh
        for obs in obstacles:
            pygame.draw.rect(screen, (255, 50, 50), obs, border_radius=8)

        # Gambar Tombol Mobile (Transparan dikit)
        pygame.draw.rect(screen, (100, 100, 100), btn_left, border_radius=40)
        pygame.draw.rect(screen, (100, 100, 100), btn_right, border_radius=40)
        # Kasih tanda panah simpel
        screen.blit(font.render("<", True, (255,255,255)), (btn_left.x+30, btn_left.y+25))
        screen.blit(font.render(">", True, (255,255,255)), (btn_right.x+30, btn_right.y+25))

    else:
        # Tampilan JEBAKAN BATMAN
        msg1 = font.render("AHHAHHAHHAHHH!", True, (255, 50, 50))
        msg2 = font.render("KAMU MASUK JEBAKAN BATMAN", True, (255, 255, 255))
        
        screen.blit(msg1, (WIDTH//2 - 140, HEIGHT//2 - 100))
        screen.blit(msg2, (WIDTH//2 - 210, HEIGHT//2 - 50))
        
        # Tombol Reset Mobile
        pygame.draw.rect(screen, (0, 150, 255), btn_reset, border_radius=10)
        screen.blit(font.render("RESTART", True, (255,255,255)), (btn_reset.x+5, btn_reset.y+10))

    # Score
    txt = font.render(f"Skor: {score}", True, (255, 255, 0))
    screen.blit(txt, (20, 20))

    pygame.display.flip()
    clock.tick(60)