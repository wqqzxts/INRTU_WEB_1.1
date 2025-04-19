from flask import Flask, render_template

app = Flask(__name__)

nav = [
    { "title": "Главная", "URL": "/main" },
    { "title": "Мидорима", "URL": "/midorima" },
    { "title": "Мурасакибара", "URL": "/murasakibara" },
    { "title": "Ханамия", "URL": "/hanamiya" },
    { "title": "Глоссарий", "URL": "/glossarium" },
    { "title": "Автор", "URL": "/author" },
]

@app.context_processor
def global_context():
    return {
        "nav": nav
    }

@app.route("/main")
def main():
    return render_template("pages/main.html", name = "Главная")

@app.route("/midorima")
def midorima():
    return render_template("pages/midorima.html", name = "Мидорима")

@app.route("/murasakibara")
def murasakibara():
    return render_template("pages/murasakibara.html", name = "Мурасакибара")

@app.route("/hanamiya")
def hanamiya():
    return render_template("pages/hanamiya.html", name = "Ханамия")

@app.route("/glossarium")
def glossarium():
    return render_template("pages/glossarium.html", name = "Глоссарий")

@app.route("/author")
def author():
    return render_template("pages/author.html", name = "Автор")