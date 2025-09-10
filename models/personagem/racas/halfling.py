from .raca import RacaBase, Alinhamento, Visao

class Halfling(RacaBase):
    def __init__(self):
        super().__init__(
            nome = "Halfling",
            mobilidade = 6,
            alinhamento = Alinhamento.NEUTRAL,
            visao = Visao.NO
        )