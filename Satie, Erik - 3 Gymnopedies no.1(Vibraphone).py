from music import *

'''
La partitura la saque de: https://www.8notes.com/scores/29221.asp

por el momento solo realice la transcripcion de notas y no de duraciones.

TODO: ARREGLAR DURACIONES

'''
# Notas y ritmos de la pieza basados en la información proporcionada
notes = [
    FS5, A5, G5, FS5, CS5, B4, CS5, D5, A4, B3, D4, FS4, A3, CS4, FS4, B3, D4, FS4, A3, CS4, FS4, FS5, 
    A5, G5, FS5, CS5, B4, CS5, D5, A4, FS4, A4, CS5, A4, CS5, FS5, G3, B3, E4, A4, B4, C5, E5, D5, B4, 
    D5, C5, B4, D5, D5, E5, F5, G5, A5, C5, D5, E5, D5, B4, D5, D5, G5, FS5, B4, A4, B4, CS5, D5, E5, 
    CS5, D5, E5, FS4, G4, C5, D5, FS5, A5, G5, FS5, CS5, B4, CS5, D5, A4, B3, D4, FS4, A3, CS4, FS4, B3, 
    D4, FS4, A3, CS4, FS4, FS5, A5, G5, FS5, CS5, B4, CS5, D5, A4, FS4, A4, CS5, A4, CS5, FS5, G3, B3, E4, 
    A4, B4, C5, E5, D5, B4, D5, C5, B4, D5, D5, E5, F5, G5, A5, C5, D5, E5, D5, B4, D5, D5, G5, F5, B4, 
    C5, F5, E5, D5, C5, E5, D5, C5
]
rhythms = [
    QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, 
    QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, 
    QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, 
    QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, 
    QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, 
    QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN
]

# Creamos la partitura
score = Score("Satie Gymnopedies no.1", 100)  # Aquí se establece el tempo a 100 BPM

# Creamos la parte
part = Part(VIBRAPHONE, 0)  # Usando VIBRAPHONE como instrumento

# Creamos la frase
phrase = Phrase()
print(len(notes))
print(len(rhythms))

# Añadimos las notas y los ritmos a la frase
for i in range(len(notes)):
    phrase.addNote(Note(notes[i], rhythms[i]))

# Añadimos la frase a la parte
part.addPhrase(phrase)

# Añadimos la parte a la partitura
score.addPart(part)

# Reproducimos la partitura
Play.midi(score)
