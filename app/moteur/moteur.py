import requests

#------------test de base---------
url_base="http://0.0.0.0:5000/model/metadata"
results = requests.get(url=url_base)


def summarize(text):
    """ Fonction qui prend un texte en entrée (string)
        renvoie un resume (string)
    """
    text_input= [text, ]
    url_post="http://0.0.0.0:5000/model/predict"
    json_data= {"text":text_input}
    header={"accept": "application/json"}
    results_text= requests.post(url=url_post, headers=header, json=json_data)
    reponse=results_text.json()['summary_text']
    resume=' '.join(reponse)
    print(resume)

with open('text_long.txt') as f:
    contents = f.readlines()
    texte=contents[0]

summarize(texte)


