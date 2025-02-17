import streamlit as st
import math

from PIL import Image
logo_insubria = Image.open("Logoinsubria.png")
logo_manfredini = Image.open("Logo_Manfredini.png")

col1, col2 = st.columns(2)
with col1:
    st.image(logo_insubria, width=150)
with col2:
    st.image(logo_manfredini, width=150)

add_sidebar = st.sidebar.selectbox('Menu',('Benvenuti','Introduzione','Il nostro progetto','Analisi dati','Previsione spesa totale'))

if add_sidebar == 'Benvenuti':
    st.title('Benvenuti')

    #informazioni personali
    name= st.text_input('Inserisci il tuo nome: ')
    if name:
    	st.write(f'ciao, {name}!')

    age = st.slider('quanti anni hai?',min_value=0, max_value=100,value=25)
    st.write(f'la tua età è: {age}')

    agree = st.checkbox("sei d'accordo con i termini?")
    if agree:
        st.write("grazie per aver accettato i termini!")


if add_sidebar =='Introduzione':
    # introduzione (a cosa serve il sito)
    st.title('A cosa serve questa web app?')
    st.write('Grazie a questa web app è possibile fare una previsione sulla spesa totale di una famiglia in un anno, inserendo diverse variabili.')
    st.title("Cos'è la statistica?")
    testo= """

    La statistica è la scienza che ha per oggetto lo studio dei fenomeni collettivi suscettibili di misurazione e di descrizione quantitativa, basandosi sulla raccolta di un grande numero di dati inerenti ai fenomeni in esame, e partendo da ipotesi più o meno direttamente suggerite dall’esperienza o da analogie con altri fenomeni già noti, mediante l’applicazione di metodi matematici fondati sul calcolo delle probabilità, si perviene alla formulazione di leggi di media che governano tali fenomeni, dette leggi statistiche. Spesso la raccolta dei dati viene limitata a un campione più ristretto, opportunamente predeterminato in modo da rappresentare il più fedelmente possibile le caratteristiche generali.

    Le tecniche della statistica trovano applicazione nelle altre scienze sperimentali, in particolare nell’analisi statistica dei dati, sia in riferimento alla natura aleatoria (quindi casuale) dei risultati delle misure, in quanto affetti da errori, sia in presenza di fenomeni intrinsecamente aleatori per cui le proprietà dei fenomeni studiati devono essere dedotte, attraverso un procedimento di inferenza statistica, dalle proprietà di un campione
    statistico, costituito dagli eventi effettivamente osservati.Le applicazioni della statistica sono principalmente nella demografia, che studia la popolazione umana (ammontare e composizione), nella fisica, che studia la meccanica classica e quantistica, nell’economia, in particolare nell’econometria, e nella biostatica e medicina, che traduce i dati clinici e di laboratorio in espressioni quantitative.

    I fenomeni statistici si dividono in qualitativi, che si identificano tramite attributi e che si misurano tramite le scale nominali (senza ordinamento) e le scale ordinali (in ordine naturale), e in quantitativi, che si identificano tramite numeri e che possono essere discreti (numeri naturali) o continui (numeri reali).La dimensione temporale/spaziale può essere cross-sectional (dati di un preciso istante temporale), longitudinal (stesso soggetto in differenti momenti) o panel (dati di differenti stati temporali).La copertura del dato può essere amministrativo (raccolto sulla totalità della popolazione) o da indagine o survey (raccolto su una parte della popolazione).

    """

    st.markdown(testo)
if add_sidebar =='Il nostro progetto':
    #piccola spiegazione del progetto
    st.title('Chi siamo')
    testo = """
    Ciao! Noi siamo dei ragazzi di terza liceo scientifico, e grazie al Prof riganti, professore di economia dell'università Insubria, e il Prof Sinatra, nostro docente di fisica e matematica, abbiamo programmato questa web app per fare una previsione sulla spesa totale di un cittadino italiano. Qui trovate tutti i passaggi del nostro progetto:

    Siamo stati introdotti alla base della statistica dal Prof. Riganti e abbiamo fatto una ricerca sulle variazioni dei prezzi al consumo delle principali 12 categorie di spesa. Queste variazioni sono state studiate con i dati presi durante gli anni del 2019, 2020, 2021, e 2022.La ricerca è stata svolta cercando i report dell’ISTAT sia manualmente, sia con l’aiuto dell’intelligenza artificiale, una volta raccolti tutti i report sono stati letti e studiati. Siamo stati successivamente introdotti a Python, un linguaggio di programmazione facile e molto vario con il quale si possono analizzare dati e programmare applicazioni. Abbiamo imparato poi cosa sono Numpy e Pandas caricando dei dataset: sono un open source contenente i metodi per analizzare i dati.Come ultimo passaggio abbiamo visualizzato i dati di un dataset contenente informazioni di più di centomila famiglie. Sono raccolte in una tabella excel, dove le righe rappresentano le famiglie e le colonne le tipologie dei dati, in particolare: il reddito (valutato in decile), l’ampiezza del nucleo familiare, l’eventuale presenza di minori o anziani, le caratteristiche della casa in cui abitano, come ad esempio la metratura e il numero di stanze, e le spese divise nelle 12 categorie principali.Dopo aver appreso come produrre le varie tipologie di grafici abbiamo svolto un’indagine sul notebook “colab” nel quale, dopo aver inserito i dati dalle nostre librerie, sono stati sviluppati numerosi grafici per un'analisi univariata e un'analisi multivariata. Queste analisi ci sono state utili per osservare delle correlazioni tra dei valori, seppur piccole.Molti di questi grafici sono stati scartati per poi analizzare e commentare quelli con il risultato più interessante, confrontandoli con ciò che avevamo appreso dai report.

    Il giorno seguente il Prof Riganti ci ha introdotto come prevedere una spesa in base a quali variabili, che possono essere continue e discrete, si consideravano. Ci ha spiegato come costruire un grafico, nel quale poi viene inserita una retta. Grazie a questa retta, bisettrice rappresentante la linea normale, tramite calcoli complessi basati sulla distanza punto retta possiamo determinare l’R2. l’R2 è un coefficiente il  cui valore è compreso tra 0 e 1, che ci dice quanto il nostro grafico è preciso. Più l’R2 è vicino a 1, più il grafico sarà preciso. In seguito abbiamo appreso come disegnare questi grafici in Colab. Abbiamo fatto diverse prove, cambiando la variabile spesa nel target e le variabili predittive, fino a trovare l’R2 più vicino a 1 possibile.

    """

    st.markdown(testo)

if add_sidebar == 'Analisi dati':
    st.title('Report finale')
    testo = """
    Alla fine del nostro progetto abbiamo fatto un report contenente i nostri grafici e le nostre analisi.

    Qui sotto trovate il link per vedere il report:
    """
    st.markdown(testo)
    st.markdown("[Clicca qui per visitare il report](https://github.com/Giuseppe86-lab/PCTO_Div_Riz_San/blob/main/Report_grafici_PCTO.pdf)")

if add_sidebar =='Previsione spesa totale':
    #calcolo spesa tolare
    componenti= st.number_input('Inserisci il numero di componenti della tua famiglia: ')
    if componenti:
	    st.write(f'Il numero di componenti della tua famiglia è: {componenti}!')


    decile_di_reddito = int(st.slider('qual è il tuo decile di reddito?',min_value=1, max_value=10,value=5))
    st.write(f'il tuo decile di reddito è: {decile_di_reddito}')

    st.write('0 = nessuna crisi \n'
    '1 = crisi moderata \n'
    '2 = crisi grave \n')
    crisi= st.number_input('è in corso una crisi economica?')

    num1 = st.number_input("Inserisci la tua spesa in prodotti alimemtari e bevande analcoliche:", value=0.0)
    num1 = math.log(num1+1)

    num2 = st.number_input("Inserisci la tua spesa in bollette:", value= 0.0)
    num2 = math.log(num2+1)

    intercetta= 2.47
    coeff1= 0.03
    coeff2= 0.06
    coeff3= 0.03
    coeff4= 0.21
    coeff5= 0.54

    st.write('Previsione spesa totale:')
    if st.button("Calcola_previsione"):
	    result=math.exp(intercetta+coeff1*componenti+coeff2*decile_di_reddito+coeff3*crisi+coeff4*num1+coeff5*num2)
	    st.success(f"la previsione è: {result}")


