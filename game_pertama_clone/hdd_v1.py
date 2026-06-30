import pygame
import math
import random

# Setup Dasar
pygame.init()
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HDD MECHANICAL SIMULATOR - SPINNING VERSION")
clock = pygame.time.Clock()

# Palet Warna Sesuai Foto
CASING_BLACK = (20, 20, 22)
PLATTER_SILVER = (220, 222, 225)
PLATTER_SHINE = (240, 242, 245)
ARM_METAL = (200, 200, 205)
MAGNET_DARK = (40, 42, 45)

# Variabel Mekanik
angle_platter = 0 # <--- INI VARIABEL BARU BUAT MUTER
arm_target_angle = 0
arm_current_angle = 0

def draw_hdd_base(platter_rot): # <--- TAMBAHIN PARAMETER platter_rot
    # 1. Casing Kotak Hitam
    pygame.draw.rect(screen, CASING_BLACK, (50, 50, 500, 600), border_radius=15)
    
    # 2. Piringan (Platter) Silver
    center = (280, 280)
    pygame.draw.circle(screen, PLATTER_SILVER, center, 220)
    
    # --- EFEK MUTAR (TEXTURE) ---
    # Kita gambar garis-garis halus biar kelihatan muter
    for i in range(0, 360, 45):
        rad = math.radians(platter_rot + i)
        lx = center[0] + int(210 * math.cos(rad))
        ly = center[1] + int(210 * math.sin(rad))
        # Garis refleksi cahaya tipis
        pygame.draw.line(screen, (200, 200, 205), center, (lx, ly), 1)

    pygame.draw.circle(screen, PLATTER_SHINE, center, 220, 3) # Efek mengkilap pinggir
    
    # Poros Tengah (Spindle Motor)
    pygame.draw.circle(screen, (160, 160, 165), center, 45)
    # Baut-baut Spindle (IKUT MUTER JUGA!)
    for i in range(6):
        bx = center[0] + 30 * math.cos(math.radians(platter_rot) + i * math.pi/3)
        by = center[1] + 30 * math.sin(math.radians(platter_rot) + i * math.pi/3)
        pygame.draw.circle(screen, (100, 100, 105), (int(bx), int(by)), 5)

def draw_actuator_assembly(angle):
    axis_pos = (460, 500) 
    pygame.draw.arc(screen, MAGNET_DARK, (400, 440, 140, 140), 0.5, 2.5, 40)
    
    arm_length = 310 
    rad = math.radians(205 + angle) 
    end_x = axis_pos[0] + arm_length * math.cos(rad)
    end_y = axis_pos[1] + arm_length * math.sin(rad)
    
    points = [
        (axis_pos[0] + 15, axis_pos[1] - 15),
        (axis_pos[0] - 15, axis_pos[1] + 15),
        (end_x, end_y)
    ]
    pygame.draw.polygon(screen, ARM_METAL, points)
    pygame.draw.rect(screen, (30, 30, 30), (end_x - 5, end_y - 5, 10, 10))
    
    pygame.draw.circle(screen, (180, 180, 185), axis_pos, 35)
    pygame.draw.circle(screen, (130, 130, 135), axis_pos, 8)

running = True
while running:
    screen.fill((230, 230, 235))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logika Gerak Lengan
    if abs(arm_current_angle - arm_target_angle) < 0.2:
        arm_target_angle = random.uniform(0, 35)
    arm_current_angle += (arm_target_angle - arm_current_angle) * 0.08
    
    # Update Putaran Piringan (Gas pol!)
    angle_platter += 15 # Ubah angka ini buat atur kecepatan putar

    # Render
    draw_hdd_base(angle_platter) # Masukin angle_platter ke sini
    draw_actuator_assembly(arm_current_angle)

    pygame.display.flip()
    clock.tick(100)

pygame.quit()