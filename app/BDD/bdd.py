# sudo docker run --name db -e POSTGRES_PASSWORD=password -e POSTGRES_USER=admin -p 5432:5432 -d -v /home/vincent.faure@Digital-Grenoble.local/Documents/chat/BDD/:/var/lib/postgresql/data postgres

from requests import session
from sqlalchemy import Integer, create_engine  
from sqlalchemy import Column, String
import sqlalchemy  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker




# Définition de la classe de l'objet enregistrer dans la base de donnée
Base = declarative_base()
class Message(Base):
    __tablename__ = 'Message'

    id = Column(Integer, primary_key = True)
    nom = Column(String)
    mail = Column(String)
    tel = Column(String)
    message = Column(String)
    texte = Column(String)
    resume = Column(String)

    def __str__(self):
        message = f"id = {self.id},\nnom = {self.nom},\nmail = {self.mail},\ntel = {self.tel},\nmessage = {self.message},\ntexte = {self.texte},\nresume = {self.resume}\n\n"
        return message




def init_bdd():
    Base = declarative_base()
    # Postgres username, password, and database name
    POSTGRES_ADDRESS = 'db' ## INSERT YOUR DB ADDRESS IF IT'S NOT ON PANOPLY
    POSTGRES_PORT = '5432'
    POSTGRES_USERNAME = 'admin'
    POSTGRES_PASSWORD = 'password'
    POSTGRES_DBNAME = 'postgres'
    # A long string that contains the necessary Postgres login information
    postgres_str = ('postgresql+psycopg2://{username}:{password}@{ipaddress}:{port}/{dbname}'.format(
        username=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        ipaddress=POSTGRES_ADDRESS,
        port=POSTGRES_PORT,
        dbname=POSTGRES_DBNAME))
    # Create the connection
    # print(postgres_str)
    db = create_engine(postgres_str)

    # Connection à la base de donnée
    Session = sessionmaker(db)  
    session = Session()


    # Vérification de l'existence de la base de donnée
    if not sqlalchemy.inspect(db).has_table('Message'):
        Base.metadata.create_all(db)
        session.commit()

    # print('truc')

    return session



def add_entry_bdd(session, nom, mail, tel="", message="", texte="", resume=""):
    '''
    add_entry_bdd permet d'ajouter une entrée à la base de donnée\n
    Input:  
        * nom, mail, tel, message, texte, resume corespond au donnée du formulaire
    '''
    # Create 
    entry = Message(nom=nom, mail=mail, tel=tel, message=message, texte=texte, resume=resume)  
    session.add(entry)  
    session.commit()

def read_all_bdd(session):
    '''
    read_all_bdd affiche la totalité de la base de donnée dans le terminal
    '''
    # Read
    messages = session.query(Message)  
    for message in messages:  
        print(message)

# read_all_bdd()



# https://www.compose.com/articles/using-postgresql-through-sqlalchemy/




