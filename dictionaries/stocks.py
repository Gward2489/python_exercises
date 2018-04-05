STOCK_DICT = {'GM': 'General Motors', 'CAT':'Caterpillar', 'EK':'Eastman Kodak',
              'GE':'General Electric', 'NIN': 'Nintendo'}

PURCHASES = [('GE', 100, '10-sep-2001', 48), ('CAT', 100, '1-apr-1999', 24),
             ('GE', 200, '1-jul-1998', 56), ('EK', 777, '5-oct-2008', 99),
             ('NIN', 68, '8-aug-2003', 435), ('GM', 666, '9-feb-1999', 420),
             ('GM', 606, '12-feb-1999', 520), ('NIN', 68, '8-aug-2003', 435)]

print('')
print('Purchase History:')

for x in PURCHASES:
    name = ''
    for key in STOCK_DICT:
        if x[0] == key:
            name = STOCK_DICT[key]
    price = str(x[1] * x[3])
    print(f'On {x[2]} ${price} worth of {name} was purchased')

print('')
print('Totals:')

for key in STOCK_DICT:
    current_total = 0
    for x in PURCHASES:
        if key == x[0]:
            current_total += x[1] * x[3]
    print(f'{key}: ${str(current_total)}')
