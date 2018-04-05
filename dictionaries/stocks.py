STOCK_DICT = {'GM': 'General Motors', 'CAT':'Caterpillar', 'EK':'Eastman Kodak',
              'GE':'General Electric'}

PURCHASES = [('GE', 100, '10-sep-2001', 48), ('CAT', 100, '1-apr-1999', 24),
             ('GE', 200, '1-jul-1998', 56), ('EK', 777, '5-oct-208', 99)]

for x in PURCHASES:
    name = ''
    for key in STOCK_DICT:
        if x[0] == key:
            name = STOCK_DICT[key]
    price = str(x[1] * x[3])
    print(f'On {x[2]} ${price} worth of {name} was purchased')
