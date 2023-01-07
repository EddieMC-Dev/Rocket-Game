import pygame
import game_functions as gf
from settings import Settings
from rocket import Rocket

def run_game():
    """Inicia o jogo, suas configurações e seus eventos."""
    pygame.init()
    # Instancia as configurações do jogo
    ai_settings = Settings()
    
    # Inicia a tela do jogo
    screen = pygame.display.set_mode((ai_settings.width_screen,
                                      ai_settings.height_screen))
    pygame.display.set_caption("Foguete Espacial")
    
    # Cria o foguete
    rocket = Rocket(screen, ai_settings)
    
    while True:
        gf.check_events(rocket)     
        gf.update_screen(screen, ai_settings, rocket)
         
run_game()    
