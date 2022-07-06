from flask import Flask, render_template, request
from app.BDD.bdd import add_entry_bdd,read_all_bdd, Message, init_bdd
from app.moteur.moteur import summarize

session = init_bdd()
# print('youpi')

app = Flask(__name__)

'''page d’accueil présentant l’entreprise WYM'''
@app.route("/home")
def home():
    return render_template("home.html")

'''quelques mots sur l’entreprise WYM, ses services,...'''
@app.route("/about")
def about():
    return render_template("about.html")

# '''page affichant le service de résumé de texte'''
# @app.route("/model")
# def model():
#     return render_template("model.html")

'''page affichant le service de résumé de texte'''
@app.route("/model", methods=["POST", "GET"])
def model():
    if request.method == "GET":
        return render_template("model.html")
    elif request.method == "POST":
        texte = request.form["texte"]
        nom = request.form["nom"]
        mail = request.form["mail"]
        tel = request.form["tel"]
        "Call AI"
        resume = summarize(texte)
        "Fill bdd"
        add_entry_bdd(session=session, nom=nom, mail=mail, tel=tel, texte=texte, resume=resume)
        read_all_bdd(session)
        return render_template("model.html", variable=resume)

# '''un joli formulaire de contact (nom, mail, téléphone (optionnel), message)'''
# @app.route("/contact")
# def contact():
#     return render_template("contact.html")

'''un joli formulaire de contact (nom, mail, téléphone (optionnel), message)'''
@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        nom = request.form["nom"]
        mail = request.form["mail"]
        tel = request.form["tel"]
        message = request.form["message"]
        # print(nom, mail, tel, message)
        "Fill bdd"
        add_entry_bdd(session=session, nom=nom, mail=mail, tel=tel, message=message)
        read_all_bdd(session)
        return render_template("contacted.html")
    

'''un petit message pour signaler à l’utilisateur que la soumission du
formulaire s’est effectuée de manière réussie'''
@app.route("/contacted")
def contacted():
    return render_template("contacted.html")

app.run(debug=True, host='0.0.0.0')

def main():
    pass

if __name__ == "__main__":
    main()