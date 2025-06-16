import random

# Dizionario di parole chiave e risposte possibili
rules = {
    "problema": [
        "Mi parli di più di questo problema.",
        "Da quanto tempo ha questo problema?",
        "Pensa che questo problema dipenda da qualcuno in particolare?"
    ],
    "madre": [
        "Mi parli di sua madre.",
        "Che rapporto ha con sua madre?"
    ],
    "padre": [
        "Mi parli di suo padre.",
        "Che rapporto ha con suo padre?"
    ],
    "triste": [
        "Mi racconti perché si sente triste.",
        "Da quanto tempo si sente triste?"
    ],
    "solo": [
        "Perché si sente solo?",
        "Vorrebbe non sentirsi solo?"
    ],
}

# Risposte generiche se nessuna parola chiave viene trovata
default_responses = [
    "Per favore, continui...",
    "Interessante. Mi dica di più.",
    "Capisco. Può spiegare meglio?",
    "Come si sente a riguardo?"
]

def find_keyword(sentence):
    for keyword in rules:
        if keyword in sentence.lower():
            return keyword
    return None

def reflect(sentence):
    # Cambia "io" in "lei", "mio" in "suo", ecc. (molto semplificato)
    replacements = {
        " io ": " lei ",
        " mio ": " suo ",
        " sono ": " è ",
        " me ": " lei ",
        " mi ": " le "
    }
    for k, v in replacements.items():
        sentence = sentence.replace(k, v)
    return sentence

print("Ciao, sono ELIZA. Parli pure, sono qui per ascoltarla. (scrivi 'esci' per terminare)")

while True:
    user_input = input("> ")
    if user_input.lower() in ['esci', 'exit', 'quit']:
        print("Arrivederci! A presto.")
        break

    keyword = find_keyword(user_input)
    if keyword:
        response = random.choice(rules[keyword])
        # A volte riflette la frase dell'utente
        if random.random() > 0.7:
            response = "Perché dice: \"" + reflect(user_input) + "\"?"
        print(response)
    else:
        print(random.choice(default_responses))
