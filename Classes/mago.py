from .classe import ClasseBase

class Mago(ClasseBase):
    def __init__(self):
        super().__init__("Mago", 0, 5)

        self.armas = ["pequenas"]
        self.armaduras = ["none"]
        self.itens_magicos = ["all"]
        self.habilidades = {
            "Magias arcanas": 1,
            "Ler magias": 1,
            "Detectar magias": 1
        }
