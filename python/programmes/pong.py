import pygame
import random

# Initialisation de pygame
pygame.init()

# Définir les dimensions de la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paramètres du jeu
paddle_width, paddle_height = 15, 90
ball_width = 20
paddle_speed = 10
ball_speed_x, ball_speed_y = 5, 5

# Position des paddles
paddle_left = pygame.Rect(30, height // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle_right = pygame.Rect(width - 30 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)

# Position de la balle
ball = pygame.Rect(width // 2 - ball_width // 2, height // 2 - ball_width // 2, ball_width, ball_width)

# Fonction pour dessiner les objets
def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle_left)
    pygame.draw.rect(screen, WHITE, paddle_right)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.display.flip()

# Boucle principale
def main():
    global ball_speed_x, ball_speed_y
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Déplacement des paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle_left.top > 0:
            paddle_left.y -= paddle_speed
        if keys[pygame.K_s] and paddle_left.bottom < height:
            paddle_left.y += paddle_speed
        if keys[pygame.K_UP] and paddle_right.top > 0:
            paddle_right.y -= paddle_speed
        if keys[pygame.K_DOWN] and paddle_right.bottom < height:
            paddle_right.y += paddle_speed

        # Déplacement de la balle
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Collision avec le haut et le bas
        if ball.top <= 0 or ball.bottom >= height:
            ball_speed_y = -ball_speed_y

        # Collision avec les paddles
        if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
            ball_speed_x = -ball_speed_x

        # Si la balle sort du terrain, réinitialiser
        if ball.left <= 0 or ball.right >= width:
            ball.x = width // 2 - ball_width // 2
            ball.y = height // 2 - ball_width // 2
            ball_speed_x = random.choice([-5, 5])
            ball_speed_y = random.choice([-5, 5])

        # Dessiner tout
        draw()

        # Contrôler la vitesse du jeu
        clock.tick(60)

if __name__ == "__main__":
    main()
