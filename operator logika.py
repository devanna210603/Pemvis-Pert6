import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Lebar dan tinggi layar
WIDTH, HEIGHT = 800, 600

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ukuran dan posisi bola awal
bola_radius = 20
bola_x, bola_y = WIDTH // 2, HEIGHT // 2
kecepatan_x, kecepatan_y = 5, 5

# Inisialisasi layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gerak Bola")

# Loop utama
running = True
while running:
    # Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Menggerakkan bola
    bola_x += kecepatan_x
    bola_y += kecepatan_y

    # Memastikan bola tetap berada di dalam layar
    if bola_x - bola_radius <= 0 or bola_x + bola_radius >= WIDTH:
        kecepatan_x *= -1
    if bola_y - bola_radius <= 0 or bola_y + bola_radius >= HEIGHT:
        kecepatan_y *= -1

    # Membersihkan layar
    screen.fill(WHITE)

    # Menggambar bola
    pygame.draw.circle(screen, BLACK, (bola_x, bola_y), bola_radius)

    # Update layar
    pygame.display.flip()

# Keluar dari Pygame
pygame.quit()
sys.exit()
