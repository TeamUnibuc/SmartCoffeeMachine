# Scopul Aplicației

Scopul final al proiectului este un aparat de cafea inteligent care va economisi timpul utilizatorilor. Făcând un “working backwards” de la nevoile acestora (vor să-și primească băutura cât mai rapid), am analizat și descoperit etape ce pot fi optimizate.

# Obiectivele aplicației

Obiectivul aplicației este un aparat de cafea inteligent, capabil să recunoască persoana care vrea să-l folosească, și să-i ofere un set de băuturi preconfigurate (tipul de băutura, mărimea, cantitatea de zahăr) în baza unor preferințe setate sau ale istoricului utilizatorului. În acest mod, utilizatorul nu mai cheltuie timp, alegând el setările.

# Grupuri țintă

Grupul nostru țintă sunt oamenii care își vor băutura făcută la fel de fiecare dată și cât mai rapid.

## Minimal Viable Product

Întrucât partea esențială este maparea consumator - recomandare de băuturi, modul în care se recunoaște consumatorul este pe plan secundar. Astfel, MVP-ul este un aparat de cafea care poate primi un identificator al unui utilizator și să ofere lista de băuturi recomandate.

## Cerințe suplimentare

1. Aparatul recunoaște (facial / vocal / etc.) consumatorul. (funcțional)
1. Utilizatorul poate trimite o lista de preferințe către aparat (funcțional)
1. Aparatul actualizează recomandările în baza istoricului utilizatorului (funcțional)
1. Workflow-ul aparatului este rapid (non-funcțional)
1. Aparatul are o baza de date cu utilizatori, bauturi, și recomandări (funcțional)
1. Aparatul anunță când trebuie făcut aprovizionare la consumabile (cafea, zahăr, ceai) (funcțional)
1. Aparatul poate da o lista de “cele mai populare băuturi” în baza istoricului tuturor utilizatorilor (funcțional)

## Cerințe de development

### Stocarea datelor:
1. Crearea bazei de date
1. Creare utilizatorilor cu permisiunile minime necesare pentru administrarea bazei de date

### Comunicare:
1. Creare endpoint-urile de API

### Procesarea datelor:
1. Implementarea funcțiilor ce administrarea căile API-ului
