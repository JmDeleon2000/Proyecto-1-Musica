# pianoPhase.py
# Plays Steve Reich's minimalist piece, Piano Phase (1967).
 
from music import *

##### define the data structure
score = Score("Satie Gymnopedies no.1", 68.0) # tempo is 68 bpm
 
flutePart = Part(FLUTE , 0) # create flute part
 
phrase1 = Phrase(0.0)      # create the phrase
 
# write music in a convenient way
flute_notes    = [REST, REST, REST, REST]
durationList   = [DHN, DHN,  DHN, DHN]

flute_notes    += [REST, FF5, A5, G5, FF5, CS5, B4, CF5, D5]
durationList   += [QN, QN, QN, QN, QN, QN, QN, QN, QN]

flute_notes    += [A4, F4]
durationList   += [DHN, DHN * 4]

flute_notes    += [REST, FF5, A5, G5, FF5, CS5, B4, CF5, D5]
durationList   += [QN, QN, QN, QN, QN, QN, QN, QN, QN]

flute_notes    += [A4, CF5, FS5, E4]
durationList   += [DHN, DHN, DHN, DHN * 3]

flute_notes    += [A4, B4, C5, E5, D5, B4, D5, C5, B4]
durationList   += [QN, QN, QN, QN, QN, QN, QN, QN, QN]

flute_notes    += [D5]
durationList   += [DHN + HN]

flute_notes    += [D5, E5, F5, G5, A5, C5, D5, E5, D5, B4]
durationList   += [QN, QN, QN, QN, QN, QN, QN, QN, QN, QN]

flute_notes    += [D5, D5, G5]
durationList   += [DHN + HN, QN, DHN]

#Parte 1
flute_notes_part1 = [FS5, B4, A4, B4, CS5, D5, E5, CS5, D5, E5]
durationList_part1 = [DHN, QN, QN ,QN , QN, QN, QN, QN, QN, QN]

flute_notes_part1 += [F4, C5, D5]
durationList_part1 += [DHN, DHN, DHN]
 
#Parte 2
flute_notes_part2 = [F5]
durationList_part2 = [DHN]

flute_notes_part2 += [B4, C5, F5, E5, D5, C5, E5, D5, C5]
durationList_part2 += [QN, QN, QN, QN, QN, QN, QN, QN, QN]

flute_notes_part2 += [F4, C5, D5]
durationList_part2 += [DHN, DHN, DHN]

# add the same notes to both phrases
phrase1.addNoteList(flute_notes, durationList)
phrase1.addNoteList(flute_notes_part1, durationList_part1)
phrase1.addNoteList(flute_notes, durationList)
phrase1.addNoteList(flute_notes_part2, durationList_part2)
 
phrase1.setTempo(68.0)   # set tempo to 68 beats-per-minute
 
flutePart.addPhrase(phrase1)   # add phrases to part
 
Play.midi(flutePart)      # play music