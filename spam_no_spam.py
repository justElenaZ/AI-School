# 1. Carichiamo i dati di esempio (messaggi SMS)
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dati: una lista di messaggi e le relative etichette (spam o no)
messaggi = [
    "Ciao, come stai?",
    "Hai vinto un premio! Clicca qui per ritirarlo",
    "Ci vediamo domani?",
    "Offerta imperdibile: sconto del 90%! Compra ora!",
    "Chiamami appena puoi",
    "Accedi subito al tuo conto: clicca qui",
    "Ti aspetto alle 8",
    "Guadagna soldi facili da casa, scopri come!"
]
etichette = [
    "ham",  # non spam
    "spam",
    "ham",
    "spam",
    "ham",
    "spam",
    "ham",
    "spam"
]

# 2. Trasformiamo il testo in numeri (il computer capisce solo numeri!)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messaggi)
y = etichette

# 3. Dividiamo i dati in "addestramento" e "test"
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Alleniamo un modello di Machine Learning
model = MultinomialNB()
model.fit(X_train, y_train)

# 5. Proviamo a classificare nuovi messaggi
nuovi_messaggi = [
    "Complimenti, hai vinto una vacanza gratis!",
    "Puoi venire a studiare da me stasera?"
]
X_nuovi = vectorizer.transform(nuovi_messaggi)
previsioni = model.predict(X_nuovi)

for msg, pred in zip(nuovi_messaggi, previsioni):
    print(f"Messaggio: '{msg}' --> Classificato come: {pred}")

# 6. Facciamo vedere quante risposte corrette dà su quelli di test
score = model.score(X_test, y_test)
print(f"\nAccuratezza del modello sui dati di test: {score:.2f}")
