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

# Chaconne de Handel (simplificado)
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

# Extracto de Sinfonia No. 4 de Beethoven (simplificado)
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


instrument0_notes = []
instrument0_durations = []
instrument0_volumes = []

instrument1_notes = []
instrument1_durations = []
instrument1_volumes = []

instrument2_notes = []
instrument2_durations = []
instrument2_volumes = []

instrument3_notes = []
instrument3_durations = []
instrument3_volumes = []

for i in range(0, width, 32):
    for j in range(0, height, 32):
        pixel = img.getPixel(i, j)

        if len(instrument0_notes) < instrument0_volumes:
            selected_canon = canons[random.randint(0, len(canons)-1)]
            instrument0_notes += selected_canon[0]
            instrument0_durations += selected_canon[1]
        instrument0_volumes.append(pixel[0])

        if len(instrument1_notes) < instrument1_volumes:
            selected_canon = canons[random.randint(0, len(canons)-1)]
            instrument1_notes += selected_canon[0]
            instrument1_durations += selected_canon[1]
        instrument1_volumes.append(max(min(pixel[1], 15), 50))


        if len(instrument2_notes) < instrument2_volumes:
            selected_canon = canons[random.randint(0, len(canons)-1)]
            instrument2_notes += selected_canon[0]
            instrument2_durations += selected_canon[1]
        instrument2_volumes.append(max(min(pixel[2], 15), 75))

        if len(instrument3_notes) < instrument3_volumes:
            selected_canon = canons[random.randint(0, len(canons)-1)]
            instrument3_notes += selected_canon[0]
            instrument3_durations += selected_canon[1]
        avg = (pixel[0] + pixel[1] + pixel[2])/3
        instrument3_volumes.append(max(min(255-avg, 15), 75))

for i in range(len(instrument0_notes)-len(instrument0_volumes)):
    instrument0_volumes.append(0)

for i in range(len(instrument1_notes)-len(instrument1_volumes)):
    instrument1_volumes.append(0)

for i in range(len(instrument2_notes)-len(instrument2_volumes)):
    instrument2_volumes.append(0)

for i in range(len(instrument3_notes)-len(instrument3_volumes)):
    instrument3_volumes.append(0)

instrument0_part = Part('Piano', 0) 
instrument1_part = Part(CELLO, 1) 
instrument2_part = Part(XYLOPHONE, 2) 
instrument3_part = Part(FLUTE, 3) 

instrument0_phrase = Phrase()
instrument1_phrase = Phrase()
instrument2_phrase = Phrase()
instrument3_phrase = Phrase()

instrument0_phrase.addNoteList(instrument0_notes, instrument0_durations, instrument0_volumes)
instrument1_phrase.addNoteList(instrument1_notes, instrument1_durations, instrument1_volumes)
instrument2_phrase.addNoteList(instrument2_notes, instrument2_durations, instrument2_volumes)
instrument3_phrase.addNoteList(instrument3_notes, instrument3_durations, instrument3_volumes)

instrument0_part.addPhrase(instrument0_phrase)
instrument1_part.addPhrase(instrument1_phrase)
instrument2_part.addPhrase(instrument2_phrase)
instrument3_part.addPhrase(instrument3_phrase)


score.addPart(instrument0_part)
score.addPart(instrument1_part)
score.addPart(instrument2_part)
score.addPart(instrument3_part)

Play.midi(score)
Write.midi(score, "score.mid")