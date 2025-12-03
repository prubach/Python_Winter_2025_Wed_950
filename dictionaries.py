days_of_week={
    'Monday':0,
    'Tuesday':1,
    'Wednesday':2,
    'Thursday':3}

#days_of_week={'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3}

print(days_of_week.get('Mondaydh'))  # - returns None if not found
print(days_of_week.get('Mondaydh', 1000))  # - returns 1000 if not found
#print(days_of_week['Mondaygdf']) # - KeyError if not found



exch_rates = {'PLN': 3.7, 'EUR': 0.8}
print(exch_rates)
exch_rates = {}
exch_rates['PLN'] = 3.8
exch_rates['USD'] = 1.0
for k, v in exch_rates.items():
    print(f'{k}: {v}')
print('--------')
for k in exch_rates.keys():
    print(f'{k}: {exch_rates[k]}')
print('--------')
print(exch_rates.keys()) # - dict_keys - special type
print(list(exch_rates.keys())) # - regular list

print(exch_rates.values())
print(list(exch_rates.values()))


print('----------------------')
myl = [('EUR', 4.2), ('USD', 1.1), ('EUR', 3.9)]
print(myl)
my_dict = dict(myl)
print(my_dict)

my_courses = [x[1] for x in myl]
print(my_courses)
print(f'Sum: {sum(my_courses)}')
print(f'Max: {max(my_courses)}')
print(f'Min: {min(my_courses)}')
