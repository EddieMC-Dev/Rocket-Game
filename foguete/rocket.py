import pygame

class Rocket():
    def __init__(self, screen, ai_settings):
        """Gera a imagem do foguete e define sua posição inicial."""
        self.screen = screen
        self.image = pygame.image.load('image/rocket.png')
        
        # Coleta o retângulo da imagem e da janela
        self.rect = self.image.get_rect()
        self.rect_screen = self.screen.get_rect()
        
        # Define uma posição central a imagem com base na janela
        self.rect.centerx = self.rect_screen.centerx
        self.rect.centery = self.rect_screen.centery
        
        # Se o foguete vai se mover para a direita, esquerda, baixo ou cima.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Armazena valores decimais para o centro da nave
        self.center = [float(self.rect.centerx), float(self.rect.centery)]

        # Define a velocidade do foguete
        self.speed = ai_settings.rocket_speed
        
    def blitme(self):
        """Coloca o foguete no jogo, define sua posição atual e limita
        o deslocamento do nave."""
        self.screen.blit(self.image, self.rect)
        
        if self.moving_right and self.rect.right < self.rect_screen.right:
            self.center[0] += self.speed
        if self.moving_left and self.rect.left > self.rect_screen.left:
            self.center[0] -= self.speed 
        if self.moving_down and self.rect.bottom < self.rect_screen.bottom:
            self.center[1] += self.speed
        if self.moving_up and self.rect.top > self.rect_screen.top:
            self.center[1] -= self.speed
        
        # Atualiza a posição do centro da nave  
        self.rect.center = self.center