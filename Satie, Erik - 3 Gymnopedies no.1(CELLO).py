from music import *
from time import sleep

# Tus arrays
notas_1 = [REST, REST, REST, REST,F4, A4, G4, F4, C4, B3, C4, D4, A3, F3, F3, F3, F3, F4, A4, G4, F4, C4, B3, C4, D4, A3, C4, F4, E3, A3, B3, C4, E4, D4, B3, D4, C4, B3, D4, D4, E4, F4, G4, A4, C4, D4, E4, D4, B3, D4, D4, G4, F4, B3, A3, B3, C4, D4, E4, C4, D4, E4, F3, G3, C4, D4]
notas_2 = [REST, REST, REST, REST, F4, A4, G4, F4, C4, B3, C4, D4, A3, F3, F3, F3, F3, F4, A4, G4, F4, C4, B3, C4, D4, A3, C4, F4, E3, A3, B3, C4, E4, D4, B3, D4, C4, B3, D4, D4, E4, F4, G4, A4, C4, D4, E4, D4, B3, D4, D4, G4, F4, B3, C4, F4, E4, D4, C4, E4, D4, C4, F3, G3, C4, D4]

duraciones_1 = [WN, WN, WN, WN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, 9, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, QN, HN, QN, DHN, DHN]
duraciones_2 = [WN, WN, WN, WN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, 9, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, QN, HN, QN, DHN, DHN]

# Creamos la partitura a 100 BPM
score1 = Score("Satie Gymnopedies no.1 (100 BPM)", 100)
part1 = Part(CELLO, 0)  # Usamos CELLO como instrumento

phrase1 = Phrase()

for i in range(len(notas_1)):
    phrase1.addNote(Note(notas_1[i], duraciones_1[i]))

part1.addPhrase(phrase1)
score1.addPart(part1)

# Creamos la partitura a 60 BPM
score2 = Score("Satie Gymnopedies no.1 (60 BPM)", 60)
part2 = Part(CELLO, 0)

phrase2 = Phrase()

for i in range(len(notas_2)):
    phrase2.addNote(Note(notas_2[i], duraciones_2[i]))

part2.addPhrase(phrase2)
score2.addPart(part2)

# Reproducimos la partitura a 100 BPM
#Play.midi(score1)

# Calculamos la duración total de la primera partitura en segundos
total_duration_seconds = sum(duraciones_1) * (60 / 100)  # Duración * duración de una negra a 100 BPM

# Esperamos la duración total de la primera partitura
sleep(total_duration_seconds)

# Reproducimos la partitura a 60 BPM
Play.midi(score2)
