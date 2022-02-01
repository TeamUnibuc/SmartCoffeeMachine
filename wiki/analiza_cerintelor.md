# Analiza Cerintelor

## Scopul Aplicației

Scopul final al proiectului este dezvoltarea softului unui aparat de cafea inteligent care va economisi timp utilizatorilor.
Făcând un “working backwards” de la nevoile acestora (vor să-și primească băutura cât mai rapid), am analizat și descoperit etape ce pot fi optimizate.

## Obiectivele aplicației

Obiectivul aplicatiei este de-a transforma aparatele de cafea dintr-o cladire de birouri / spatiu public intr-un network inteligent de aparate interconectate. Obiectivele finale ale aplicatiei sunt:

 * Vizibilitatea masinilor de cafea conectate la retea.
 **Nota:** Deoarece folosim un broker hostat pe internet, conexiunea functioneaza indiferent de retea, dar efectul dorit este atins daca brokerul se afla intr-o retea locala.

 * Aparatele de cafea dau posibilitatea utilizatorilor sa isi faca cafele.
 
 * Istoric centralizat (de la toate aparatele) de ce bauturi au fost comandate.
  
 * Recomandari de bauturi in dependenta de popularitate

 * Administratorul poate aduga / scoate retete de bauturi

 * Vizibilitatea nivelului consumabilelor

## Grupuri țintă

Grupul tinta sunt corporatiile mari, care dispun de zeci daca nu sute de aparate de cafea imprastiate in birouri, si al caror mentenanta necesita mult efort.

## Minimal Viable Product

MVP-ul consta din:
 * Un server central, capabil sa comunice cu lumea exterioara prin HTTP, si cu aparatele de cafea prin MQTT
 * Aparatul de cafea, capabil sa:
    * Anunte regulat care sunt nivele de resurse ale aparatului catre server.
    * Este capabil sa serveasca cafea bazandu-se pe o lista de retete salvate intern.

## Cerințe suplimentare

1. Utilizatorul poate trimite o lista de preferințe către aparat (funcțional)
1. Aparatul actualizează recomandările în baza istoricului utilizatorului (funcțional)
1. Workflow-ul aparatului este rapid (non-funcțional)
1. Aparatul anunță când trebuie făcut aprovizionare la consumabile (cafea, zahăr, ceai) (funcțional)
1. Aparatul poate da o lista de “cele mai populare băuturi” în baza istoricului tuturor utilizatorilor (funcțional)

## Cerințe de development

### Stocarea datelor

Fiecare masina de cafea isi tine lista retetelor in memory. 

Serverul central are o baza de date, unde isi salveza lista retetelor si istoricul comenzilor care au fost facute la oricare dintre aparate.

Datele masinilor de cafea se sincronizeaza automat cu serverul central, si serverul central poate fi alterat numai de persone autorizate (care detin un token hardcodat in server) prin HTTP.

### Comunicare

Pentru comunicare, trebuie puse la punct:
 1. Topicurile MQTT pe care le folosesc aparatele de cafea.
 2. API-ul folosit de serverul central.

### Procesarea datelor

1. Implementarea funcțiilor ce administreaza căile API-ului
