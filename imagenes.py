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

canons.append((canon_simplex, canon_simplex_duration))
canons.append((canon_simplex_mod, canon_simplex_duration_mod))
canons.append((allroverscio, allroverscio_duration))

score = Score("Untitled", 200)  # Aqui se establece el tempo a 100 BPM


piano_notes = []
piano_durations = []
piano_volumes = []

instrument_notes = []
instrument_durations = []
instrument_volumes = []

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

for i in range(len(piano_notes)-len(piano_volumes)):
    piano_volumes.append(0)

for i in range(len(instrument_notes)-len(instrument_volumes)):
    instrument_volumes.append(0)

piano_part = Part('Piano', 0) 
instrument_part = Part(CELLO, 1) 

piano_phrase = Phrase()
instrument_phrase = Phrase()

piano_phrase.addNoteList(piano_notes, piano_durations, piano_volumes)
instrument_phrase.addNoteList(instrument_notes, instrument_durations, instrument_volumes)

piano_part.addPhrase(piano_phrase)
instrument_part.addPhrase(instrument_phrase)


score.addPart(piano_part)
score.addPart(instrument_part)

Play.midi(score)
