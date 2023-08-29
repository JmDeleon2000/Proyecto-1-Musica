from image import *
from music import *
import random

img = Image("photos/OIG.png")
width = img.getWidth()     # get number of columns in image
height = img.getHeight()   # get number of rows in image

print(width)
print(height)

random.seed(123)


canons = []

canon_simplex =             [ES5, DS5, CS5, BS4, GS4, AS4, BS4, ES4]
canon_simplex_duration =    [1, 1, 1, 1, 1, 1, 1, 1,]

canon_simplex_mod =             [i - 12 for i in canon_simplex]
canon_simplex_duration_mod =    [1, 1, 1, 1, 1, 1, 1, 1,]

allroverscio =             [ES4, FS4, GS4, AS4, CS5, BS4, AS4, ES5]
allroverscio_duration =    [1, 1, 1, 1, 1, 1, 1, 1,]

# Canon en D mayor - Pachelbel (simplificado)
pachelbel_notes = [D4, A4, B4, F4, G4, D4, G4, A4]
pachelbel_durations = [1, 1, 1, 1, 1, 1, 1, 1]

# Canon de Bach (simplificado)
bach_notes = [C4, D4, E4, F4, G4, A4, B4, C5]
bach_durations = [1, 1, 1, 1, 1, 1, 1, 1]

# Chaconne de Händel (simplificado)
handel_notes = [D4, F4, A4, D5, A4, F4, D4, A3]
handel_durations = [1, 1, 1, 1, 1, 1, 1, 1]

# Minueto de Haydn (simplificado)
haydn_notes = [D4, F4, A4, D5, F5, A4, F4, D4]
haydn_durations = [1, 1, 1, 1, 1, 1, 1, 1]

# Canon cancrizans de Bach (simplificado)
bach_cancrizans_notes = [C4, D4, C4, B3, C4, D4, E4, F4]
bach_cancrizans_durations = [1, 1, 1, 1, 1, 1, 1, 1]

# La Harpe de Melodie - Jacob de Senleches (simplificado)
senleches_notes = [G4, A4, B4, C5, D5, E5, F5, G5]
senleches_durations = [1, 1, 1, 1, 1, 1, 1, 1]

# Canon a 4 voces en C mayor de Mozart (simplificado)
mozart_notes = [C4, G4, A4, F4, E4, D4, C4, B3]
mozart_durations = [1, 1, 1, 1, 1, 1, 1, 1]

# Extracto de Sinfonía No. 4 de Beethoven (simplificado)
beethoven_sym4_notes = [E4, F4, G4, A4, B4, C5, D5, E5]
beethoven_sym4_durations = [1, 1, 1, 1, 1, 1, 1, 1]

# ALS Vogel Prophete - Schumann (simplificado)
schumann_notes = [D4, C4, B3, A3, G3, F3, E3, D3]
schumann_durations = [1, 1, 1, 1, 1, 1, 1, 1]

#NuevosCanonsAndres
canon_min7 = [A4, C5, E5, G5, D4, F4, A4, C5, G4, B4, D5, F5, C4, E4, G4, B4]
canon_min7_duration = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

canon_quintas = [C4, G4, A4, E5, D4, A4, B4, F5]
canon_quintas_duration = [1, 1, 1, 1, 1, 1, 1, 1]

canon_melodico = [C4, E4, F4, G4, A4, G4, F4, E4]
canon_melodico_duration = [1, 1, 1, 1, 1, 1, 1, 1]

#canons jorge
canons.append((canon_simplex, canon_simplex_duration))
canons.append((canon_simplex_mod, canon_simplex_duration_mod))
canons.append((allroverscio, allroverscio_duration))
#canons renato
canons.append((pachelbel_notes, pachelbel_durations))
canons.append((bach_notes, bach_durations))
canons.append((handel_notes, handel_durations))
canons.append((haydn_notes, haydn_durations))
canons.append((bach_cancrizans_notes, bach_cancrizans_durations))
canons.append((senleches_notes, senleches_durations))
canons.append((mozart_notes, mozart_durations))
canons.append((beethoven_sym4_notes, beethoven_sym4_durations))
canons.append((schumann_notes, schumann_durations))

#nuevos canons
canons.append((canon_min7, canon_min7_duration))
canons.append((canon_quintas, canon_quintas_duration))
canons.append((canon_melodico, canon_melodico_duration))

score = Score("Untitled", 200)  # Aqui se establece el tempo a 100 BPM


piano_notes = []
piano_durations = []
piano_volumes = []

instrument_notes = []
instrument_durations = []
instrument_volumes = []

new_instrument_notes = []
new_instrument_durations = []
new_instrument_volumes = []

for i in range(0, width, 32):
    for j in range(0, height, 32):
        pixel = img.getPixel(i, j)

        if len(piano_notes) < piano_volumes:
            selected_canon = canons[random.randint(0, len(canons)-1)]
            piano_notes += selected_canon[0]
            piano_durations += selected_canon[1]
        piano_volumes.append(pixel[0])

        if len(instrument_notes) < instrument_volumes:
            selected_canon = canons[random.randint(0, len(canons)-1)]
            instrument_notes += selected_canon[0]
            instrument_durations += selected_canon[1]
        instrument_volumes.append(max(min(pixel[1], 15), 50))
        
        if len(new_instrument_notes) < new_instrument_volumes:
            selected_canon = canons[random.randint(0, len(canons)-1)]
            new_instrument_notes += selected_canon[0]
            new_instrument_durations += selected_canon[1]
        new_instrument_volumes.append(max(min(pixel[2], 15), 75))  # pixel[2] podría ser la componente azul, por ejemplo

for i in range(len(piano_notes)-len(piano_volumes)):
    piano_volumes.append(0)

for i in range(len(instrument_notes)-len(instrument_volumes)):
    instrument_volumes.append(0)
    
for i in range(len(new_instrument_notes) - len(new_instrument_volumes)):
    new_instrument_volumes.append(0)

piano_part = Part('Piano', 0) 
instrument_part = Part(CELLO, 1) 
new_instrument_part = Part(XYLOPHONE, 2)

piano_phrase = Phrase()
instrument_phrase = Phrase()
new_instrument_phrase = Phrase()

piano_phrase.addNoteList(piano_notes, piano_durations, piano_volumes)
instrument_phrase.addNoteList(instrument_notes, instrument_durations, instrument_volumes)
new_instrument_phrase.addNoteList(new_instrument_notes, new_instrument_durations, new_instrument_volumes)

piano_part.addPhrase(piano_phrase)
instrument_part.addPhrase(instrument_phrase)
new_instrument_part.addPhrase(new_instrument_phrase)


score.addPart(piano_part)
score.addPart(instrument_part)
score.addPart(new_instrument_part)

Play.midi(score)

Write.midi(score, "mi_canon.mid")
