from abc import ABC, abstractmethod

class ClasseBase(ABC):
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida_base = vida
        self.ataque_base = ataque
        self.armas = []
        self.armaduras = []
        self.habilidades = {}

    def exibir_habilidades(self):
        print(f"\t\t--> Habilidades <--\t\t\n")
        if not self.habilidades:
            print("Nenhuma habilidade definida.")
        else:
            for habilidade, descricao in self.habilidades.items():
                print(f"{habilidade}: {descricao}")
        print("\n" * 2)
    
