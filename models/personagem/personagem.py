class Personagem:
    def __init__(self, raca, classe, atributos):
        self.raca = raca()
        self.classe = classe()
        self.atributos = atributos
        self.atributos["XP"] = 0 # XP inicial

        # bônus raciais
        bonus_raciais = self.raca.bonus() if hasattr(self.raca, 'bonus') else {}
        for atributo, bonus in bonus_raciais.items():
            if atributo in self.atributos:
                self.atributos[atributo] += bonus

    def __str__(self):
        base = (
            f"\t\t--> Atributos <--\t\t\n"
            f"FOR:\t{self.atributos.get('forca', 0)}\n"
            f"DES:\t{self.atributos.get('destreza', 0)}\n"
            f"CON:\t{self.atributos.get('constituicao', 0)}\n"
            f"INT:\t{self.atributos.get('inteligencia', 0)}\n"
            f"SAB:\t{self.atributos.get('sabedoria', 0)}\n"
            f"CAR:\t{self.atributos.get('carisma', 0)}\n\n"
            f"\t\t--> {getattr(self.raca, 'nome', 'Raça Desconhecida')} <--\t\t\n"
            f"MOB:\t{getattr(self.raca, 'mobilidade', 0)}\n"
            f"VISÃO:\t{getattr(self.raca, 'visao', 'N/A').value if hasattr(self.raca, 'visao') else 'N/A'}\n"
            f"ALINH:\t{getattr(self.raca, 'alinhamento', 'N/A').value if hasattr(self.raca, 'alinhamento') else 'N/A'}\n\n"
            f"\t\t--> {self.classe.nome} <--\t\t\n"
            f"VIDA:\t{self.classe.vida_base}\n"
            f"ATAQUE:\t{self.classe.ataque_base}\n"
        )
        return base