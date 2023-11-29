import pygame as py
import sys

# Inicialização do pygame
py.init()

# Definição das dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Definição de cores
light_grey = (200, 200, 200)

# Criar a tela
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
py.display.set_caption("Exemplo de Sprite")

# Carregar a imagem (sprite)
humberto_image = py.image.load("assets/image/humberto.png")
humberto_image = py.transform.scale(humberto_image, (30, 30))
humberto_rect = humberto_image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

# Loop principal
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    # Limpar a tela
    screen.fill((0, 0, 0))

    # Desenhar a sprite (imagem)
    screen.blit(humberto_image, humberto_rect)

    # Atualizar a tela
    py.display.flip()

    # Controlar a taxa de atualização
    py.time.Clock().tick(60)
