import pygame
import random

# Inisialisasi
pygame.init()
WIDTH, HEIGHT = 400, 600 # Gue tinggiin biar jalannya kerasa panjang
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Variabel Global
car = pygame.Rect(185, 500, 30, 50)
obstacles = []
score = 0
game_over = False

def reset_game():
    global car, obstacles, score, game_over
    car.topleft = (185, 500)
    obstacles.clear()
    score = 0
    game_over = False

def main():
    global score, game_over
    running = True
    
    while running:
        screen.fill((40, 40, 40)) # Warna aspal
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if game_over and event.key == pygame.K_r: # Tekan R buat reset
                    reset_game()

        if not game_over:
            # Kontrol Mobil (PC i7 kenceng lu pasti responsif banget)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and car.left > 0:
                car.x -= 5
            if keys[pygame.K_RIGHT] and car.right < WIDTH:
                car.x += 5

            # Munculin Rintangan (Obstacles)
            if random.randint(1, 40) == 1:
                obs_x = random.randint(0, WIDTH - 40)
                obstacles.append(pygame.Rect(obs_x, -50, 40, 40))

            # Gerakin Rintangan
            for obs in obstacles[:]:
                obs.y += 5
                if obs.top > HEIGHT:
                    obstacles.remove(obs)
                    score += 1
                
                # Cek Tabrakan (Collision)
                if car.colliderect(obs):
                    game_over = True

            # Gambar Mobil & Rintangan
            pygame.draw.rect(screen, (0, 255, 100), car) # Mobil Ijo
            for obs in obstacles:
                pygame.draw.rect(screen, (255, 50, 50), obs) # Musuh Merah
        else:
            # Tampilan Game Over
            msg = font.render("None"), True, ((255, 255, 255))
            screen.blit(msg, (WIDTH//2 - 120, HEIGHT//2))

        # Tampilan Skor
        txt = font.render(f"Skor: {score}", True, (255, 255, 0))
        screen.blit(txt, (10, 10))

        pygame.display.flip()
        clock.tick(60) # Biar stabil dan HP gak panas kayak iklan tadi

    pygame.quit()

if __name__ == "__main__":
    main()