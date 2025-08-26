import random
from raca import Humano, Elfo, Halfling

# Os atributos são determinados de acordo com o índice da lista
# 0 = Força
# 1 = Destreza
# 2 = Constituição
# 3 = Inteligência
# 4 = Sabedoria
# 5 = Carisma

class Personagem:
    def __init__(self, raca, estilo):
        self.atributos = {
            "forca": 0,
            "destreza": 0,
            "constituicao": 0,
            "inteligencia": 0,
            "sabedoria": 0,
            "carisma": 0,
            "XP": 0
        }
        self.raca = raca()
        self.determinar_atributos(estilo)
        bonus_raciais = self.raca.bonus()
        self.atributos.update(bonus_raciais)

    def __str__(self):
        base = (
            f"\t\t--> Atributos <--\t\t\n"
            f"FOR:\t{self.atributos['forca']}\n"
            f"DES:\t{self.atributos['destreza']}\n"
            f"CON:\t{self.atributos['constituicao']}\n"
            f"INT:\t{self.atributos['inteligencia']}\n"
            f"SAB:\t{self.atributos['sabedoria']}\n"
            f"CAR:\t{self.atributos['carisma']}\n\n"
            f"\t\t--> {self.atributos['nome']} <--\t\t\n"
            f"MOB:\t{self.atributos['mobilidade']}\n"
            f"INF:\t{self.atributos['infravisão']}\n"
            f"ALIGN:\t{self.atributos['alinhamento']}\n"
        )

        return base
    
# Como a decisão de estilos aparentemente afeta somente a criação de personagens, então decidi colocar os métodos relacionados a isso aqui mesmo. 
    def determinar_atributos(self, estilo):
        nomes_atributos = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]

        if estilo == "1":
            for atributo in nomes_atributos:
                dado = 0
                for _ in range(3):
                    dado += random.randint(1, 6)
                self.atributos[atributo] = dado

        elif estilo == "2":
            print(f"Os atributos são\n"
                "1\t-\tForça\n"
                "2\t-\tDestreza\n"
                "3\t-\tConstituição\n"
                "4\t-\tInteligência\n"
                "5\t-\tSabedoria\n"
                "6\t-\tCarisma\n...")
            escolhido = []
            for atributo in nomes_atributos:
                dado = 0
                for _ in range(3):
                    dado += random.randint(1, 6)

                while True:
                    escolha = int(input(
                    f"O dado rolou\t->\t{dado}\n"
                    "Quer colocar o valor em qual atributo?\t-> "))
                
                    #checagem e adição
                    if escolha in escolhido:
                        print("Você não pode repetir o mesmo atributo!")
                    else:
                        self.atributos[nomes_atributos[escolha - 1]] = dado
                        escolhido.append(escolha)
                        break

        elif estilo == "3":
            print(f"Os atributos são\n"
                    "1\t-\tForça\n"
                    "2\t-\tDestreza\n"
                    "3\t-\tConstituição\n"
                    "4\t-\tInteligência\n"
                    "5\t-\tSabedoria\n"
                    "6\t-\tCarisma\n...")
            escolhido = []
            for atributo in nomes_atributos:
                dado = 0
                numeros = []
                for _ in range(4):
                    num = random.randint(1,6)
                    numeros.append(num)

                valor = min(numeros)
                numeros.remove(valor)

                for numero in numeros:
                    dado += numero

                while True:
                    escolha = int(input(
                        f"O dado rolou\t->\t{dado}\n"
                        "Quer colocar o valor em qual atributo?\t-> "))
                    
                    #checagem e adição
                    if escolha in escolhido:
                        print("Você não pode repetir o mesmo atributo!")
                    else:
                        self.atributos[nomes_atributos[escolha - 1]] = dado
                        escolhido.append(escolha)
                        break

