# app.py

from flask import Flask, render_template, request, redirect, session, url_for
from models.personagem import (
    Personagem,
    Guerreiro,
    Mago,
    Clerigo,
    Humano,
    Elfo,
    Halfling,
)
from services.distribuicao_atributos import distribuir_classico, rolar_dados_aventureiro, rolar_dados_heroico

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
        session["personagem_info"] = {
            "classe_id": classe_id,
            "raca_id": raca_id,
            "estilo": estilo
        }
        
        if estilo == "1":
            atributos_base = distribuir_classico()
            personagem_info = session.pop("personagem_info", None)
            
            classe_escolhida = CLASSES.get(personagem_info["classe_id"])
            raca_escolhida = RACAS.get(personagem_info["raca_id"])
            
            personagem = Personagem(raca_escolhida, classe_escolhida, atributos_base)
            return render_template("personagem.html", personagem=personagem)
        
        elif estilo == "2":  # Aventureiro
            valores = rolar_dados_aventureiro()
            session['valores_rolados'] = valores
            return redirect(url_for('distribuir_atributos'))

        elif estilo == "3":  # Heróico
            valores = rolar_dados_heroico()
            session['valores_rolados'] = valores
            return redirect(url_for('distribuir_atributos'))
        
        if not classe_escolhida or not raca_escolhida:
            # Lida com uma escolha inválida
            return render_template(
                "criar_personagem.html", erro="Opção de classe ou raça inválida!"
            )
            
    return render_template("criar_personagem.html")

@app.route("/distribuir-atributos", methods=["GET", "POST"])
def distribuir_atributos():
    if 'personagem_info' not in session or 'valores_rolados' not in session:
        return redirect(url_for("criar_personagem"))

    valores = session['valores_rolados']
    info = session['personagem_info']

    if request.method == "POST":
        nomes_atributos = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]
        atributos = {}
        valores_usados_do_form = [int(v) for v in request.form.values()]

        if sorted(valores_usados_do_form) != sorted(valores):
            erro_msg = "Valores inválidos. Por favor, use apenas os valores rolados, sem repetição."
            titulo = "Aventureiro" if info.get('estilo') == "2" else "Heróico"
            return render_template("distribuir_atributos.html", valores=valores, titulo=titulo, erro=erro_msg)

        for nome in nomes_atributos:
            atributos[nome] = int(request.form.get(nome))

        classe = CLASSES.get(info['classe_id'])
        raca = RACAS.get(info['raca_id'])
        personagem = Personagem(raca, classe, atributos)

        session.pop('personagem_info')
        session.pop('valores_rolados')

        return render_template("personagem.html", personagem=personagem)

    estilo = info.get('estilo')
    titulo = "Aventureiro" if estilo == "2" else "Heróico"
    return render_template("distribuir_atributos.html", valores=valores, titulo=titulo)

if __name__ == "__main__":
    app.run(debug=True)