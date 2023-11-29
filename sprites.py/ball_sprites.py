import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Definir constantes
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
light_grey = (200, 200, 200)

# Criar a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Sprite Redonda')

# Criar a classe do sprite
class SpriteRedonda(pygame.sprite.Sprite):
    def __init__(self, x, y, raio, imagem):
        super().__init__()
        self.image = pygame.image.load(imagem)
        self.image = pygame.transform.scale(self.image, (raio * 2, raio * 2))  # Ajustar o tamanho da imagem
        self.rect = self.image.get_rect(center=(x, y))

# Criar uma instância do sprite
humberto_sprite = SpriteRedonda(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 15, 'humberto.jpg')

# Criar um grupo de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(humberto_sprite)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpar a tela
    screen.fill((255, 255, 255))

    # Atualizar e desenhar os sprites
    all_sprites.update()
    all_sprites.draw(screen)

    # Atualizar a tela
    pygame.display.flip()
