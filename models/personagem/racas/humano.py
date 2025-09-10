from .raca import RacaBase, Alinhamento, Visao

class Humano(RacaBase):
    def __init__(self):
        super().__init__(
            nome = "Humano",
            mobilidade = 9,
            alinhamento = Alinhamento.ALL,
            visao = Visao.NO
        )