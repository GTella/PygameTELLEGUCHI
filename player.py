import pygame, sys

class Player(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):
            super().__init__()
            self.sprites = []
            self.animating = False
            self.sprites.append(pygame.image.load('assets/image/direita_1.png'))
            self.sprites.append(pygame.image.load('assets/image/direita_2.png'))
            self.sprites.append(pygame.image.load('assets/image/direita_3.png'))
            self.sprites.append(pygame.image.load('assets/image/direita_4.png'))
            self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]
            
            self.rect = self.image.get_rect()
            self.rect.topleft = [pos_x, pos_y]
            
        def animate(self):
            self.animating = True
            
        def update(self):
            if self.animating == True:
                self.current_sprite += 1
            
                if self.current_sprite >= len(self.sprites):
                    self.current_sprite = 0
                    self.animating = False
                
                self.image = self.sprites[self.current_sprite]
        