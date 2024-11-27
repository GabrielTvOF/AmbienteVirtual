import sys

class RPG:
    def __init__(self):
        self.player_name = ""
        self.choices_made = []
        self.current_chapter = 0

    def start_game(self):
        self.display_intro()

    def display_intro(self):
        print("Bem-vindo a 'As Crônicas de Eryndor'!\n")
        print("Você é um jovem aventureiro de um reino desconhecido.")
        print("Seu destino está atrelado à profecia do Cristal de Eternidade.")
        self.player_name = input("Antes de começarmos, qual é o seu nome, herói? ")
        print(f"\nBem-vindo, {self.player_name}! Sua jornada começa agora...\n")
        self.first_choice()

    def first_choice(self):
        print("Capítulo 1: O Despertar do Herói\n")
        print("Você está em sua vila, prestes a iniciar seu treinamento.")
        print("No entanto, uma estranha visão aparece em seu sonho, onde o Cristal de Eternidade é revelado.")
        print("Você sente uma conexão profunda com ele, mas a profecia também fala de grandes sacrifícios.")
        print("\nO que você fará?")
        print("1: Decidir seguir a jornada e buscar o Cristal.")
        print("2: Ignorar a visão e continuar sua vida como antes.")
        
        choice = input("Escolha 1 ou 2: ")
        self.handle_first_choice(choice)

    def handle_first_choice(self, choice):
        if choice == "1":
            print("\nVocê decide seguir a jornada em busca do Cristal de Eternidade, impulsionado pela visão em seu sonho.")
            self.choices_made.append("seguiu_jornada")
            self.second_choice()
        elif choice == "2":
            print("\nVocê decide ignorar a visão e continuar sua vida simples na vila. No entanto, algo parece te afastar da paz...")
            self.choices_made.append("ignorou_visao")
            self.end_game_bad()
        else:
            print("\nEscolha inválida. Tente novamente.")
            self.first_choice()

    def second_choice(self):
        print("\nCapítulo 2: O Confronto dos Reinos\n")
        print("Você chega à cidade de Avalora, onde encontra a feiticeira Lyra.")
        print("Ela está disposta a ajudar você, mas revela que os outros reinos também estão atrás do Cristal, e a guerra pode ser iminente.")
        print("\nO que você faz?")
        print("1: Alinhar-se com Lyra para encontrar o Cristal.")
        print("2: Ir sozinho em busca do Cristal, desconfiando de todos ao seu redor.")
        
        choice = input("Escolha 1 ou 2: ")
        self.handle_second_choice(choice)

    def handle_second_choice(self, choice):
        if choice == "1":
            print("\nVocê decide confiar em Lyra e formar uma aliança com ela, acreditando que ela pode ajudá-lo a encontrar o Cristal.")
            self.choices_made.append("aliado_lyra")
            self.third_choice()
        elif choice == "2":
            print("\nVocê decide seguir sozinho, desconfiando das intenções de todos. Você sabe que isso será mais difícil, mas prefere a solidão.")
            self.choices_made.append("foi_sozinho")
            self.third_choice()
        else:
            print("\nEscolha inválida. Tente novamente.")
            self.second_choice()

    def third_choice(self):
        print("\nCapítulo 3: O Caminho Final\n")
        print("À medida que você se aproxima do Cristal, as opções ficam mais difíceis.")
        print("Você sente o peso do destino sobre seus ombros. O que fazer?")
        print("\nO que você fará?")
        print("1: Usar o Cristal para restaurar a paz, acreditando que seu poder pode equilibrar os reinos.")
        print("2: Destruir o Cristal para evitar que alguém o use para fins malignos.")
        print("3: Esconder o Cristal, esperando que o tempo resolva o problema.")
        print("4: Liberar todo o poder do Cristal, acreditando que é a única maneira de salvar Eryndor.")

        choice = input("Escolha 1, 2, 3 ou 4: ")
        self.handle_third_choice(choice)

    def handle_third_choice(self, choice):
        if choice == "1":
            print("\nVocê decide usar o Cristal para restaurar a paz e equilibrar os reinos.")
            self.choices_made.append("usou_cristal")
            self.end_game_good()
        elif choice == "2":
            print("\nVocê decide destruir o Cristal para evitar que alguém o use para fins malignos.")
            self.choices_made.append("destruiu_cristal")
            self.end_game_tragic()
        elif choice == "3":
            print("\nVocê decide esconder o Cristal, esperando que o tempo resolva o problema. No entanto, a corrupção mágica continua a crescer.")
            self.choices_made.append("escondeu_cristal")
            self.end_game_bad()
        elif choice == "4":
            print("\nVocê decide liberar todo o poder do Cristal, acreditando que ele pode restaurar o equilíbrio de uma vez por todas.")
            self.choices_made.append("liberou_poder")
            self.end_game_heroic()
        else:
            print("\nEscolha inválida. Tente novamente.")
            self.third_choice()

    def end_game_good(self):
        print("\nFim do jogo: O retorno da harmonia.\nVocê restaurou a paz em Eryndor, e os reinos agora vivem em harmonia. Você será lembrado como o herói que uniu todos os povos.")
    
    def end_game_tragic(self):
        print("\nFim do jogo: O exílio do Cristal.\nA destruição do Cristal causou uma catástrofe em Eryndor. Embora a guerra tenha terminado, o continente foi corrompido pela magia selvagem.")
    
    def end_game_bad(self):
        print("\nFim do jogo: O Reino de Ferro.\nO mundo de Eryndor caiu em ruínas, os reinos estavam em guerra e nada poderia salvar a terra da destruição inevitável.")
    
    def end_game_heroic(self):
        print("\nFim do jogo: O sacrifício do herói.\nVocê sacrificou sua vida para liberar o poder do Cristal, restaurando Eryndor e purificando as terras corrompidas. Seu nome será lembrado para sempre.")

# Executando o jogo
game = RPG()
game.start_game()
