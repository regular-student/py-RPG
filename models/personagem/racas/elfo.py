from .raca import RacaBase, Alinhamento, Visao

class Elfo(RacaBase):
    def __init__(self):
        super().__init__(
            nome = "Elfo",
            mobilidade = 9,
            alinhamento = Alinhamento.NEUTRAL,
            visao = Visao.NO
        )