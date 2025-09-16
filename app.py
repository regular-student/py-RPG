# app.py

from flask import Flask, render_template, request, redirect, url_for
from models.personagem import (
    Personagem,
    Guerreiro,
    Mago,
    Clerigo,
    Humano,
    Elfo,
    Halfling,
)
from services.distribuicao_atributos import determinar_atributos

app = Flask(__name__)
app.config["SECRET_KEY"] = "sua-chave-secreta-aqui"  # Não sei ainda

# Dicionários
CLASSES = {"1": Guerreiro, "2": Mago, "3": Clerigo}

RACAS = {"1": Humano, "2": Elfo, "3": Halfling}


@app.route("/")
def index():
    return redirect(url_for("criar_personagem"))


@app.route("/criar", methods=["GET", "POST"])
def criar_personagem():
    if request.method == "POST":
        # Pega os dados do formulário
        classe_id = request.form.get("classe")
        raca_id = request.form.get("raca")
        estilo = request.form.get("estilo")

        # Seleciona a classe e raça com base na escolha
        classe_escolhida = CLASSES.get(classe_id)
        raca_escolhida = RACAS.get(raca_id)

        if not classe_escolhida or not raca_escolhida:
            # Lida com uma escolha inválida
            return render_template(
                "criar_personagem.html", erro="Opção de classe ou raça inválida!"
            )

        atributos_base = determinar_atributos(estilo)

        personagem = Personagem(raca_escolhida, classe_escolhida, atributos_base)

        return render_template("personagem.html", personagem=personagem)

    return render_template("criar_personagem.html")


if __name__ == "__main__":
    app.run(debug=True)
