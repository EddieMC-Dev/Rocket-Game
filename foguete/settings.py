import pygame

class Settings():
    """Armazena as configurações básicas do jogo."""
    def __init__(self):
        """Inicia as configurações da janela e a velocidade da nave"""
        self.width_screen = 1200
        self.height_screen = 800
        self.bg_color = (50, 153, 204)
        self.rocket_speed = 1.5
        