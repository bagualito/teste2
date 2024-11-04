from flask import Flask, render_template
app = Flask (__name__)

# criar a primeira pagina do site
# toda pagina sempre tem um route e uma função, o route seria o caminho que voce precisa passar para chegar a aquela pagina
# route -> meuprimeirosite.com/
# função -> oque voce quer exibir na pagina
# para editar o site aprender html e css
# criar route, função e template
# estudar mais sobre o flask

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template('contatos.html')

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku



