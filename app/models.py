from . import db
from .Config import Asset


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, title, content):
        self.title = title
        self.content = content


def add_blog_articles():
    if BlogPost.query.first() is not None:
        BlogPost.query.delete()
        db.session.commit()

    posts = [
        BlogPost(title="Cos'è un Asset e Quali Sono i Principali",
                 content="Un asset è qualsiasi risorsa che possiede un valore economico e che può essere posseduta "
                         "o controllata per produrre valore in futuro. Gli asset possono essere tangibili, come una "
                         "casa o un'auto, o intangibili, come un brevetto o un marchio.\n"
                         "I principali tipi di asset:\n"
                         "1. Asset Liquidi: Contante, conti correnti e di risparmio, investimenti a breve termine.\n"
                         "2. Asset Reali: Immobili, beni mobili, oggetti d'arte e da collezione.\n"
                         "3. Asset Finanziari: Azioni, obbligazioni, fondi comuni di investimento.\n"
                         "4. Asset Intangibili: Proprietà intellettuale, goodwill.\n"
                         "Conoscere e gestire i tuoi asset è cruciale per avere una buona salute finanziaria, ti "
                         "permette di pianificare il futuro, valutare la tua ricchezza e diversificare gli "
                         "investimenti."),

        BlogPost(title="Cos'è la Finanza Personale?",
                 content="La finanza personale riguarda la gestione delle tue finanze individuali, compresi reddito, "
                         "spese, risparmi, investimenti e pianificazione per il futuro. L'obiettivo è massimizzare il "
                         "benessere finanziario e raggiungere i tuoi obiettivi economici.\n"
                         "Elementi chiave della finanza personale:\n"
                         "1. Reddito: Include tutte le fonti di entrate come stipendi, redditi da investimenti, ecc.\n"
                         "2. Spese: Monitorare e gestire le uscite quotidiane e straordinarie.\n"
                         "3. Risparmio: Accumulare denaro per esigenze future o emergenze.\n"
                         "4. Investimenti: Far crescere il proprio capitale investendo in vari asset.\n"
                         "5. Pianificazione per il Futuro: Prepararsi per pensionamento, acquisto di casa, istruzione "
                         "dei figli, ecc.\n "
                         "Una buona gestione della finanza personale ti aiuta a raggiungere i tuoi obiettivi, "
                         "evitare il debito e affrontare le emergenze."),

        BlogPost(title="Cos'è un Ticker, ISIN e Valore?",
                 content="Un ticker è un simbolo unico composto da lettere che rappresenta una società quotata in "
                         "borsa. Ad esempio, il ticker di Apple Inc. è 'AAPL'.\n"
                         "L'ISIN (International Securities Identification Number) è un codice unico di 12 caratteri "
                         "alfanumerici che identifica specificamente un titolo a livello internazionale. Ad esempio, "
                         "l'ISIN di Apple è US0378331005.\n "
                         "Il valore di un titolo rappresenta il prezzo corrente al quale può essere acquistato o "
                         "venduto "
                         "sul mercato. È determinato dalla domanda e offerta tra acquirenti e venditori."),

        BlogPost(title="Perché è Importante Investire?",
                 content="Investire è importante per diversi motivi:\n"
                         "1. Crescita del Capitale: Gli investimenti possono aumentare il tuo patrimonio nel tempo.\n"
                         "2. Protezione dall'Inflazione: Gli investimenti possono aiutarti a mantenere il potere "
                         "d'acquisto.\n "
                         "3. Reddito Passivo: Gli investimenti come azioni e immobili possono generare reddito "
                         "regolare.\n "
                         "Per iniziare a investire, educati sulle basi dell'investimento, inizia con piccoli importi "
                         "e diversifica il tuo portafoglio."),

        BlogPost(title="Cos'è l'Interesse Composto?",
                 content="L'interesse composto è l'interesse calcolato sia sul capitale iniziale che sugli interessi "
                         "accumulati nel tempo. "
                         "È un potente strumento per far crescere i tuoi risparmi e investimenti.\n"
                         "Esempio: Se investi 1000€ con un interesse annuo del 5%, dopo un anno avrai 1050€. Nel "
                         "secondo anno, l'interesse sarà calcolato su 1050€, e così via.\n "
                         "L'interesse composto è importante perché permette una crescita esponenziale del capitale e "
                         "incentiva il risparmio."),

        BlogPost(title="Cos'è il Budgeting e Perché va Fatto?",
                 content="Il budgeting è il processo di pianificazione e gestione delle tue finanze personali, "
                         "decidendo in anticipo come allocare il tuo reddito.\n "
                         "Passaggi per creare un budget:\n"
                         "1. Calcola il Reddito Netto: Quanto guadagni al netto delle tasse.\n"
                         "2. Elenca le Spese Fisse: Affitto, mutuo, bollette, ecc.\n"
                         "3. Pianifica le Spese Variabili: Spesa alimentare, divertimenti, ecc.\n"
                         "4. Imposta Obiettivi di Risparmio: Decidi quanto vuoi risparmiare ogni mese.\n"
                         "5. Rivedi e Regola: Monitora il tuo budget e fai aggiustamenti necessari.\n"
                         "Il budgeting ti aiuta a tenere sotto controllo le tue finanze, ridurre lo stress "
                         "finanziario e raggiungere i tuoi obiettivi economici."),

        BlogPost(title="Come Creare un Budget Personale in 5 Semplici Passi",
                 content="Creare un budget personale è fondamentale per gestire le tue finanze. Ecco come farlo in 5 "
                         "semplici passi:\n "
                         "1. Calcola il tuo reddito mensile netto.\n"
                         "2. Elenca tutte le tue spese fisse mensili.\n"
                         "3. Stima le tue spese variabili mensili.\n"
                         "4. Imposta un obiettivo di risparmio mensile.\n"
                         "5. Monitora le tue spese e aggiusta il budget se necessario.\n"
                         "Un budget ti aiuta a capire dove vanno i tuoi soldi e come puoi risparmiare di più."),

        BlogPost(title="Risparmio Automatico: Perché e Come Iniziare Subito",
                 content="Il risparmio automatico è un metodo efficace per accantonare denaro senza pensarci troppo. "
                         "Ecco perché e come iniziare:\n"
                         "1. Vantaggi: Il risparmio automatico riduce la tentazione di spendere e ti aiuta a "
                         "costruire un fondo di emergenza.\n "
                         "2. Come Impostarlo: Puoi impostare trasferimenti automatici dal tuo conto corrente a un "
                         "conto di risparmio ogni mese.\n "
                         "3. Consigli: Inizia con piccole somme e aumenta gradualmente l'importo.\n"
                         "Il risparmio automatico è una strategia semplice ma potente per migliorare la tua "
                         "situazione finanziaria."),

        BlogPost(title="10 Modi per Risparmiare sui Tuoi Acquisti Quotidiani",
                 content="Risparmiare sui tuoi acquisti quotidiani è possibile con alcuni semplici accorgimenti:\n"
                         "1. Fai una lista della spesa e attieniti ad essa.\n"
                         "2. Confronta i prezzi online prima di acquistare.\n"
                         "3. Usa coupon e codici sconto.\n"
                         "4. Compra in grandi quantità per risparmiare.\n"
                         "5. Evita gli acquisti impulsivi.\n"
                         "6. Acquista prodotti di marca del supermercato.\n"
                         "7. Cerca offerte e promozioni.\n"
                         "8. Utilizza app per il cashback.\n"
                         "9. Paga in contanti per avere un maggiore controllo sulle spese.\n"
                         "10. Ripara e riutilizza invece di comprare nuovo.\n"
                         "Seguendo questi consigli, puoi risparmiare notevolmente senza rinunciare alla qualità."),

        BlogPost(title="Investire per Principianti: Dove e Come Iniziare",
                 content="Investire può sembrare complicato, ma ecco alcuni suggerimenti per iniziare:\n"
                         "1. Educati: Leggi libri, segui blog e partecipa a corsi online sulle basi "
                         "dell'investimento.\n "
                         "2. Inizia con Piccoli Importi: Non serve una grande somma per iniziare, anche piccole somme "
                         "possono crescere nel tempo.\n "
                         "3. Diversifica: Non mettere tutte le uova nello stesso paniere; investi in diversi tipi di "
                         "asset.\n "
                         "4. Usa Piattaforme Affidabili: Scegli piattaforme di investimento sicure e affidabili.\n"
                         "5. Monitora i Tuoi Investimenti: Tieni traccia delle performance e fai aggiustamenti se "
                         "necessario.\n "
                         "Investire può aiutarti a far crescere il tuo capitale e raggiungere i tuoi obiettivi "
                         "finanziari a lungo termine."),

        BlogPost(title="Cos’è un Fondo di Emergenza e Come Crearlo",
                 content="Un fondo di emergenza è un cuscinetto finanziario per affrontare spese impreviste. Ecco "
                         "come crearlo:\n "
                         "1. Definisci l’Importo: L’obiettivo è avere da tre a sei mesi di spese di vita coperte.\n"
                         "2. Apri un Conto Separato: Mantieni il fondo separato dal resto dei tuoi risparmi.\n"
                         "3. Risparmia Regolarmente: Imposta trasferimenti automatici verso il fondo ogni mese.\n"
                         "4. Non Utilizzarlo per Spese Non Essenziali: Usa il fondo solo per vere emergenze.\n"
                         "Avere un fondo di emergenza ti offre sicurezza e tranquillità finanziaria."),
    ]

    db.session.bulk_save_objects(posts)
    db.session.commit()


class Trade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(4), nullable=False)
    company = db.Column(db.Text, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String(10), nullable=False)

    def __init__(self, ticker, unit_price, quantity, date):
        self.ticker = ticker
        self.unit_price = unit_price
        self.quantity = quantity
        self.company = self.get_company_from_ticker()
        self.date = date
        self.type = self.get_type_from_ticker()

    def get_company_from_ticker(self):
        import yfinance as yf
        return yf.Ticker(self.ticker).info['shortName']

    def get_type_from_ticker(self):
        if self.ticker in Asset.STOCKS:
            return 'Stocks'
        else:
            if self.ticker in Asset.BONDS:
                return 'Bonds'
            else:
                if self.ticker in Asset.ETFS:
                    return 'ETFs'

