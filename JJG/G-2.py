import random
import sys

class RPG:
    def __init__(self):
        self.player_name = ""
        self.player_hp = 100
        self.enemy_hp = 50
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
        print("De repente, um monstro aparece e te desafia para um combate.")
        
        # Combate
        self.combat()

    def combat(self):
        print(f"\nVocê se prepara para a batalha! Seu HP: {self.player_hp} | HP do inimigo: {self.enemy_hp}")
        
        while self.player_hp > 0 and self.enemy_hp > 0:
            print("\nEscolha uma ação:")
            print("1: Atacar")
            print("2: Fugir")
            print("3: Curar")
            print("4: Desviar")

            action = input("Escolha 1, 2, 3 ou 4: ")

            if action == "1":
                self.attack_enemy()
            elif action == "2":
                self.flee_battle()
                break
            elif action == "3":
                self.heal_player()
            elif action == "4":
                self.dodge_enemy_attack()
            else:
                print("\nEscolha inválida. Tente novamente.")

            if self.enemy_hp > 0:
                self.enemy_turn()

        if self.player_hp > 0:
            print("\nVocê venceu o combate!")
            self.choices_made.append("venceu_combate")
            self.third_choice()
        else:
            self.end_game_bad()

    def attack_enemy(self):
        damage = random.randint(10, 20)
        self.enemy_hp -= damage
        print(f"\nVocê atacou o inimigo e causou {damage} de dano!")
        print(f"HP do inimigo: {self.enemy_hp}")

    def flee_battle(self):
        print("\nVocê decidiu fugir da batalha, mas o inimigo te persegue. Você tem que voltar para a luta!")
        self.enemy_hp += 10  # O inimigo recebe um bônus de vida ao tentar fugir
        print(f"HP do inimigo após perseguição: {self.enemy_hp}")

    def heal_player(self):
        heal = random.randint(5, 15)
        self.player_hp += heal
        print(f"\nVocê usou uma poção de cura e recuperou {heal} HP. Seu HP atual: {self.player_hp}")

    def dodge_enemy_attack(self):
        if random.random() < 0.5:
            print("\nVocê desviou com sucesso do ataque do inimigo!")
        else:
            damage = random.randint(5, 15)
            self.player_hp -= damage
            print(f"\nVocê tentou desviar, mas não conseguiu totalmente. Você tomou {damage} de dano. Seu HP: {self.player_hp}")

    def enemy_turn(self):
        if random.random() < 0.7:  # Chance de inimigo atacar
            damage = random.randint(5, 15)
            self.player_hp -= damage
            print(f"\nO inimigo atacou você e causou {damage} de dano! Seu HP: {self.player_hp}")
        else:
            print("\nO inimigo perdeu sua chance de atacar.")

    def third_choice(self):
        print("\nCapítulo 3: O Caminho Final\n")
        print("Após vencer o monstro, você chega perto do Cristal de Eternidade.")
        print("Agora você deve tomar uma decisão crítica.")
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
        self.ask_for_new_game()

    def end_game_tragic(self):
        print("\nFim do jogo: O exílio do Cristal.\nA destruição do Cristal causou uma catástrofe em Eryndor. Embora a guerra tenha terminado, o continente foi corrompido pela magia selvagem.")
        self.ask_for_new_game()

    def end_game_bad(self):
        print("\nFim do jogo: O Reino de Ferro.\nO mundo de Eryndor caiu em ruínas, os reinos estavam em guerra e nada poderia salvar a terra da destruição inevitável.")
        self.ask_for_new_game()

    def end_game_heroic(self):
        print("\nFim do jogo: O sacrifício do herói.\nVocê sacrificou sua vida para liberar o poder do Cristal, restaurando Eryndor e purificando as terras corrompidas. Seu nome será lembrado para sempre.")
        self.ask_for_new_game()

    def ask_for_new_game(self):
        print("\nGostaria de começar uma nova aventura ou tentar novamente a jornada?")
        print("1: Nova Aventura")
        print("2: Tentar Novamente")
        choice = input("Escolha 1 ou 2: ")
        
        if choice == "1":
            self.__init__()
            self.start_game()
        elif choice == "2":
            self.__init__()
            self.start_game()
        else:
            print("Escolha inválida. Tentando novamente...")
            self.ask_for_new_game()

# Executando o jogo
game = RPG()
game.start_game()

