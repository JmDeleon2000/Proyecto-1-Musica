from music import *
from time import sleep

# mis arrays vibrafono
notes_array = [REST, REST, REST, REST, REST, F5, A5, G5, F5, C5, B4, C5, D5, A4, B3, A3, B3, A3,REST,  F5, A5, G5, F5, C5, B4, C5, B5, A4, F4, A4, G3, A4, B4, C4, E5, B5, B4, B5, C5, B4, D5, D5, E5, F5, G5, A5, C5, D5, B4, D5, D5, G5, F5, A4, B4, C5, D5, G5, C5, D5, E5, F4, G4, C5, D5] 

notes_array2 = [REST, REST, REST, REST, REST, F5, A5, G5, F5, C5, B4, C5, D5, A4, A3, B3, A3,REST, F5, A5, G5, F5, C5, B4, C5, D5, A4, F4, A4, G3, A4, B4, C5, E5, D5, B4, D5, C5, B4, D5, D5, E5, F5, G5, A5, C5, D5, E5, D5, B4, D5, D5, G5, F5, B4, C5, F5, E5, D5, C5, E5, D5, C5, F4, G4, E4, F4]

durations_array = [DHN,DHN, DHN, DHN,QN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, DHN, DHN,QN,  QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, 9, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, QN, HN, QN, DHN, DHN] 

durations_array2 =[DHN, DHN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, DHN ,DHN,QN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, 9, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, QN, HN, QN, DHN, DHN]

# Creamos la primera partitura con un tempo de 100 BPM
score = Score("Satie Gymnopedies no.1 (100 BPM)", 100)
part_vibraphone = Part(VIBRAPHONE, 1)  # Usamos VIBRAPHONE como instrumento

# Creamos la primera frase para las notas y duraciones a 100 BPM
phrase_vibraphone = Phrase()

for i in range(len(notes_array)):
    phrase_vibraphone.addNote(Note(notes_array[i], durations_array[i]))


for i in range(len(notes_array2)):
    phrase_vibraphone.addNote(Note(notes_array2[i], durations_array2[i]))


part_vibraphone.addPhrase(phrase_vibraphone)

#piano
#primeros dos acordes se repiten 8 veces
piano_notes_sol_1   = [REST,    FS5,    REST,   FS5]*8
piano_notes_sol_2   = [REST,    DS5,    REST,   CS5]*8
piano_notes_sol_3   = [REST,    BS4,    REST,   AS4]*8
piano_durations     = [QN,      2,      QN,     2]*8

piano_notes_fa      =   [GS3,   DS3]*8
piano_durations_fa  =   [3,     3]*8


piano_notes_sol_1   += [REST,   FS5,    REST,   FS5,]
piano_notes_sol_2   += [REST,   CS5,    REST,   DS5,]
piano_notes_sol_3   += [REST,   AS4,    REST,   BS4,]
piano_durations     += [QN,     2,      QN,     2,]

piano_notes_fa      +=  [FS3,   BS3]
piano_durations_fa  +=  [3,     3]

piano_notes_sol_1   += [REST,   REST,    REST,   GS5,]
piano_notes_sol_2   += [REST,   BS4,     REST,   DS5,]
piano_notes_sol_3   += [REST,   GS4,     REST,   BS4,]
piano_durations     += [QN,     2,       QN,     2,]

piano_notes_fa      +=  [ES3,   ES3]
piano_durations_fa  +=  [3,     3]


piano_notes_sol_1   += [REST,   DS5,     REST,   ES5,]
piano_notes_sol_2   += [REST,   AS4,     REST,   C5,]
piano_notes_sol_3   += [REST,   F4,      REST,   AS4,]
piano_durations     += [QN,     2,       QN,     2,]

piano_notes_fa      +=  [DS3,   AS2]
piano_durations_fa  +=  [3,     3]

#Fa se repite por 9 compases
piano_notes_fa      +=  [DS3,]*9
piano_durations_fa  +=  [3, ]*9

piano_notes_sol_1   += [REST,   ES5, ]*2
piano_notes_sol_2   += [REST,   BS4, ]*2
piano_notes_sol_3   += [REST,   GS4, ]*2
piano_durations     += [QN,     2,   ]*2

piano_notes_sol_1   += [REST,   AS4,    REST,   AS4, ]
piano_notes_sol_2   += [REST,   ES4,    REST,   FS4, ]
piano_notes_sol_3   += [REST,   C4,     REST,   C4,  ]
piano_durations     += [QN,     2,      QN,     2,   ]

piano_notes_sol_1   += [REST,   F5,     REST,   ES5, ]
piano_notes_sol_2   += [REST,   C5,     REST,   C5,  ]
piano_notes_sol_3   += [REST,   AS4,    REST,   AS4, ]
piano_durations     += [QN,     2,      QN,     2,   ]

piano_notes_sol_1   += [REST,   ES5,     REST,   AS5, ]
piano_notes_sol_2   += [REST,   BS4,     REST,   ES4, ]
piano_notes_sol_3   += [REST,   GS4,     REST,   C4,  ]
piano_durations     += [QN,     2,       QN,     2,   ]

piano_notes_sol_1   += [REST,   AS5, ]
piano_notes_sol_2   += [REST,   FS4, ]
piano_notes_sol_3   += [REST,   C4,  ]
piano_durations     += [QN,     2,   ]


piano_notes_sol_1   += [REST,   GS5,     REST,   FS5, ]
piano_notes_sol_2   += [REST,   ES5,     REST,   CS5, ]
piano_notes_sol_3   += [REST,   BS4,     REST,   AS4, ]
piano_durations     += [QN,     2,       QN,     2,   ]

piano_notes_fa      +=  [ES3,   FS3,]
piano_durations_fa  +=  [3,     3,  ]


piano_notes_sol_1   += [REST,   FS5,     REST,   AS5, ]
piano_notes_sol_2   += [REST,   DS5,     REST,   ES5, ]
piano_notes_sol_3   += [REST,   BS4,     REST,   CS5, ]
piano_durations     += [QN,     2,       QN,     2,   ]

piano_notes_fa      +=  [BS2,   ES3,]
piano_durations_fa  +=  [3,     3,  ]


piano_notes_sol_1   += [REST,   FS5,     REST,   REST,   GS5,]
piano_notes_sol_2   += [REST,   CS5,     REST,   DS5,    DS5,]
piano_notes_sol_3   += [REST,   AS4,     REST,   AS4,    BS4,]
piano_durations     += [QN,     2,       QN,     1,      1,  ]

piano_notes_fa      +=  [ES2,   ES3,]
piano_durations_fa  +=  [3,     3,  ]


piano_notes_sol_1   += [REST,   ES5,     REST,   AS5, ]
piano_notes_sol_2   += [REST,   C5,      REST,   FS5, ]
piano_notes_sol_3   += [REST,   AS4,     REST,   DS5, ]
piano_durations     += [QN,     2,       QN,     2,   ]

piano_notes_fa      +=  [AS3,   DS3,]
piano_durations_fa  +=  [3,     3,  ]


piano_notes_sol_1   += [REST,   F5,      REST,   F5,  ]
piano_notes_sol_2   += [REST,   DS5,     REST,   C5,  ]
piano_notes_sol_3   += [REST,   AS4,     REST,   AS4, ]
piano_durations     += [QN,     2,       QN,     2,   ]

#Fa se repite por 5 compases
piano_notes_fa      +=  [ES3,]*5
piano_durations_fa  +=  [3,  ]*5


piano_notes_sol_1   += [REST,   AS5,     REST,   F5,  ]
piano_notes_sol_2   += [REST,   ES5,     REST,   C5,  ]
piano_notes_sol_3   += [REST,   C5,      REST,   AS4, ]
piano_durations     += [QN,     2,       QN,     2,   ]


piano_notes_sol_1   += [REST,   AS4,    GS5,]
piano_notes_sol_2   += [REST,   DS4,    DS5,]
piano_notes_sol_3   += [REST,   ES4,    BS4,]
piano_durations     += [QN,     1,      1,  ]

piano_notes_sol_1   += [GS5,]
piano_notes_sol_2   += [ES5,]
piano_notes_sol_3   += [C5, ]
piano_durations     += [3,  ]

piano_notes_fa      +=  [AS3,]
piano_durations_fa  +=  [3,  ]


piano_notes_sol_1   += [AS5,]
piano_notes_sol_2   += [F5, ]
piano_notes_sol_3   += [DS5,]
piano_durations     += [3,  ]

piano_notes_fa      +=  [DS3,]
piano_durations_fa  +=  [3,  ]

# Creamos la parte
sol1 = Part('Piano', 0)   # Parte para clave de sol (una para cada nota de los acordes)
sol2 = Part('Piano', 0)   # Parte para clave de sol (una para cada nota de los acordes)
sol3 = Part('Piano', 0)   # Parte para clave de sol (una para cada nota de los acordes)
fa = Part('Piano', 0)     # Parte para clave de fa

# Creamos las frasespiano_sol1_phrase
piano_sol1_phrase = Phrase()
piano_sol1_phrase.addNoteList(piano_notes_sol_1, piano_durations)

piano_sol2_phrase = Phrase()
piano_sol2_phrase.addNoteList(piano_notes_sol_2, piano_durations)

piano_sol3_phrase = Phrase()
piano_sol3_phrase.addNoteList(piano_notes_sol_3, piano_durations)

piano_fa_phrase = Phrase()
piano_fa_phrase.addNoteList(piano_notes_fa, piano_durations_fa)

# Anadimos la frase a la parte
sol1.addPhrase(piano_sol1_phrase)
sol2.addPhrase(piano_sol2_phrase)
sol3.addPhrase(piano_sol3_phrase)
fa.addPhrase(piano_fa_phrase)



# Mis arrays CELLO
notas_1 = [REST, REST, REST, REST, REST, F4, A4, G4, F4, C4, B3, C4, D4, A3, F3, F3, F3, F3,REST, F4, A4, G4, F4, C4, B3, C4, D4, A3, C4, F4, E3, A3, B3, C4, E4, D4, B3, D4, C4, B3, D4, D4, E4, F4, G4, A4, C4, D4, E4, D4, B3, D4, D4, G4, F4, B3, A3, B3, C4, D4, E4, C4, D4, E4, F3, G3, C4, D4]
notas_2 = [REST, REST, REST, REST, REST, F4, A4, G4, F4, C4, B3, C4, D4, A3, F3, F3, F3, F3,REST, F4, A4, G4, F4, C4, B3, C4, D4, A3, C4, F4, E3, A3, B3, C4, E4, D4, B3, D4, C4, B3, D4, D4, E4, F4, G4, A4, C4, D4, E4, D4, B3, D4, D4, G4, F4, B3, C4, F4, E4, D4, C4, E4, D4, C4, F3, G3, C4, D4]

duraciones_1 = [DHN, DHN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, 9, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, QN, HN, QN, DHN, DHN]
duraciones_2 = [DHN, DHN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN,QN,  DHN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, DHN, DHN, DHN, 9, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, QN, QN, QN, QN, QN, QN, QN, QN, QN, 5, QN, DHN, DHN, QN, QN, QN, QN, QN, QN, QN, QN, QN, HN, QN, DHN, DHN]

# Ajustar el volumen deseado
volumen_deseado = 55  # Puedes cambiar este número según tus necesidades

part_cello = Part(CELLO, 2)  # Usamos CELLO como instrumento

phrase_cello = Phrase()

for i in range(len(notas_1)):
    nota = Note(notas_1[i], duraciones_1[i])
    nota.setDynamic(volumen_deseado)  # Ajustar el volumen
    phrase_cello.addNote(nota)

for i in range(len(notas_2)):
    nota = Note(notas_2[i], duraciones_2[i])
    nota.setDynamic(volumen_deseado)  # Ajustar el volumen
    phrase_cello.addNote(nota)

part_cello.addPhrase(phrase_cello)


flutePart = Part(FLUTE , 3) # create flute part
 
phrase_flute = Phrase(0.0)      # create the phrase
 
# write music in a convenient way
flute_notes    = [REST, REST, REST, REST]
durationList   = [DHN, DHN,  DHN, DHN]

flute_notes    += [REST, FS5, A5, G5, FS5, CS5, B4, CS5, D5]
durationList   += [QN, QN, QN, QN, QN, QN, QN, QN, QN]

flute_notes    += [A4, F4]
durationList   += [DHN, DHN * 4]

flute_notes    += [REST, FS5, A5, G5, FS5, CS5, B4, CS5, D5]
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
phrase_flute.addNoteList(flute_notes, durationList)
phrase_flute.addNoteList(flute_notes_part1, durationList_part1)
phrase_flute.addNoteList(flute_notes, durationList)
phrase_flute.addNoteList(flute_notes_part2, durationList_part2)

 
flutePart.addPhrase(phrase_flute)   # add phrases to part

score.addPart(flutePart)

# Anadimos la parte a la partitura
score.addPart(sol1)
score.addPart(sol2)
score.addPart(sol3)
score.addPart(fa)

#anadir vibrafono
score.addPart(part_vibraphone)

#anadir cello
score.addPart(part_cello)

# Reproducimos la segunda partitura
Play.midi(score)
