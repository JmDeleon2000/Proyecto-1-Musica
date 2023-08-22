from music import *


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

#print(sum(piano_durations))
#print(sum(piano_durations_fa))
# Creamos la partitura
score = Score("Satie Gymnopedies no.1", 100)  # Aqui se establece el tempo a 100 BPM

# Creamos la parte
sol1 = Part('Piano', 0)   # Parte para clave de sol (una para cada nota de los acordes)
sol2 = Part('Piano', 0)   # Parte para clave de sol (una para cada nota de los acordes)
sol3 = Part('Piano', 0)   # Parte para clave de sol (una para cada nota de los acordes)
fa = Part('Piano', 0)     # Parte para clave de fa

# Creamos las frases
sol1_phrase = Phrase()
sol1_phrase.addNoteList(piano_notes_sol_1, piano_durations)

sol2_phrase = Phrase()
sol2_phrase.addNoteList(piano_notes_sol_2, piano_durations)

sol3_phrase = Phrase()
sol3_phrase.addNoteList(piano_notes_sol_3, piano_durations)

fa_phrase = Phrase()
fa_phrase.addNoteList(piano_notes_fa, piano_durations_fa)

# Anadimos la frase a la parte
sol1.addPhrase(sol1_phrase)
sol2.addPhrase(sol2_phrase)
sol3.addPhrase(sol3_phrase)
fa.addPhrase(fa_phrase)

# Anadimos la parte a la partitura
score.addPart(sol1)
score.addPart(sol2)
score.addPart(sol3)
score.addPart(fa)


# Reproducimos la partitura
Play.midi(score)
