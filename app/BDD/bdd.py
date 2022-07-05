# sudo docker run --name db -e POSTGRES_PASSWORD=password -e POSTGRES_USER=admin -p 5432:5432 -d -v /home/vincent.faure@Digital-Grenoble.local/Documents/chat/BDD/:/var/lib/postgresql/data postgres

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData


class User:
    def __init__(self, nom, mail, tel="", message="", texte="", resume=""):
        self.nom = nom
        self.mail = mail
        self.message = message
        self.tel = tel
        self.texte = texte
        self.resume = resume


# Postgres username, password, and database name
POSTGRES_ADDRESS = '0.0.0.0' ## INSERT YOUR DB ADDRESS IF IT'S NOT ON PANOPLY
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
print(postgres_str)
db = create_engine(postgres_str)

meta = MetaData(db)
database = Table('user', meta,  
                       Column('nom', String),
                       Column('mail', String),
                       Column('tel', String),
                       Column('message', String),
                       Column('texte', String),
                       Column('resume', String))

with db.connect() as conn:

    # database.create() # METTRE UN IF TABLE EXIST ....
    insert_statement = database.insert().values(nom="Doctor Strange2", mail="doctor.strange2@doctor.com")
    conn.execute(insert_statement)

    # Read
    select_statement = database.select()
    result_set = conn.execute(select_statement)
    for r in result_set:
        print(r)

