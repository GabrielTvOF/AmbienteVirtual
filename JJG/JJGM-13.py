import pygame
import random
import pickle
import time

# Configurações básicas
LARGURA, ALTURA = 600, 400  # Tamanho da janela Pygame
TAMANHO_CELULA = 20  # Tamanho de cada célula da masmorra
LARGURA_GRADE = LARGURA // TAMANHO_CELULA
ALTURA_GRADE = ALTURA // TAMANHO_CELULA

# Cores
COR_CAMINHO = (200, 200, 200)
COR_PAREDE = (50, 50, 50)
COR_FIM = (255, 0, 0)
COR_JOGADOR = (0, 0, 255)  # Cor do jogador
COR_BAU = (255, 215, 0)  # Cor do baú (dourado)
COR_MENU = (0, 0, 0)
COR_TEXTO = (255, 255, 255)

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Masmorra com Itens Rápidos e Ranking")
font = pygame.font.Font(None, 36)  # Fonte para exibir a pontuação
font_menu = pygame.font.Font(None, 48)  # Fonte para o menu

# Função para criar uma sala no mapa
def criar_sala(mapa, x, y, largura, altura):
    for i in range(y, y + altura):
        for j in range(x, x + largura):
            if 0 <= i < ALTURA_GRADE and 0 <= j < LARGURA_GRADE:
                mapa[i][j] = 0  # Define como caminho

# Função para conectar duas salas com um corredor
def conectar_salas(mapa, x1, y1, x2, y2):
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
    mapa = [[1 for _ in range(LARGURA_GRADE)] for _ in range(ALTURA_GRADE)]
    num_salas = 6
    salas = []
    for _ in range(num_salas):
        largura = random.randint(3, 6)
        altura = random.randint(3, 6)
        x = random.randint(1, LARGURA_GRADE - largura - 1)
        y = random.randint(1, ALTURA_GRADE - altura - 1)
        criar_sala(mapa, x, y, largura, altura)
        salas.append((x + largura // 2, y + altura // 2))
    sala_bau = random.choice(salas)
    bau_x = sala_bau[0]
    bau_y = sala_bau[1]
    mapa[bau_y][bau_x] = 2
    for i in range(1, len(salas)):
        x1, y1 = salas[i - 1]
        x2, y2 = salas[i]
        conectar_salas(mapa, x1, y1, x2, y2)
    return mapa, salas[0], salas[-1], (bau_x, bau_y)

# Função para desenhar o mapa na tela
def desenhar_mapa(mapa, fim, jogador_pos, bau_pos, pontuacao, itens_rapidos):
    for y in range(ALTURA_GRADE):
        for x in range(LARGURA_GRADE):
            if mapa[y][x] == 1:
                cor = COR_PAREDE
            elif (x, y) == fim:
                cor = COR_FIM
            elif (x, y) == bau_pos:
                cor = COR_BAU
            elif (x, y) == jogador_pos:
                cor = COR_JOGADOR
            else:
                cor = COR_CAMINHO
            pygame.draw.rect(screen, cor, (x * TAMANHO_CELULA, y * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))
    
    # Desenhar a barra de itens rápidos
    for i, item in enumerate(itens_rapidos):
        pygame.draw.rect(screen, (100, 100, 100), (10 + i * 100, ALTURA - 40, 90, 30))
        texto_item = font.render(item['nome'], True, COR_TEXTO)
        screen.blit(texto_item, (20 + i * 100, ALTURA - 35))
    
    texto_pontuacao = font.render(f"Pontuação: {pontuacao}", True, COR_TEXTO)
    screen.blit(texto_pontuacao, (10, 10))

# Função para desenhar o menu
def desenhar_menu(opcoes, opcao_selecionada, mensagem=None):
    screen.fill(COR_MENU)
    for i, opcao in enumerate(opcoes):
        cor = COR_TEXTO if i == opcao_selecionada else (150, 150, 150)
        texto = font_menu.render(opcao, True, cor)
        screen.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2 - 100 + i * 60))

    # Se houver uma mensagem, exibe-a na tela
    if mensagem:
        texto_mensagem = font.render(mensagem, True, COR_TEXTO)
        screen.blit(texto_mensagem, (LARGURA // 2 - texto_mensagem.get_width() // 2, ALTURA // 2 + 100))
    
    pygame.display.flip()

# Função de salvar o jogo
def salvar_jogo(jogador_pos, pontuacao, mapa, bau_pos, tempo_inicio, nome):
    with open('savegame.pkl', 'wb') as f:
        pickle.dump((jogador_pos, pontuacao, mapa, bau_pos, tempo_inicio, nome), f)

# Função de carregar o jogo
def carregar_jogo():
    try:
        with open('savegame.pkl', 'rb') as f:
            jogador_pos, pontuacao, mapa, bau_pos, tempo_inicio, nome = pickle.load(f)
            return jogador_pos, pontuacao, mapa, bau_pos, tempo_inicio, nome
    except FileNotFoundError:
        return None, None, None, None, None, None

# Função para mostrar o ranking
def mostrar_ranking():
    try:
        with open('ranking.pkl', 'rb') as f:
            ranking = pickle.load(f)
            ranking.sort(key=lambda x: x[1], reverse=True)  # Ordenar por pontuação
            return ranking
    except FileNotFoundError:
        return []

# Função para atualizar o ranking
def atualizar_ranking(nome, pontuacao):
    try:
        ranking = mostrar_ranking()
        ranking.append((nome, pontuacao))
        ranking.sort(key=lambda x: x[1], reverse=True)
        with open('ranking.pkl', 'wb') as f:
            pickle.dump(ranking, f)
    except Exception as e:
        print(f"Erro ao atualizar ranking: {e}")

# Função principal do jogo
def main():
    nome = input("Digite seu nome: ")
    mapa, inicio, fim, bau_pos = gerar_mapa()
    jogador_pos = inicio
    bau_coletado = False
    pontuacao = 0
    tempo_inicio = time.time()
    
    # Itens rápidos (com funções)
    itens_rapidos = [
        {'nome': 'Poção', 'efeito': 'cura', 'uso': False},
        {'nome': 'Espada', 'efeito': 'dano', 'uso': False},
        {'nome': 'Escudo', 'efeito': 'defesa', 'uso': False}
    ]
    
    ranking = mostrar_ranking()
    
    opcao_selecionada = 0
    em_menu = False
    mensagem_erro = None
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Processamento de teclas
            elif event.type == pygame.KEYDOWN:
                if not em_menu:
                    if event.key == pygame.K_ESCAPE:
                        em_menu = True  # Pausa e abre o menu
                    else:
                        nova_posicao = jogador_pos
                        if event.key == pygame.K_UP:
                            nova_posicao = (jogador_pos[0], jogador_pos[1] - 1)
                        elif event.key == pygame.K_DOWN:
                            nova_posicao = (jogador_pos[0], jogador_pos[1] + 1)
                        elif event.key == pygame.K_LEFT:
                            nova_posicao = (jogador_pos[0] - 1, jogador_pos[1])
                        elif event.key == pygame.K_RIGHT:
                            nova_posicao = (jogador_pos[0] + 1, jogador_pos[1])
                        
                        if posicao_valida(mapa, nova_posicao, bau_pos):
                            jogador_pos = nova_posicao
                    
                    if jogador_pos == bau_pos and not bau_coletado:
                        bau_coletado = True
                        pontuacao += random.randint(1, 15)  # Baú dá pontos aleatórios
                        
                    if jogador_pos == fim:
                        tempo_fim = time.time()
                        tempo_decorrido = tempo_fim - tempo_inicio
                        tempo_bonus = max(0, 100 - tempo_decorrido)  # Pontuação bônus baseada na rapidez
                        pontuacao += int(tempo_bonus)
                        mapa, inicio, fim, bau_pos = gerar_mapa()
                        jogador_pos = inicio
                        bau_coletado = False
                        tempo_inicio = time.time()  # Reinicia o tempo
                        
                else:
                    if event.key == pygame.K_UP:
                        opcao_selecionada = (opcao_selecionada - 1) % 5
                    elif event.key == pygame.K_DOWN:
                        opcao_selecionada = (opcao_selecionada + 1) % 5
                    elif event.key == pygame.K_RETURN:
                        if opcao_selecionada == 0:  # Ranking
                            ranking = mostrar_ranking()
                            print("Ranking:")
                            for i, (nome_ranking, pontos) in enumerate(ranking):
                                print(f"{i+1}. {nome_ranking}: {pontos} pontos")
                        elif opcao_selecionada == 1:  # Salvar Jogo
                            salvar_jogo(jogador_pos, pontuacao, mapa, bau_pos, tempo_inicio, nome)
                            print("Jogo salvo.")
                        elif opcao_selecionada == 2:  # Carregar Jogo
                            jogador_pos, pontuacao, mapa, bau_pos, tempo_inicio, nome = carregar_jogo()
                            if jogador_pos is None:
                                mensagem_erro = "Você não possui jogo salvo."
                            else:
                                print("Jogo carregado.")
                            em_menu = False
                        elif opcao_selecionada == 3:  # Itens Rápidos
                            pass  # Aqui podemos adicionar a lógica para usar os itens rápidos
                        elif opcao_selecionada == 4:  # Sair
                            running = False
                    
        if mensagem_erro:
            desenhar_menu(["Ranking", "Salvar Jogo", "Carregar Jogo", "Itens Rápidos", "Sair"], opcao_selecionada, mensagem_erro)
            pygame.time.wait(2000)  # Exibe a mensagem por 2 segundos
            mensagem_erro = None
            em_menu = False
        else:
            if not em_menu:
                screen.fill((0, 0, 0))
                desenhar_mapa(mapa, fim, jogador_pos, bau_pos if not bau_coletado else None, pontuacao, itens_rapidos)
            else:
                desenhar_menu(["Ranking", "Salvar Jogo", "Carregar Jogo", "Itens Rápidos", "Sair"], opcao_selecionada)
            
        pygame.display.flip()  # Atualiza a tela
    
    pygame.quit()

# Função para verificar se a nova posição é válida
def posicao_valida(mapa, nova_posicao, bau_pos):
    if 0 <= nova_posicao[0] < LARGURA_GRADE and 0 <= nova_posicao[1] < ALTURA_GRADE:
        if mapa[nova_posicao[1]][nova_posicao[0]] == 0 or nova_posicao == bau_pos:
            return True
    return False

# Executa o jogo
main()
