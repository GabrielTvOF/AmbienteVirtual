import pygame
import random

# Configurações básicas
LARGURA, ALTURA = 600, 400  # Tamanho da janela Pygame
TAMANHO_CELULA = 20  # Tamanho de cada célula da masmorra
LARGURA_GRADE = LARGURA // TAMANHO_CELULA
ALTURA_GRADE = ALTURA // TAMANHO_CELULA

# Cores
COR_CAMINHO = (200, 200, 200)
COR_PAREDE = (50, 50, 50)
COR_INICIO = (0, 255, 0)
COR_FIM = (255, 0, 0)
COR_JOGADOR = (0, 0, 255)  # Cor do jogador

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Mapa de Masmorra Aleatória com Movimento")

# Função para gerar o mapa da masmorra
def gerar_mapa():
    # Inicializar o mapa com paredes
    mapa = [[1 for _ in range(LARGURA_GRADE)] for _ in range(ALTURA_GRADE)]
    
    # Definir o ponto inicial
    x, y = LARGURA_GRADE // 2, ALTURA_GRADE // 2
    mapa[y][x] = 0  # Marcar como caminho
    
    # Caminhada Aleatória
    passos = 1000  # Número de passos para a caminhada
    for _ in range(passos):
        # Escolher uma direção aleatória
        direcao = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        x = max(1, min(LARGURA_GRADE - 2, x + direcao[0]))
        y = max(1, min(ALTURA_GRADE - 2, y + direcao[1]))
        mapa[y][x] = 0  # Marcar como caminho
    
    return mapa, (LARGURA_GRADE // 2, ALTURA_GRADE // 2), (x, y)  # Retorna o mapa, início e fim

# Função para desenhar o mapa na tela
def desenhar_mapa(mapa, inicio, fim, jogador_pos):
    for y in range(ALTURA_GRADE):
        for x in range(LARGURA_GRADE):
            if mapa[y][x] == 1:
                cor = COR_PAREDE
            elif (x, y) == inicio:
                cor = COR_INICIO
            elif (x, y) == fim:
                cor = COR_FIM
            elif (x, y) == jogador_pos:
                cor = COR_JOGADOR
            else:
                cor = COR_CAMINHO
            pygame.draw.rect(screen, cor, (x * TAMANHO_CELULA, y * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))

# Função principal do jogo
def main():
    mapa, inicio, fim = gerar_mapa()
    jogador_pos = inicio  # A posição inicial do jogador é a mesma que a posição de início
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Processamento das teclas pressionadas
        teclas = pygame.key.get_pressed()
        nova_posicao = jogador_pos
        
        if teclas[pygame.K_UP]:  # Movimenta para cima
            nova_posicao = (jogador_pos[0], jogador_pos[1] - 1)
        elif teclas[pygame.K_DOWN]:  # Movimenta para baixo
            nova_posicao = (jogador_pos[0], jogador_pos[1] + 1)
        elif teclas[pygame.K_LEFT]:  # Movimenta para a esquerda
            nova_posicao = (jogador_pos[0] - 1, jogador_pos[1])
        elif teclas[pygame.K_RIGHT]:  # Movimenta para a direita
            nova_posicao = (jogador_pos[0] + 1, jogador_pos[1])
        
        # Verificar se a nova posição está dentro dos limites e é um caminho
        if 0 <= nova_posicao[0] < LARGURA_GRADE and 0 <= nova_posicao[1] < ALTURA_GRADE:
            if mapa[nova_posicao[1]][nova_posicao[0]] == 0:  # Verifica se é um caminho
                jogador_pos = nova_posicao  # Atualiza a posição do jogador
        
        screen.fill((0, 0, 0))  # Limpa a tela com a cor preta
        desenhar_mapa(mapa, inicio, fim, jogador_pos)  # Desenha o mapa e o jogador
        pygame.display.flip()  # Atualiza a tela
        
    pygame.quit()

# Executa o jogo
main()
