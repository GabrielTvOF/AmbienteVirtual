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
COR_BAU = (255, 215, 0)  # Cor do baú (dourado)

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Mapa de Masmorra com Sala de Baú e Pontuação")
font = pygame.font.Font(None, 36)  # Fonte para exibir a pontuação

# Função para criar uma sala no mapa
def criar_sala(mapa, x, y, largura, altura):
    for i in range(y, y + altura):
        for j in range(x, x + largura):
            if 0 <= i < ALTURA_GRADE and 0 <= j < LARGURA_GRADE:
                mapa[i][j] = 0  # Define como caminho

# Função para conectar duas salas com um corredor
def conectar_salas(mapa, x1, y1, x2, y2):
    # Cria um corredor horizontal e depois um vertical ou vice-versa
    if random.choice([True, False]):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            mapa[y1][x] = 0
        for y in range(min(y1, y2), max(y1, y2) + 1):
            mapa[y][x2] = 0
    else:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            mapa[y][x1] = 0
        for x in range(min(x1, x2), max(x1, x2) + 1):
            mapa[y2][x] = 0

# Função para gerar o mapa da masmorra com salas, corredores e uma sala de baú
def gerar_mapa():
    # Inicializar o mapa com paredes
    mapa = [[1 for _ in range(LARGURA_GRADE)] for _ in range(ALTURA_GRADE)]
    
    # Parâmetros para geração de salas
    num_salas = 6
    salas = []
    
    # Gera salas aleatórias
    for _ in range(num_salas):
        largura = random.randint(3, 6)
        altura = random.randint(3, 6)
        x = random.randint(1, LARGURA_GRADE - largura - 1)
        y = random.randint(1, ALTURA_GRADE - altura - 1)
        
        # Criar a sala no mapa
        criar_sala(mapa, x, y, largura, altura)
        salas.append((x + largura // 2, y + altura // 2))  # Centro da sala
    
    # Definir uma sala aleatória como sala de baú
    sala_bau = random.choice(salas)
    
    # Posicionar o baú em uma posição aleatória dentro da sala de baú
    bau_x = sala_bau[0]
    bau_y = sala_bau[1]
    mapa[bau_y][bau_x] = 2  # Marcar a posição do baú com o valor 2

    # Conectar as salas com corredores
    for i in range(1, len(salas)):
        x1, y1 = salas[i - 1]
        x2, y2 = salas[i]
        conectar_salas(mapa, x1, y1, x2, y2)
    
    return mapa, salas[0], salas[-1], (bau_x, bau_y)  # Retorna o mapa, ponto inicial, ponto final e posição do baú

# Função para desenhar o mapa na tela
def desenhar_mapa(mapa, inicio, fim, jogador_pos, bau_pos, pontuacao):
    for y in range(ALTURA_GRADE):
        for x in range(LARGURA_GRADE):
            if mapa[y][x] == 1:
                cor = COR_PAREDE
            elif (x, y) == inicio:
                cor = COR_INICIO
            elif (x, y) == fim:
                cor = COR_FIM
            elif (x, y) == bau_pos:
                cor = COR_BAU
            elif (x, y) == jogador_pos:
                cor = COR_JOGADOR
            else:
                cor = COR_CAMINHO
            pygame.draw.rect(screen, cor, (x * TAMANHO_CELULA, y * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))
    
    # Exibir pontuação
    texto_pontuacao = font.render(f"Pontuação: {pontuacao}", True, (255, 255, 255))
    screen.blit(texto_pontuacao, (10, 10))

# Função para verificar se a nova posição é válida
def posicao_valida(mapa, nova_posicao, bau_pos):
    if 0 <= nova_posicao[0] < LARGURA_GRADE and 0 <= nova_posicao[1] < ALTURA_GRADE:
        if mapa[nova_posicao[1]][nova_posicao[0]] == 0 or nova_posicao == bau_pos:
            return True
    return False

# Função principal do jogo
def main():
    mapa, inicio, fim, bau_pos = gerar_mapa()
    jogador_pos = inicio  # A posição inicial do jogador é a mesma que a posição de início
    bau_coletado = False  # Flag para verificar se o baú foi coletado
    pontuacao = 0  # Variável para armazenar a pontuação do jogador
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Processamento das teclas pressionadas uma vez por evento
            elif event.type == pygame.KEYDOWN:
                nova_posicao = jogador_pos
                
                if event.key == pygame.K_UP:  # Movimenta para cima
                    nova_posicao = (jogador_pos[0], jogador_pos[1] - 1)
                elif event.key == pygame.K_DOWN:  # Movimenta para baixo
                    nova_posicao = (jogador_pos[0], jogador_pos[1] + 1)
                elif event.key == pygame.K_LEFT:  # Movimenta para a esquerda
                    nova_posicao = (jogador_pos[0] - 1, jogador_pos[1])
                elif event.key == pygame.K_RIGHT:  # Movimenta para a direita
                    nova_posicao = (jogador_pos[0] + 1, jogador_pos[1])
                
                # Verificar se a nova posição está dentro dos limites e é um caminho
                if posicao_valida(mapa, nova_posicao, bau_pos):
                    jogador_pos = nova_posicao  # Atualiza a posição do jogador
        
        # Verifica se o jogador alcançou o baú
        if jogador_pos == bau_pos and not bau_coletado:
            bau_coletado = True  # Marca o baú como coletado
            pontuacao += 5  # Incrementa a pontuação

        # Verifica se o jogador alcançou o ponto final
        if jogador_pos == fim:
            # Gera uma nova fase ao alcançar o ponto final
            mapa, inicio, fim, bau_pos = gerar_mapa()
            jogador_pos = inicio  # Redefine a posição do jogador para o ponto inicial da nova fase
            bau_coletado = False  # Redefine o baú para a nova fase

        screen.fill((0, 0, 0))  # Limpa a tela com a cor preta
        desenhar_mapa(mapa, inicio, fim, jogador_pos, bau_pos if not bau_coletado else None, pontuacao)  # Desenha o mapa e o jogador
        pygame.display.flip()  # Atualiza a tela
        
    pygame.quit()

# Executa o jogo
main()
