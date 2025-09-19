from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Banco de dados simples em memória
alunos = [
    {"id": 1, "nome": "Maria", "nota": 8.5},
    {"id": 2, "nome": "João", "nota": 7.0}
]

@app.route("/")
def index():
    return render_template("index.html", alunos=alunos)

@app.route("/aluno/<int:id>")
def aluno(id):
    for a in alunos:
        if a["id"] == id:
            return render_template("aluno.html", aluno=a)
    return "Aluno não encontrado", 404

@app.route("/adicionar", methods=["POST"])
def adicionar():
    nome = request.form["nome"]
    nota = float(request.form["nota"])
    novo = {"id": len(alunos) + 1, "nome": nome, "nota": nota}
    alunos.append(novo)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
