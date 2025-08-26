from classe import ClasseBase

class Guerreiro(ClasseBase):
    def __init__(self):
        super().__init__("Guerreiro", 10, 1)

        self.armas = ["all"]
        self.armaduras = ["all"]
        self.itens_magicos = ["Pergaminho de protecao"]
        self.habilidades = {
            "Maestria em arma": 1,
            "Aparar": 1,
            "Ataque extra": 6
        }
