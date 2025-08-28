collegarlo con GIT 



Questo progetto base della documentazione:

step:
Inserire file di configurazione per i parametri visualizzati su web/file
Creare pagina di edit dei file MD
Processo di creazione pdf
processo di importazione api
processo di pubblicazione
processo di "version control"
processo di version diff checker


processo nuovo progetto

creare ENV  'python -m venv venv'
Accedere a env 'venv\Scripts\activate'
install material "pip install mkdocs-material"
installare i plugin 'pip install -r preConfiguration/requirements.txt'
nuovo progetto 'mkdocs new nome-progetto'


PRECONFIGURATION = personalizza il progetto

mkdocs template è il file yaml di mkdocs
config.json sono le variabili 
il file python permette di creare dinamicamente il file yaml di mkdocs
modificare nav-config.yml per personalizzare info sul progetto
Nella cartella docs/personalization modificare il file LOGO.png a seconda dell APP

Nella cartella docs inserire tutti i file md nominati come su nav-config.yml
Nella cartella docs/images inserire tutte le immagini da utilizzare

entrare nella folder
python preConfiguration/build_config.py
entrare nella folder
ng serve --proxy-config proxy.conf.json    





nella cartella md editor fare 

node editor/backend.js
ng serve --proxy-config proxy.conf.json