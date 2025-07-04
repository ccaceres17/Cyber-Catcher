import pygame
import random

# Inicialización
pygame.init()
WIDTH, HEIGHT = 600, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyber Catcher")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FONT = pygame.font.SysFont('Arial', 24)

# Jugador
hacker = pygame.Rect(275, 340, 50, 50)

# Objetos
packets = []
firewalls = []
score = 0
clock = pygame.time.Clock()

# Funciones para crear enemigos y puntos
def spawn_packet():
    x = random.randint(0, WIDTH - 30)
    packets.append(pygame.Rect(x, 0, 30, 30))

def spawn_firewall():
    x = random.randint(0, WIDTH - 50)
    firewalls.append(pygame.Rect(x, 0, 50, 50))

# Loop principal
running = True
while running:
    clock.tick(60)
    WIN.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and hacker.x > 0:
        hacker.x -= 5
    if keys[pygame.K_RIGHT] and hacker.x < WIDTH - hacker.width:
        hacker.x += 5

    # Spawn aleatorio
    if random.randint(0, 60) == 1:
        spawn_packet()
    if random.randint(0, 40) == 1:
        spawn_firewall()

    # Movimiento y colisión
    for packet in packets[:]:
        packet.y += 3
        if hacker.colliderect(packet):
            packets.remove(packet)
            score += 1
        elif packet.y > HEIGHT:
            packets.remove(packet)

    for firewall in firewalls[:]:
        firewall.y += 5
        if hacker.colliderect(firewall):
            running = False
        elif firewall.y > HEIGHT:
            firewalls.remove(firewall)

    # Dibujar
    pygame.draw.rect(WIN, BLUE, hacker)
    for packet in packets:
        pygame.draw.rect(WIN, GREEN, packet)
    for firewall in firewalls:
        pygame.draw.rect(WIN, RED, firewall)

    # Mostrar puntaje
    score_text = FONT.render(f"Score: {score}", True, (0, 0, 0))
    WIN.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()