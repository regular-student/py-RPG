from .classe import ClasseBase

class Clerigo(ClasseBase):
    def __init__(self):
        super().__init__("Clérigo", 1, 5)

        self.armas = ["impactantes"]
        self.armaduras = ["all"]
        self.itens_magicos = ["all"]
        self.habilidades = {
            "Magias divinas": 1,
            "Afastar mortos-vivos": 1,
            "Cura milagrosa": 1
        }
