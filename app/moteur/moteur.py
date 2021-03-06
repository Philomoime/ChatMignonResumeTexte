"""
sudo docker pull codait/max-text-summarizer

sudo docker run -it -d -p 5001:5000 quay.io/codait/max-text-summarizer

"""

import requests

#------------test de base---------
url_base="http://moteur:5000/model/metadata"
results = requests.get(url=url_base)

#------------Fonction qui fabrique le résumé-------------
def summarize(text):
    """ Fonction qui prend un texte en entrée (string)
        renvoie un resume (string)
    """
    text_input= [text, ]
    url_post="http://moteur:5000/model/predict"
    json_data= {"text":text_input}
    header={"accept": "application/json"}
    results_text= requests.post(url=url_post, headers=header, json=json_data)
    reponse=results_text.json()['summary_text']
    # print(reponse)
    resume=' '.join(reponse)
    return resume 

# #-----------Lecture d'un texte--------------------------
# with open('text_long.txt') as f:
#     contents = f.readlines()
#     texte=contents[0]

# #-----------Appel de la fonction crée-----------------------
# summarize(texte)


