import sys
import pygame

def update_screen(screen, ai_settings, rocket):
    """Atualiza os elementos na tela."""
    screen.fill(ai_settings.bg_color)
    rocket.blitme()
    pygame.display.flip()  
    
def check_events(rocket):
    """Verifica os eventos."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        check_keydown(event, rocket)
        check_keyup(event, rocket)
                
def check_keydown(event, rocket):
    """Cuida dos eventos de pressionamentos de tecla."""
    if event.type == pygame.KEYDOWN:
      keydown = True
      move_right(event, rocket, keydown)
      move_left(event, rocket, keydown)
      move_down(event, rocket, keydown)
      move_up(event, rocket, keydown)
            
def check_keyup(event, rocket):
    """Cuida dos eventos de solturas de tecla."""
    if event.type == pygame.KEYUP:
        keydown = False
        move_right(event, rocket, keydown)
        move_left(event, rocket, keydown)
        move_down(event, rocket, keydown)
        move_up(event, rocket, keydown)
        
def move_right(event, rocket, keydown):
    """Ativa ou desativa não o movimento pra direita."""
    if event.key == pygame.K_RIGHT:
        if keydown:
            rocket.moving_right = True
        else:
            rocket.moving_right = False
        
def move_left(event, rocket, keydown):
    """Ativa ou desativa o movimento pra esquerda."""
    if event.key == pygame.K_LEFT:
        if keydown:
            rocket.moving_left = True
        else:
            rocket.moving_left = False
            
def move_down(event, rocket, keydown):
    """Ativa ou desativa o movimento pra baixo."""
    if event.key == pygame.K_DOWN:
        if keydown:
            rocket.moving_down = True
        else:
            rocket.moving_down = False   
            
def move_up(event, rocket, keydown):
    """Ativa ou desativa o movimento pra cima."""
    if event.key == pygame.K_UP:
        if keydown:
            rocket.moving_up = True
        else:
            rocket.moving_up = False
            
