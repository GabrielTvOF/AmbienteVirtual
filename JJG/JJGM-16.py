import pygame
import random
import pickle
import time
import os

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
font_ranking = pygame.font.Font(None, 30)  # Fonte para o ranking

# Estrutura de dados para o jogador
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.andares = {}  # Dicionário que mantém o melhor tempo e ranking de cada andar
        self.andares_completados = []  # Lista de andares completados
        self.tempo_inicio = time.time()
    
    def salvar(self):
        # Salva os dados do jogador em um arquivo
        with open(f'usuarios/{self.nome}.pkl', 'wb') as f:
            pickle.dump(self, f)
    
    @staticmethod
    def carregar(nome):
        try:
            with open(f'usuarios/{nome}.pkl', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None

# Função para verificar se o diretório de usuários existe
def verificar_diretorio_usuarios():
    if not os.path.exists('usuarios'):
        os.makedirs('usuarios')

# Função para pedir o nome do jogador
def pedir_nome():
    nome = ""
    digitando = True
    while digitando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                digitando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Pressionando Enter para confirmar
                    digitando = False
                elif event.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]  # Apaga o último caractere
                else:
                    nome += event.unicode  # Adiciona o caractere digitado
        screen.fill(COR_MENU)
        texto = font.render("Digite seu nome: " + nome, True, COR_TEXTO)
        screen.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2))
        pygame.display.flip()
        pygame.time.Clock().tick(30)
    
    # Verifica se o jogador já existe
    jogador = Jogador.carregar(nome)
    if jogador is None:
        jogador = Jogador(nome)  # Cria um novo jogador
    return jogador

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

# Função para atualizar o ranking de cada andar
def atualizar_ranking_andar(jogador, andar, tempo):
    if andar not in jogador.andares:
        jogador.andares[andar] = {'tempo': tempo, 'ranking': []}
    else:
        melhor_tempo = jogador.andares[andar]['tempo']
        if tempo < melhor_tempo:
            jogador.andares[andar]['tempo'] = tempo

    ranking = jogador.andares[andar]['ranking']
    ranking.append((jogador.nome, tempo))
    ranking = sorted(ranking, key=lambda x: x[1])  # Ordena por tempo
    jogador.andares[andar]['ranking'] = ranking[:10]  # Mantém os 10 melhores tempos

    jogador.salvar()

# Função para mostrar o ranking de um andar
def mostrar_ranking_andar(jogador, andar):
    if andar not in jogador.andares:
        return []
    return jogador.andares[andar]['ranking']

# Função para ir para o próximo andar
def proximo_andar(jogador, tempo_decorrido, andar_atual):
    atualizar_ranking_andar(jogador, andar_atual, tempo_decorrido)
    return andar_atual + 1

# Função principal do jogo
def main():
    # Inicializa o diretório de usuários
    verificar_diretorio_usuarios()
    
    # Pede o nome do jogador e carrega ou cria o jogador
    jogador = pedir_nome()
    
    andar_atual = 1
    tempo_inicio = time.time()
    
    # Gera o mapa para o andar atual
    mapa, inicio, fim, bau_pos = gerar_mapa()
    jogador_pos = inicio
    bau_coletado = False
    pontuacao = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            # Processa os eventos do jogador (movimento, coleta de baú, etc.)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Pausa o jogo e mostra o menu
                    pass  # Lógica de menu
    
        # Verifica se o jogador completou o andar
        if jogador_pos == fim:
            tempo_fim = time.time()
            tempo_decorrido = tempo_fim - tempo_inicio
            jogador_pos = inicio
            bau_coletado = False
            pontuacao = 0
            andar_atual = proximo_andar(jogador, tempo_decorrido, andar_atual)
            
            # Gera o próximo mapa
            mapa, inicio, fim, bau_pos = gerar_mapa()
            tempo_inicio = time.time()  # Reinicia o tempo

        # Desenha o mapa e a interface do jogo
        screen.fill((0, 0, 0))
        desenhar_mapa(mapa, fim, jogador_pos, bau_pos if not bau_coletado else None, pontuacao, [])
        
        pygame.display.flip()
        pygame.time.Clock().tick(30)  # Limita a taxa de quadros

    pygame.quit()
