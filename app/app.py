import BDD
import moteur
from flask import Flask, render_template

app = Flask(__name__)

'''page d’accueil présentant l’entreprise WYM'''
@app.route("/home")
def home():
    return render_template("home.html")

'''quelques mots sur l’entreprise WYM, ses services,...'''
@app.route("/about")
def about():
    return render_template("about.html")

'''page affichant le service de résumé de texte'''
@app.route("/model")
def model():
    return render_template("model.html")

'''un joli formulaire de contact (nom, mail, téléphone (optionnel), message)'''
@app.route("/contact")
def contact():
    return render_template("contact.html")

'''un petit message pour signaler à l’utilisateur que la soumission du
formulaire s’est effectuée de manière réussie'''
@app.route("/contacted")
def contacted():
    return render_template("contacted.html")

app.run()
