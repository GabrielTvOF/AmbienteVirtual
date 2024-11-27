import pygame

janela = pygame.display.set_mode([736, 476])

pygame.display.set_caption('RPG DE TEXTO')

imagem_fundo = pygame.image.load('ksksksksksk.jpg')

loop = True

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    janela.blit(imagem_fundo, (0, 0))
    
    pygame.display.update()