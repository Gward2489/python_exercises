SHOW_ROOM = set(['volvo 850', 'honda crv', 'nissan sentra', 'toyota corolla'])

print(len(SHOW_ROOM))

SHOW_ROOM.add('volvo 850')

print(len(SHOW_ROOM))

ADDITIONS = set(['suburu outback', 'sauub express'])

SHOW_ROOM.update(ADDITIONS)

print(SHOW_ROOM)

SHOW_ROOM.discard('honda crv')

print(SHOW_ROOM)

JUNK_YARD = set(['ford focus', 'toyota acura', 'volvo 850', 'sauub express'])

print(SHOW_ROOM.intersection(JUNK_YARD))

SHOW_ROOM.union(JUNK_YARD)

SHOW_ROOM.discard('toyota acura')

print(SHOW_ROOM)
