from music import *
from time import sleep

'''
La partitura la saque de: https://www.8notes.com/scores/29221.asp

por el momento solo realice la transcripcion de notas y no de duraciones.

DONE: ARREGLAR DURACIONES

'''

# mis arrays
notes_array = [REST, REST, REST, REST, F5, A5, G5, F5, C5, B4, C5, D5, A4, B3, A3, B3, A3, F5, A5, G5, F5, C5, B4, C5, B5, A4, F4, A4, G3, A4, B4, C4, E5, B5, B4, B5, C5, B4, D5, D5, E5, F5, G5, A5, C5, D5, B4, D5, D5, G5, F5, A4, B4, C5, D5, G5, C5, D5, E5, F4, G4, C5, D5] 

notes_array2 = [REST, REST, REST, REST, F5, A5, G5, F5, C5, B4, C5, D5, A4, A3, B3, A3, F5, A5, G5, F5, C5, B4, C5, D5, A4, F4, A4, G3, A4, B4, C5, E5, D5, B4, D5, C5, B4, D5, D5, E5, F5, G5, A5, C5, D5, E5, D5, B4, D5, D5, G5, F5, B4, C5, F5, E5, D5, C5, E5, D5, C5, F4, G4, E4, F4]

durations_array = [WN, WN, WN, WN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, 9, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, QN, HN, QN, DHN, DHN] 

durations_array2 =[WN, WN, WN, WN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, DHN ,DHN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, 9, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, QN, HN, QN, DHN, DHN]

# Creamos la primera partitura con un tempo de 100 BPM
score1 = Score("Satie Gymnopedies no.1 (100 BPM)", 100)
part1 = Part(VIBRAPHONE, 0)  # Usamos VIBRAPHONE como instrumento

# Creamos la primera frase para las notas y duraciones a 100 BPM
phrase1 = Phrase()

for i in range(len(notes_array)):
    phrase1.addNote(Note(notes_array[i], durations_array[i]))

part1.addPhrase(phrase1)
score1.addPart(part1)

# Creamos la segunda partitura con un tempo de 60 BPM
score2 = Score("Satie Gymnopedies no.1 (60 BPM)", 60)
part2 = Part(VIBRAPHONE, 0)

phrase2 = Phrase()

for i in range(len(notes_array2)):
    phrase2.addNote(Note(notes_array2[i], durations_array2[i]))

part2.addPhrase(phrase2)
score2.addPart(part2)

# Reproducimos la primera partitura
#Play.midi(score1)

# Calculamos la duración total de la primera partitura en segundos
total_duration_seconds = sum(durations_array) * (60 / 100)  # Duración * duración de una negra a 100 BPM

# Esperamos la duración total de la primera partitura
sleep(total_duration_seconds)

# Reproducimos la segunda partitura
Play.midi(score2)

