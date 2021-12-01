# Scopul Aplicației

Scopul final al proiectului este dezvoltarea softului unui aparat de cafea inteligent care va economisi timp utilizatorilor.
Făcând un “working backwards” de la nevoile acestora (vor să-și primească băutura cât mai rapid), am analizat și descoperit etape ce pot fi optimizate.

# Obiectivele aplicației

Obiectivul aplicatiei este de-a transforma aparatele de cafea dintr-o cladire de birouri / spatiu public intr-un network inteligent de aparate interconectate. Obiectivele finale ale aplicatiei sunt:
 * Nivelul de apa / lapte / cafea / zahar din fiecare aparat de cafea poate fi privit online cu ajutorul unor requesturi HTTP trimise controllerului aparatelor de cafea.
 * Administratorul sa poata observa statistici despre folosirea cafelelor, cum ar fi histograme ale folosirii pe zi / aparat de cafea.
 * Administratorul poate instala o masina de cafea noua doar conectand-o la retea, aceasta conectandu-se si configurand singura setarile inpuse de administrator.
 * Administratorul poate adauga / modifica / sterge retete si bauturi de cafea, cum ar fi cantitatea de zahar, apa, cafea, lapte etc.
 * Administratorul poate edita meniul principal al aparatelor de cafea, propunand de exemplu "bautura zilei", sau anunturi.
 * Administratorul poate seta setari generale ale aparatului de cafea, cum ar fi temperatura la care aceasta este tinuta calda, daca aparatul face sau nu beep cand apesi pe butoane etc.

# Grupuri țintă

Grupul tinta sunt corporatiile mari, care dispun de zeci daca nu sute de aparate de cafea imprastiate in birouri, si al caror mentenanta necesita mult efort.

## Minimal Viable Product

MVP-ul consta din:
 * Un server central, capabil sa comunice cu lumea exterioara prin HTTP, si cu aparatele de cafea prin MQTT
 * Aparatul de cafea, capabil sa:
    * Anunte regulat care sunt nivele de resurse ale aparatului catre server.
    * Este capabil sa serveasca cafea bazandu-se pe o lista de retete salvate intern.

## Cerințe suplimentare

1. Aparatul recunoaște (facial / vocal / etc.) consumatorul. (funcțional)
1. Utilizatorul poate trimite o lista de preferințe către aparat (funcțional)
1. Aparatul actualizează recomandările în baza istoricului utilizatorului (funcțional)
1. Workflow-ul aparatului este rapid (non-funcțional)
1. Aparatul are o baza de date cu utilizatori, bauturi, și recomandări (funcțional)
1. Aparatul anunță când trebuie făcut aprovizionare la consumabile (cafea, zahăr, ceai) (funcțional)
1. Aparatul poate da o lista de “cele mai populare băuturi” în baza istoricului tuturor utilizatorilor (funcțional)

## Cerințe de development

### Stocarea datelor

Fiecare masina de cafea isi tine o micro-baza de date, cu lista retetelor, intr-un low-memeory db (see [this](https://stackoverflow.com/questions/47233562/key-value-store-in-python-for-possibly-100-gb-of-data-without-client-server)).

Serverul central are o baza de date mai complexa, unde isi salveza statistici despre masinile de cafea, si eventuri.

Datele masinilor de cafea se sincronizeaza automat cu serverul central, si serverul central poate fi alterat numai de persone autorizate (care detin un token hardcodat in server) prin HTTP.

### Comunicare

Pentru comunicare, trebuie puse la punct:
 1. Topicurile MQTT pe care le folosesc aparatele de cafea.
 2. API-ul folosit de serverul central.

### Procesarea datelor

1. Implementarea funcțiilor ce administrarea căile API-ului
